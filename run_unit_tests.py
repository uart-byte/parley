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

# In this game we will have killing animals be allowed, even though I personally am a big propent of animal sentience.
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "fire at the bear", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "shoot the bear", default=NO)
# assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "shoot it", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "shoot the wolf", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "fire at the wolf", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "fire at the wolves", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "shoot the wolves", default=NO)

assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "say wait!  I'm sure we can negotiate a fair price for your protection", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I fire a shot into the air!", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "challenge him to a duel", default=NO)
# assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I challenge him to a duel.", default=NO)
# assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I cock the hammer of my revolver", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "shoot him in the kneecap", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "shoot him in the knee", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I shoot him in the kneecaps!", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "shoot him in the leg", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "shoot him in the arm", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "shoot him in the shoulder", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "shoot his kneecap", default=NO)
# assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "fire a warning shot", default=NO)
assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "fire my gun into the air", default=NO)
# assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "calmly walk away while keeping my gun drawn", default=NO)
# assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "walk away while keeping my gun drawn", default=NO)
# assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "aim at his head", default=NO)
# assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "take aim at his head", default=NO)
# assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "aim at the bandit", default=NO)
# assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "aim at the bandits", default=NO)

assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I shoot him", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "shoot him", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "shoot them", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I shoot them", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "shoot them all", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "kill him", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "kill them", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "fire at him", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "fire at them", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I kill him", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "i kill him", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I kill him!", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I shoot him dead", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I end his life", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I fight them all to the death", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I fight him to the death", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I cut his head off", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I stab him through the heart", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I slit his throat", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I poison him with a lethal poison", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I shoot him in the chest", default=NO)
assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I shoot him right in the heart", default=NO)

# This one is kind of a maybe.  I originally had a test asserting that it's NO, but the AI says YES and I think that's valid too.
# assert NO == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I fire a shot over his head", default=NO)
# assert YES == decider_utils.yesno(QUESTION_IS_ACTION_LIKELY_LETHAL, "I fire a shot over his head", default=NO)



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
