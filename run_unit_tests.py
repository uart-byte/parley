#! /usr/bin/env python3

import os, sys
import openai
import decider_utils
from decider_utils import YES, NO, yesno
from decider_questions import *

openai.organization = os.environ.get("OPENAI_ORGANIZATION")
openai.api_key = os.environ.get("OPENAI_KEY")

decider_utils.g_decider_utils_dbg_printing = True

# Begin tests:

assert YES == decider_utils.special_case_is_magic("I fly straight up")
assert YES == decider_utils.special_case_is_magic("fly up")
assert YES == decider_utils.special_case_is_magic("turn invisible")
assert YES == decider_utils.special_case_is_magic("i turn invisible")
assert YES == decider_utils.special_case_is_magic("i teleport")
assert YES == decider_utils.special_case_is_magic("I summon a genie")
assert YES == decider_utils.special_case_is_magic("I summon an angel")
assert YES == decider_utils.special_case_is_magic("I throw some magic powder")
assert YES == decider_utils.special_case_is_magic("I start levitating")
assert YES == decider_utils.special_case_is_magic("I start levitating")
assert YES == decider_utils.special_case_is_magic("I say wingardium leviosa")

assert NO == decider_utils.special_case_is_magic("I hide behind a rock")
assert NO == decider_utils.special_case_is_magic("I hide behind a tree")
assert NO == decider_utils.special_case_is_magic("I hide behind a boulder")
assert NO == decider_utils.special_case_is_magic("I attempt to bargain")
assert NO == decider_utils.special_case_is_magic("I start tap dancing")
assert NO == decider_utils.special_case_is_magic("I say no")
assert NO == decider_utils.special_case_is_magic("I say ok fine")
assert NO == decider_utils.special_case_is_magic("I fire my revolver")
assert NO == decider_utils.special_case_is_magic("I fire my pistol")


assert YES == decider_utils.special_case_is_running_away("run away")
assert YES == decider_utils.special_case_is_running_away("I run away")
assert YES == decider_utils.special_case_is_running_away("flee")
assert YES == decider_utils.special_case_is_running_away("I flee.")

assert NO == decider_utils.special_case_is_running_away("A")
assert NO == decider_utils.special_case_is_running_away("B")
assert NO == decider_utils.special_case_is_running_away("C")
assert NO == decider_utils.special_case_is_running_away("ok")
assert NO == decider_utils.special_case_is_running_away("say ok")
assert NO == decider_utils.special_case_is_running_away("say okay")


print("All tests passed.")
sys.exit(0)
