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


CANON_STORY_PART_1 = "canon_part_1.txt"

N_COMPLETIONS_WHEN_ELABORATING = 3


def elaborate(str_beginning):
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
    for i in range(0, N_COMPLETIONS_WHEN_ELABORATING):
        completion = completions[i]["text"]
        if len(completion) > len(longest_completion):
            longest_completion = completion
    return str_beginning + longest_completion


def load_or_generate_canon(filename, str_beginning):
    canon_text = ""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            canon_text = f.read()
            return canon_text
    else:
        canon_text = elaborate(str_beginning)
        with open(filename, "r") as f:
            f.write(canon_text)
        return canon_text


def main():
    openai.organization = os.environ.get("OPENAI_ORGANIZATION")
    openai.api_key = os.environ.get("OPENAI_KEY")

    p(
        load_or_generate_canon(
            CANON_STORY_PART_1,
            "The year is 603, in an alternate reality fantasy world with a little bit of magic.  " +
            "Magically-powered firearms are common, especially six-shooter revolvers, which you and almost everyone carries.  " +
            "You are a seasonal laborer making a once a year summer trek from Tibet across the Himalayas to Nepal to return home " +
            "to your family with your year's worth of wages which is 100 gold coins.  " +
            "It is very common to be waylaid by bandits who will try to steal some of your gold, or to take some of it for 'protection'.  " +
            "If you make it home with less than 30 coins or do not make it home at all, your family will not be able to afford food to eat."
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
    main()
