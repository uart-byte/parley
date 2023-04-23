# formatted with python black, line length 200

import os, random
import openai
import gradio as gr
from game_content import GAME_INTRO_CHOICES, NOTES_TO_THE_NARRATOR_AT_START, AWAITING_INPUT, NOTES_TO_THE_NARRATOR_EVERY_TIME
from game_content import game_over_victory_txt, game_over_fail_txt, S_GAME_OVER
from game_content import N_TURNS_REQUIRED_TO_PASS_FIRST_BANDIT_ENCOUNTER, N_TURNS_REQUIRED_TO_REACH_HOME
import decider_utils
from decider_utils import YES, NO
from decider_questions import *  # QUESTION_IS_USER_HOME, QUESTION_IS_USER_ENGAGED_WITH_BANDITS, etc.
from webpage import PAGE_STYLING_JS, PLEASE_BE_PATIENT_DIV, TOP_OF_SCREEN_PADDING_DIV


N_COMPLETIONS_WHEN_ELABORATING = 1  # I previously had this set to 3, but that made the program very slow.
MINIMUM_COMPLETION_LENGTH_CHARS_WHEN_ELABORATING = 7


def elaborate(
    str_beginning,
    prevent_user_from_reaching_home=True,
    require_user_to_be_still_engaged_with_bandits=False,
):

    longest_completion = ""

    while len(longest_completion) < MINIMUM_COMPLETION_LENGTH_CHARS_WHEN_ELABORATING:
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=str_beginning,
            temperature=0.5,
            max_tokens=4000 - int(len(str_beginning) / 4),
            frequency_penalty=0.5,
            presence_penalty=0.5,
            n=N_COMPLETIONS_WHEN_ELABORATING,
        )["choices"]

        for i in range(0, N_COMPLETIONS_WHEN_ELABORATING):
            completion = completions[i]["text"]
            # debug_print(completion)

            allowed = True
            if prevent_user_from_reaching_home:
                does_the_user_reach_home = decider_utils.yesno(QUESTION_IS_USER_HOME, str_beginning + completion, default=YES)
                allowed = not does_the_user_reach_home

            if require_user_to_be_still_engaged_with_bandits:
                is_user_engaged_with_bandits = decider_utils.yesno(
                    QUESTION_IS_USER_ENGAGED_WITH_BANDITS,
                    str_beginning + completion,
                    default=YES,
                )
                allowed = allowed and is_user_engaged_with_bandits

            if allowed and len(completion) > len(longest_completion):
                longest_completion = completion

    return str_beginning + longest_completion


def run_1_game_turn(s_narr_transcript, s_n_turns_elapsed, s_user_transcript, s_user_input):
    n_turns_elapsed = int(s_n_turns_elapsed)

    finally_add2_both_tscripts = ""

    if s_user_input == "":
        s_user_transcript += "You must choose an action.\n"

    elif S_GAME_OVER in s_narr_transcript:
        s_user_transcript += "Sorry, the game is already over.  To play again, please refresh the page.\n"

    elif decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, s_user_input, default=NO):
        finally_add2_both_tscripts += game_over_fail_txt("You have taken an action that is likely to result in killing someone.")

    elif decider_utils.yesno(QUESTION_IS_USER_ENGAGED_WITH_BANDITS, s_narr_transcript, default=NO) and decider_utils.yesno(QUESTION_IS_ACTION_RUNNING_AWAY, s_user_input, default=NO):
        finally_add2_both_tscripts += "Invalid entry.  You cannot outrun these bandits.\n"

    elif decider_utils.yesno(QUESTION_IS_ACTION_MAGIC, s_user_input, default=NO):
        finally_add2_both_tscripts += "Invalid entry.  You are not a spellcaster and have no magic items except your revolver.\n"

    else:
        # User input accepted.
        n_turns_elapsed += 1
        s_user_transcript += s_user_input + "\n"
        s_narr_transcript += s_user_input + "\n"
        s_narr_transcript += NOTES_TO_THE_NARRATOR_EVERY_TIME

        s_new_narr_transcript = elaborate(
            s_narr_transcript,
            prevent_user_from_reaching_home=n_turns_elapsed < N_TURNS_REQUIRED_TO_REACH_HOME,
            require_user_to_be_still_engaged_with_bandits=n_turns_elapsed < N_TURNS_REQUIRED_TO_PASS_FIRST_BANDIT_ENCOUNTER,
        )

        s_new_part = s_new_narr_transcript.replace(s_narr_transcript, "")

        s_narr_transcript += s_new_part + "\n"
        s_user_transcript += s_new_part + "\n"

        did_user_kill = decider_utils.yesno(QUESTION_DID_PROTAGONIST_KILL, s_new_part, default=NO)
        did_user_kill = did_user_kill or decider_utils.yesno(QUESTION_DID_PROTAGONIST_KILL, s_narr_transcript, default=NO)
        if did_user_kill:
            finally_add2_both_tscripts += game_over_fail_txt("You have taken a life.")

        else:
            is_user_home = decider_utils.yesno(QUESTION_IS_USER_HOME, s_narr_transcript, default=NO)
            if is_user_home:
                has_at_least_30_gold = decider_utils.yesno(QUESTION_DOES_USER_STILL_HAVE_AT_LEAST_30_GOLD, s_narr_transcript, default=NO)
                if has_at_least_30_gold:
                    finally_add2_both_tscripts += game_over_victory_txt("You made it home with 30+ gold!  Your family is grateful and you all hug in celebration.")
                else:
                    finally_add2_both_tscripts += game_over_fail_txt("You reached home with less than 30 gold - too little for your family to live on.")

        # End of code block User input accepted.

    s_n_turns_elapsed = str(n_turns_elapsed)
    s_user_input = ""

    if S_GAME_OVER not in finally_add2_both_tscripts and S_GAME_OVER not in s_narr_transcript:
        finally_add2_both_tscripts += AWAITING_INPUT

    s_narr_transcript += finally_add2_both_tscripts
    s_user_transcript += finally_add2_both_tscripts

    return [s_narr_transcript, s_n_turns_elapsed, s_user_transcript, s_user_input]


openai.organization = os.environ.get("OPENAI_ORGANIZATION")
openai.api_key = os.environ.get("OPENAI_KEY")


demo = gr.Blocks()

with demo:
    game_intro = random.choice(GAME_INTRO_CHOICES)

    s_narr_transcript = game_intro + NOTES_TO_THE_NARRATOR_AT_START + AWAITING_INPUT
    s_user_transcript = game_intro + AWAITING_INPUT

    gr_top_of_scr_padding = gr.HTML(TOP_OF_SCREEN_PADDING_DIV)

    gr_narr_transcript = gr.Textbox(label="", value=s_narr_transcript, interactive=False, max_lines=9999, visible=False)
    gr_user_transcript = gr.Textbox(label="", value=s_user_transcript, interactive=False, max_lines=9999, elem_classes="parleygame")

    gr_pls_be_patient = gr.HTML(PLEASE_BE_PATIENT_DIV)

    gr_user_input = gr.Textbox(label="", value="", placeholder="Describe your next action here...", interactive=True)
    gr_button1 = gr.Button(value="Run Next Turn")

    gr_n_turns_elapsed = gr.Textbox(label="N Turns Elapsed", value="0", interactive=False)

    gr_button1.click(
        fn=run_1_game_turn, inputs=[gr_narr_transcript, gr_n_turns_elapsed, gr_user_transcript, gr_user_input], outputs=[gr_narr_transcript, gr_n_turns_elapsed, gr_user_transcript, gr_user_input]
    )

    # See https://discuss.huggingface.co/t/gradio-html-component-with-javascript-code-dont-work/37316/2
    demo.load(None, None, None, _js=PAGE_STYLING_JS)


demo.launch()
