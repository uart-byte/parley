# import uuid
import gradio as gr

GAME_INTRO = '''-----------------------------------  -------------------
- ----- -----                                          -
- PARLEY -                                             -
- -----                                                -
-   The one-of-a-kind role playing game                -
-   that tests your ability to achieve                 -
-   your objective without killing                     -
-   any sentient beings.                               -
- -----                                                -
-------------- ------------------------------- ------- -

The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been traveling for weeks now and you are nearing the end of your journey. You can see the border between Tibet and Nepal in the distance, but before you can cross it, you must pass through a narrow mountain pass. As you enter the pass, you hear a voice call out from behind you.

"Halt! This is our territory now." 

You turn around to find two bandits blocking your path, each armed with a magical revolver. They demand that you hand over half of your gold coins as 'protection money'. You know that if you give them what they want, there's no guarantee that they won't just take all of it anyway. On the other hand, if you refuse to pay up then they could easily shoot you down and take all of your coins anyway. 

What do you do?
'''

NOTES_TO_THE_NARRATOR = '''
IMPORTANT NOTES TO THE NARRATOR:
BANDITS ARE TOUGH, POWERFUL CHARACTERS THAT CANNOT BE EASILY DEFEATED OR FOOLED.
ATTEMPTS TO REACH HOME MUST ALWAYS BE FOILED BY GETTING LOST, ENCOUNTERING DANGEROUS WILD ANIMALS, OR ENCOUNTERING MORE BANDITS.

'''

AWAITING_INPUT = '''Awaiting user input:
'''


def run_1_game_turn(s_narrator_transcript, s_n_turns_elapsed, s_print_output, s_user_input):
    n_turns_elapsed = int(s_n_turns_elapsed)

    if s_narrator_transcript == "":
        # New user or a user is starting over.
        
        s_print_output += GAME_INTRO
        s_narrator_transcript += GAME_INTRO

        s_narrator_transcript += NOTES_TO_THE_NARRATOR

    n_turns_elapsed += 1

    s_n_turns_elapsed = str(n_turns_elapsed)
    s_user_input = ""
    return [s_narrator_transcript, s_n_turns_elapsed, s_print_output, s_user_input]


demo = gr.Blocks()

with demo:
    # unique_session_key = str(uuid.uuid4())

    gr_narrator_transcript = gr.Textbox(value=GAME_INTRO + NOTES_TO_THE_NARRATOR + AWAITING_INPUT, interactive=False) #, visible=False)
    gr_n_turns_elapsed = gr.Textbox(value="0", interactive=False) #, visible=False)
    gr_print_output = gr.Textbox(label="", value=GAME_INTRO + AWAITING_INPUT, interactive=False)
    gr_user_input = gr.Textbox(label="", value="", interactive=True)
    gr_button1 = gr.Button(value="Run Next Turn")
    
    gr_button1.click(fn=run_1_game_turn,
        inputs=[gr_narrator_transcript, gr_n_turns_elapsed, gr_print_output, gr_user_input],
        outputs=[gr_narrator_transcript, gr_n_turns_elapsed, gr_print_output, gr_user_input])

demo.launch()
