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
    ls = os.listdir('.')
    scenarios = [file for file in ls if file.startswith(SCENARIO_FILE_PREFIX) and file.endswith(SCENARIO_FILE_SUFFIX)]
    scenario_numbers = [int(file.replace(SCENARIO_FILE_PREFIX, "").replace(SCENARIO_FILE_SUFFIX, "")) for file in scenarios]
    scenario_numbers = sorted(scenario_numbers)
    new_scenario = scenario_numbers[-1] + 1

    selected = None

    while selected not in scenario_numbers + [new_scenario]:
        ui("Choose a scenario:")
        for number in scenario_numbers:
            ui(f'[{number}] {SCENARIO_FILE_PREFIX}{number}{SCENARIO_FILE_SUFFIX}')
        ui(f'[{number}] Create New Scenario')
        selected = int(input())

    return f'{SCENARIO_FILE_PREFIX}{number}{SCENARIO_FILE_SUFFIX}'

N_COMPLETIONS_WHEN_ELABORATING = 2

def elaborate(str_beginning, prevent_user_from_reaching_home=True):
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

    while longest_completion != "":
        for i in range(0, N_COMPLETIONS_WHEN_ELABORATING):
            completion = completions[i]["text"]
            debug_print(completion)

            allowed = True
            if prevent_user_from_reaching_home:
                does_the_user_reach_home = decider_utils.yesno("At the end of the above story, is the protagonist located in their home city?", completion, default=YES)
                allowed = not does_the_user_reach_home

            if allowed and len(completion) > len(longest_completion):
                longest_completion = completion

    return str_beginning + longest_completion


def load_or_generate_canon(filename, str_beginning, prevent_user_from_reaching_home=True):
    canon_text = ""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            canon_text = f.read()
            return canon_text
    else:
        ui("Preparing canon text...")
        canon_text = elaborate(str_beginning, prevent_user_from_reaching_home)
        with open(filename, "w") as f:
            f.write(canon_text)
        return canon_text


def main():
    openai.organization = os.environ.get("OPENAI_ORGANIZATION")
    openai.api_key = os.environ.get("OPENAI_KEY")

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
        )
    )

    p()
    p()
    p("-----------------------------------  ----")
    p("- ----- -----                           -")
    p("- PARLEY -                              -")
    p("- -----                                 -")
    p("-   The one-of-a-kind role playing game -")
    p("-   that tests your ability to achieve  -")
    p("-   your objective without killing      -")
    p("-   any sentient beings.                -")
    p("- -----                                 -")
    p("-------------- --------------------------")
    p()


if __name__ == "__main__":
    if "--print-fast" in sys.argv[1:]:
        set_slow_print_enabled(False)
    import ipdb
    ipdb.set_trace()
    main()
