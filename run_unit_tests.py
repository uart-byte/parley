#! /usr/bin/env python3

import os
import openai

openai.organization = os.environ.get("OPENAI_ORGANIZATION")
openai.api_key = os.environ.get("OPENAI_KEY")


from decider_utils import YES, NO, yesno, special_case_is_running_away
from decider_questions import *



assert YES == special_case_is_running_away("run away")
assert YES == special_case_is_running_away("I run away")
assert YES == special_case_is_running_away("flee")
assert YES == special_case_is_running_away("I flee.")

assert NO == special_case_is_running_away("A")
assert NO == special_case_is_running_away("B")
assert NO == special_case_is_running_away("C")
assert NO == special_case_is_running_away("ok")
assert NO == special_case_is_running_away("say ok")
assert NO == special_case_is_running_away("say okay")

