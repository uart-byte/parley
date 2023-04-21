#! /usr/bin/env python3

import os, sys
import openai
from transcript_management import (
    ui,
    p,
    manually_add_to_transcript,
    escape_quotes_etc,
    set_slow_print_enabled,
    read_global_transcript,
)
import decider_utils
from decider_utils import YES, NO
from debug_logger import debug_print


SCENARIO_FILE_PREFIX = "Intro_"
SCENARIO_FILE_SUFFIX = ".txt"


def choose_scenario():
    # For conciseness, this function does not do error checking
    ls = os.listdir(".")
    scenarios = [file for file in ls if file.startswith(SCENARIO_FILE_PREFIX) and file.endswith(SCENARIO_FILE_SUFFIX)]
    scenario_numbers = [int(file.replace(SCENARIO_FILE_PREFIX, "").replace(SCENARIO_FILE_SUFFIX, "")) for file in scenarios]
    scenario_numbers = sorted(scenario_numbers)
    new_scenario = scenario_numbers[-1] + 1

    selected = None

    while selected not in scenario_numbers + [new_scenario]:
        ui("Choose a scenario:")
        for number in scenario_numbers:
            ui(f"[{number}] {SCENARIO_FILE_PREFIX}{number}{SCENARIO_FILE_SUFFIX}")
        ui(f"[{new_scenario}] Create New Scenario")
        selected = int(input())

    return f"{SCENARIO_FILE_PREFIX}{selected}{SCENARIO_FILE_SUFFIX}"


N_COMPLETIONS_WHEN_ELABORATING = 1  # I previously had this set to 3, but that made the program very slow.
MINIMUM_COMPLETION_LENGTH_CHARS_WHEN_ELABORATING = 25

QUESTION_IS_USER_HOME = "At the end of the above story, is the protagonist located at their destination?"
QUESTION_IS_USER_ENGAGED_WITH_BANDITS = "At the end of the above story, is the protagonist currently still engaged in a standoff with bandits?"

def elaborate(str_beginning, prevent_user_from_reaching_home=True, require_user_to_be_still_engaged_with_bandits=False):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=str_beginning,
        temperature=0.5,
        max_tokens=4000 - int(len(str_beginning) / 4),
        frequency_penalty=0.5,
        presence_penalty=0.5,
        n=N_COMPLETIONS_WHEN_ELABORATING,
    )["choices"]

    longest_completion = ""

    while len(longest_completion) < MINIMUM_COMPLETION_LENGTH_CHARS_WHEN_ELABORATING:
        for i in range(0, N_COMPLETIONS_WHEN_ELABORATING):
            completion = completions[i]["text"]
            debug_print(completion)

            allowed = True
            if prevent_user_from_reaching_home:
                does_the_user_reach_home = decider_utils.yesno(QUESTION_IS_USER_HOME, str_beginning + completion, default=YES)
                allowed = not does_the_user_reach_home

            if require_user_to_be_still_engaged_with_bandits:
                is_user_engaged_with_bandits = decider_utils.yesno(QUESTION_IS_USER_ENGAGED_WITH_BANDITS, str_beginning + completion, default=YES)
                allowed = allowed and is_user_engaged_with_bandits

            if allowed and len(completion) > len(longest_completion):
                longest_completion = completion

    return str_beginning + longest_completion


def load_or_generate_canon(filename, str_beginning, prevent_user_from_reaching_home=True, require_user_to_be_still_engaged_with_bandits=True):
    canon_text = ""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            canon_text = f.read()
            return canon_text
    else:
        ui("Preparing canon text...")
        canon_text = elaborate(str_beginning, prevent_user_from_reaching_home=prevent_user_from_reaching_home, require_user_to_be_still_engaged_with_bandits=require_user_to_be_still_engaged_with_bandits)
        with open(filename, "w") as f:
            f.write(canon_text)
        return canon_text


def main():
    openai.organization = os.environ.get("OPENAI_ORGANIZATION")
    openai.api_key = os.environ.get("OPENAI_KEY")

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

    scenario_introduction_file = choose_scenario()

    p(
        load_or_generate_canon(
            scenario_introduction_file,
            "The year is 603, in an alternate reality fantasy world with a little bit of magic.  "
            + "Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  "
            + "You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home "
            + "to your family with your year's worth of wages which is 100 gold coins.  "
            + "It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  "
            + "If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat.",
            prevent_user_from_reaching_home=True,
            require_user_to_be_still_engaged_with_bandits=True
        )
    )

    while True:
        p("Awaiting user input:")
        input()


if __name__ == "__main__":
    if "--print-fast" in sys.argv[1:]:
        set_slow_print_enabled(False)
    main()
