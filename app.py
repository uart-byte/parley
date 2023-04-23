import gradio as gr
from game_content import GAME_INTRO, NOTES_TO_THE_NARRATOR, AWAITING_INPUT
from game_content import game_over_victory_txt, game_over_fail_txt, S_GAME_OVER
import decider_utils
from decider_utils import YES, NO
from decider_questions import *   # QUESTION_IS_USER_HOME and other questions









N_COMPLETIONS_WHEN_ELABORATING = 1  # I previously had this set to 3, but that made the program very slow.
MINIMUM_COMPLETION_LENGTH_CHARS_WHEN_ELABORATING = 7



N_TURNS_REQUIRED_TO_PASS_FIRST_BANDIT_ENCOUNTER = 3
N_TURNS_REQUIRED_TO_REACH_HOME = 6


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
        s_user_transcript += "You must choose an action."

    elif S_GAME_OVER in s_narr_transcript:
        s_user_transcript += "Sorry, the game is already over.  To play again, please refresh the page."

    elif decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, s_user_input, default=NO):
        finally_add2_both_tscripts += game_over_fail_txt("You have taken an action that is likely to result in killing someone.")

    else:
        # User input accepted.

        n_turns_elapsed += 1



    s_n_turns_elapsed = str(n_turns_elapsed)
    s_user_input = ""
    
    s_narr_transcript += finally_add2_both_tscripts
    s_user_transcript += finally_add2_both_tscripts

    return [s_narr_transcript, s_n_turns_elapsed, s_user_transcript, s_user_input]


demo = gr.Blocks()

with demo:
    s_narr_transcript = GAME_INTRO + NOTES_TO_THE_NARRATOR + AWAITING_INPUT
    s_user_transcript = GAME_INTRO + AWAITING_INPUT

    gr_narr_transcript = gr.Textbox(label="", value=s_narr_transcript, interactive=False, max_lines=9999) #, visible=False)
    gr_user_transcript = gr.Textbox(label="", value=s_user_transcript, interactive=False, max_lines=9999)

    gr_markdown1 = gr.Markdown("After clicking Run Next Turn, please be patient as it may take up to a minute for the game state to update.")
    gr_user_input = gr.Textbox(label="", value="", placeholder="Describe your next action here...", interactive=True)
    gr_button1 = gr.Button(value="Run Next Turn")

    gr_n_turns_elapsed = gr.Textbox(label="N Turns Elapsed", value="0", interactive=False)
    
    gr_button1.click(fn=run_1_game_turn,
        inputs=[gr_narr_transcript, gr_n_turns_elapsed, gr_user_transcript, gr_user_input],
        outputs=[gr_narr_transcript, gr_n_turns_elapsed, gr_user_transcript, gr_user_input])

demo.launch()
