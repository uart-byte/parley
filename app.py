import gradio as gr
from game_content import GAME_INTRO, NOTES_TO_THE_NARRATOR, AWAITING_INPUT
import decider_utils
from decider_utils import YES, NO










N_COMPLETIONS_WHEN_ELABORATING = 1  # I previously had this set to 3, but that made the program very slow.
MINIMUM_COMPLETION_LENGTH_CHARS_WHEN_ELABORATING = 7

QUESTION_IS_USER_HOME = "At the end of the above story, is the protagonist located at their destination?"
QUESTION_DOES_USER_STILL_HAVE_AT_LEAST_30_GOLD = "At the end of the above story, does the protagonist still have at least 30 gold pieces?"
QUESTION_IS_USER_ENGAGED_WITH_BANDITS = "At the end of the above story, is the protagonist currently still engaged in a standoff with bandits?"
QUESTION_IS_ACTION_LIKELY_LETHAL = "Is the action just described likely to result in anyone dying?"
QUESTION_IS_ACTION_RUNNING_AWAY = "Is the action just described an example of running away by sprinting?"
QUESTION_IS_ACTION_MAGIC = "Is the action just described an example of using supernatural magical spells / potions / etc?"
QUESTION_DID_PROTAGONIST_KILL = "In the story segment above, did the protagonist kill anyone?"
QUESTION_DID_PROTAGONIST_PERISH = "In the story segment above, does the protagonist get killed?"

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











def run_1_game_turn(s_narrator_transcript, s_n_turns_elapsed, s_print_output, s_user_input):
    n_turns_elapsed = int(s_n_turns_elapsed)
    n_turns_elapsed += 1

    s_n_turns_elapsed = str(n_turns_elapsed)
    s_user_input = ""
    return [s_narrator_transcript, s_n_turns_elapsed, s_print_output, s_user_input]


demo = gr.Blocks()

with demo:
    # unique_session_key = str(uuid.uuid4())

    gr_narrator_transcript = gr.Textbox(value=GAME_INTRO + NOTES_TO_THE_NARRATOR + AWAITING_INPUT, interactive=False) #, visible=False)
    gr_n_turns_elapsed = gr.Textbox(value="0", interactive=False) #, visible=False)
    gr_print_output = gr.Textbox(label="", value=GAME_INTRO + AWAITING_INPUT, interactive=False, max_lines=9999)
    gr_markdown1 = gr.Markdown("After clicking Run Next Turn, please be patient as it may take up to a minute for the game state to update.")
    gr_user_input = gr.Textbox(label="", value="", placeholder="Describe your next action here...", interactive=True)
    gr_button1 = gr.Button(value="Run Next Turn")
    
    gr_button1.click(fn=run_1_game_turn,
        inputs=[gr_narrator_transcript, gr_n_turns_elapsed, gr_print_output, gr_user_input],
        outputs=[gr_narrator_transcript, gr_n_turns_elapsed, gr_print_output, gr_user_input])

demo.launch()
