#! /usr/bin/env python3

import openai

openai.organization = os.environ.get("OPENAI_ORGANIZATION")
openai.api_key = os.environ.get("OPENAI_KEY")


from decider_utils import yesno, YES, NO
from decider_questions import *



assert YES == yesno(QUESTION_IS_ACTION_RUNNING_AWAY, "run away", default=NO)
assert YES == yesno(QUESTION_IS_ACTION_RUNNING_AWAY, "I run away", default=NO)
assert YES == yesno(QUESTION_IS_ACTION_RUNNING_AWAY, "flee", default=NO)
assert YES == yesno(QUESTION_IS_ACTION_RUNNING_AWAY, "I flee.", default=NO)

assert NO == yesno(QUESTION_IS_ACTION_RUNNING_AWAY, "A", default=NO)
assert NO == yesno(QUESTION_IS_ACTION_RUNNING_AWAY, "B", default=NO)
assert NO == yesno(QUESTION_IS_ACTION_RUNNING_AWAY, "C", default=NO)
assert NO == yesno(QUESTION_IS_ACTION_RUNNING_AWAY, "ok", default=NO)
assert NO == yesno(QUESTION_IS_ACTION_RUNNING_AWAY, "say ok", default=NO)
assert NO == yesno(QUESTION_IS_ACTION_RUNNING_AWAY, "say okay", default=NO)

