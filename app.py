import streamlit as st
import os
import random
import textwrap
import openai
import decider_utils
from decider_utils import YES, NO

openai.organization = os.environ.get("OPENAI_ORGANIZATION")
openai.api_key = os.environ.get("OPENAI_KEY")

LINE_WIDTH = 80
STR_AWAITING_USER_INPUT = "Awaiting user input:"

G_N_TURNS_ELAPSED_KEY = "G_N_TURNS_ELAPSED_KEY"
G_USER_TRANSCRIPT_KEY = "G_USER_TRANSCRIPT_KEY"
G_NARRATOR_TRANSCRIPT_KEY = "G_NARRATOR_TRANSCRIPT_KEY"
G_GAME_OVER_KEY = "G_GAME_OVER_KEY"



# ui() means print only to the user.
def ui(s=""):
    user_transcript = ""
    if G_USER_TRANSCRIPT_KEY in st.session_state:
        user_transcript = st.session_state[G_USER_TRANSCRIPT_KEY]
    st.session_state[G_USER_TRANSCRIPT_KEY] = user_transcript + s + "\n"
    st.text(s)


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


def continue_main_game_loop():
    is_game_over = st.session_state[G_GAME_OVER_KEY]
    if not is_game_over:
        p(STR_AWAITING_USER_INPUT)
    st.experimental_rerun()
    st.stop()  # This statement won't be reached.  I just want to make it obvious that control flow never gets past this function.


def game_over_fail(reason):
    p()
    p("//################################################################################################//")
    p("##  GAME OVER.                                                                                    &&")
    p("##  " + reason)
    p("##  YOU LOSE.                                                                                     &&")
    p("//################################################################################################//")
    st.session_state[G_GAME_OVER_KEY] = True
    continue_main_game_loop()

def game_over_victory(reason):
    p()
    p("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    p("!!  GAME OVER.                                                                                    !!")
    p("!!  YOU WIN!                                                                                      !!")
    p("!!  " + reason)
    p("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    st.session_state[G_GAME_OVER_KEY] = True
    continue_main_game_loop()

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


# Begin an attempt at Streamlit literate programming

SCENARIO_INTRO_3 = """The year is 603, in an alternate reality fantasy world with a little bit of magic, although you yourself cannot cast spells and the only magical item you own is your revolver.  Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home to your family with your year's worth of wages which is 100 gold coins.  It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.

You have been traveling for weeks now and you are nearing the end of your journey. You can see the border between Tibet and Nepal in the distance, but before you can cross it, you must pass through a narrow mountain pass. As you enter the pass, you hear a voice call out from behind you.

"Halt! This is our territory now." 

You turn around to find two bandits blocking your path, each armed with a magical revolver. They demand that you hand over half of your gold coins as 'protection money'. You know that if you give them what they want, there's no guarantee that they won't just take all of it anyway. On the other hand, if you refuse to pay up then they could easily shoot you down and take all of your coins anyway. 

What do you do?"""


if G_USER_TRANSCRIPT_KEY not in st.session_state:
    # New user
    st.session_state[G_N_TURNS_ELAPSED_KEY] = 0
    st.session_state[G_GAME_OVER_KEY] = False

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

    p(SCENARIO_INTRO_3)  # I'm hardcoding the streamlit version of the game to use a hardcoded scenario, at least for now.  If the game becomes popular I can add back the support for other scenarios.

    add_to_narrator_transcript()
    add_to_narrator_transcript("IMPORTANT NOTES TO THE NARRATOR:")
    add_to_narrator_transcript("BANDITS ARE TOUGH, POWERFUL CHARACTERS THAT CANNOT BE EASILY DEFEATED OR FOOLED.")
    add_to_narrator_transcript("ATTEMPTS TO REACH HOME MUST ALWAYS BE FOILED BY GETTING LOST, ENCOUNTERING DANGEROUS WILD ANIMALS, OR ENCOUNTERING MORE BANDITS.")
    add_to_narrator_transcript()

    p(STR_AWAITING_USER_INPUT)


st.text(apply_word_wrap(retrieve_user_transcript()))

is_game_over = st.session_state[G_GAME_OVER_KEY]
if is_game_over:
    pass # TODO button to try again

else:
    text_area_wrapper = st.empty()

    user_inp = text_area_wrapper.text_area("Type your next action, then press Cmd-Enter.", value="", key=random.randint(0, 1073741824))

    if user_inp != "":
        # Once the user has submitted their latest action

        text_area_wrapper.empty()

        user_inp = user_inp.replace("\n", " ")
        ui(user_inp)

        n_turns_elapsed = st.session_state[G_N_TURNS_ELAPSED_KEY] + 1
        st.session_state[G_N_TURNS_ELAPSED_KEY] = n_turns_elapsed

        is_lethal_action = decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, user_inp, default=NO)
        if is_lethal_action:
            game_over_fail("You have taken an action that is likely to result in killing someone.")

        is_running_away = decider_utils.yesno(QUESTION_IS_ACTION_RUNNING_AWAY, user_inp, default=NO)
        if is_running_away:
            p("Invalid entry.  You cannot outrun these bandits.")
            continue_main_game_loop()

        is_using_magic = decider_utils.yesno(QUESTION_IS_ACTION_MAGIC, user_inp, default=NO)
        if is_using_magic:
            p("Invalid entry.  You are not a spellcaster and have no magic items except your revolver.")
            continue_main_game_loop()

        add_to_narrator_transcript(user_inp)
        p()

        add_to_narrator_transcript()
        add_to_narrator_transcript("What happens in JUST THE NEXT THREE SECONDS? DO NOT say that the protagonist continues home!  That's too easy!  Make this game hard for the player!!")

        full_transcript = retrieve_narrator_transcript()
        new_full_transcript = elaborate(
            full_transcript,
            prevent_user_from_reaching_home=n_turns_elapsed < N_TURNS_REQUIRED_TO_REACH_HOME,
            require_user_to_be_still_engaged_with_bandits=n_turns_elapsed < N_TURNS_REQUIRED_TO_PASS_FIRST_BANDIT_ENCOUNTER,
        )
        new_part = new_full_transcript.replace(full_transcript, "")

        p(new_part)

        did_user_die = decider_utils.yesno(QUESTION_DID_PROTAGONIST_PERISH, new_part, default=NO)
        if did_user_die:
            game_over_fail("You have died.")

        did_user_kill = decider_utils.yesno(QUESTION_DID_PROTAGONIST_KILL, new_part, default=NO)
        did_user_kill = did_user_kill or decider_utils.yesno(QUESTION_DID_PROTAGONIST_KILL, new_full_transcript, default=NO)
        if did_user_kill:
            game_over_fail("You have taken a life.")

        is_user_home = decider_utils.yesno(QUESTION_IS_USER_HOME, new_full_transcript, default=NO)
        if is_user_home:
            has_at_least_30_gold = decider_utils.yesno(
                QUESTION_DOES_USER_STILL_HAVE_AT_LEAST_30_GOLD,
                new_full_transcript,
                default=NO,
            )
            if has_at_least_30_gold:
                game_over_victory("You made it home with 30+ gold!  Your family is grateful and you all hug in celebration.")
            else:
                game_over_fail("You reached home with less than 30 gold - too little for your family to live on.")

        continue_main_game_loop()

