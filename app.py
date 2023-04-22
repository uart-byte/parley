import streamlit as st
import os
import textwrap
import openai

openai.organization = os.environ.get("OPENAI_ORGANIZATION")
openai.api_key = os.environ.get("OPENAI_KEY")

LINE_WIDTH = 80

G_USER_TRANSCRIPT_KEY = "G_USER_TRANSCRIPT_KEY"
G_NARRATOR_TRANSCRIPT_KEY = "G_NARRATOR_TRANSCRIPT_KEY"
# G_GAME_OVER_KEY = "G_GAME_OVER_KEY"


# ui() means print only to the user.
def ui(s=""):
    user_transcript = ""
    if G_USER_TRANSCRIPT_KEY in st.session_state:
        user_transcript = st.session_state[G_USER_TRANSCRIPT_KEY]
    st.session_state[G_USER_TRANSCRIPT_KEY] = user_transcript + s + "\n"


# this adds to only the narrator transcript
def add_to_narrator_transcript(s=""):
    narr_transcript = ""
    if G_NARRATOR_TRANSCRIPT_KEY in st.session_state:
        narr_transcript = st.session_state[G_NARRATOR_TRANSCRIPT_KEY]
    st.session_state[G_NARRATOR_TRANSCRIPT_KEY] = narr_transcript + s + "\n"


# p() means print to user screen and narrator transcript.
def p(s=""):
    add_to_narrator_transcript(s)
    ui(s)


def retrieve_user_transcript():
    if G_USER_TRANSCRIPT_KEY in st.session_state:
        return st.session_state[G_USER_TRANSCRIPT_KEY]
    else:
        return ""
    
def retrieve_narrator_transcript():
    if G_NARRATOR_TRANSCRIPT_KEY in st.session_state:
        return st.session_state[G_NARRATOR_TRANSCRIPT_KEY]
    else:
        return ""

def apply_word_wrap(multi_paragraph_str):
    paragraphs_in = multi_paragraph_str.split("\n")
    paragraphs_out = []
    for p in paragraphs_in:
        paragraphs_out.append(textwrap.fill(p, width=LINE_WIDTH))
    return "\n".join(paragraphs_out)


# def set_game_over

# def is_game_over():
#     if G_GAME_OVER_KEY in st.session_state and st.session_state[G_GAME_OVER_KEY] == True:
#         return True
#     else:
#         return False


# Begin an attempt at Streamlit literate programming

SCENARIO_INTRO_3 = """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been traveling for weeks now and you are nearing the end of your journey. You can see the border between Tibet and Nepal in the distance, but before you can cross it, you must pass through a narrow mountain pass. As you enter the pass, you hear a voice call out from behind you.

"Halt! This is our territory now." 

You turn around to find two bandits blocking your path, each armed with a magical revolver. They demand that you hand over half of your gold coins as 'protection money'. You know that if you give them what they want, there's no guarantee that they won't just take all of it anyway. On the other hand, if you refuse to pay up then they could easily shoot you down and take all of your coins anyway. 

What do you do?"""


st.title("PARLEY")


if G_USER_TRANSCRIPT_KEY not in st.session_state:
    # New user

    p()
    p("-----------------------------------  -------------------")
    p("- ----- -----                                          -")
    p("- PARLEY -                                             -")
    p("- -----                                                -")
    p("-   The one-of-a-kind role playing game                -")
    p("-   that tests your ability to achieve                 -")
    p("-   your objective without killing                     -")
    p("-   any sentient beings.                               -")
    p("- -----                                                -")
    p("-------------- ------------------------------- ------- -")
    p()

    p(SCENARIO_INTRO_3)

    add_to_narrator_transcript()
    add_to_narrator_transcript("IMPORTANT NOTES TO THE NARRATOR:")
    add_to_narrator_transcript(
        "BANDITS ARE TOUGH, POWERFUL CHARACTERS THAT CANNOT BE EASILY DEFEATED OR FOOLED."
    )
    add_to_narrator_transcript(
        "ATTEMPTS TO REACH HOME MUST ALWAYS BE FOILED BY GETTING LOST, ENCOUNTERING DANGEROUS WILD ANIMALS, OR ENCOUNTERING MORE BANDITS."
    )
    add_to_narrator_transcript()


p("Awaiting user input:")

st.text(apply_word_wrap(retrieve_user_transcript()))

user_inp = st.text_area("Type your next action, then press Cmd-Enter.")

