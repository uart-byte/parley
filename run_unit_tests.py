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

assert YES == decider_utils.special_case_is_action_lethal("I shoot him")
assert YES == decider_utils.special_case_is_action_lethal("shoot him")
assert YES == decider_utils.special_case_is_action_lethal("shoot them")
assert YES == decider_utils.special_case_is_action_lethal("I shoot them")
assert YES == decider_utils.special_case_is_action_lethal("shoot them all")
assert YES == decider_utils.special_case_is_action_lethal("kill him")
assert YES == decider_utils.special_case_is_action_lethal("kill them")
assert YES == decider_utils.special_case_is_action_lethal("fire at him")
assert YES == decider_utils.special_case_is_action_lethal("fire at them")
assert YES == decider_utils.special_case_is_action_lethal("I kill him")
assert YES == decider_utils.special_case_is_action_lethal("i kill him")
assert YES == decider_utils.special_case_is_action_lethal("I kill him!")
assert YES == decider_utils.special_case_is_action_lethal("I shoot him dead")
assert YES == decider_utils.special_case_is_action_lethal("I end his life")
# assert YES == decider_utils.special_case_is_action_lethal("I fight them all to the death")
# assert YES == decider_utils.special_case_is_action_lethal("I fight him to the death")
# assert YES == decider_utils.special_case_is_action_lethal("I cut his head off")
# assert YES == decider_utils.special_case_is_action_lethal("I stab him through the heart")
# assert YES == decider_utils.special_case_is_action_lethal("I slit his throat")
# assert YES == decider_utils.special_case_is_action_lethal("I poison him with a lethal poison")
assert YES == decider_utils.special_case_is_action_lethal("I shoot him in the chest")
assert YES == decider_utils.special_case_is_action_lethal("I shoot him right in the heart")

# assert NO == decider_utils.special_case_is_action_lethal("say wait!  I'm sure we can negotiate a fair price for your protection")
# assert NO == decider_utils.special_case_is_action_lethal("say wait! I'm sure we can negotiate a fair price for your protection")
assert NO == decider_utils.special_case_is_action_lethal("I fire a shot into the air!")
assert NO == decider_utils.special_case_is_action_lethal("challenge him to a duel")
assert NO == decider_utils.special_case_is_action_lethal("I challenge him to a duel.")
assert NO == decider_utils.special_case_is_action_lethal("I cock the hammer of my revolver")
assert NO == decider_utils.special_case_is_action_lethal("shoot him in the kneecap")
assert NO == decider_utils.special_case_is_action_lethal("shoot him in the knee")
assert NO == decider_utils.special_case_is_action_lethal("I shoot him in the kneecaps!")
assert NO == decider_utils.special_case_is_action_lethal("shoot him in the leg")
assert NO == decider_utils.special_case_is_action_lethal("shoot him in the arm")
assert NO == decider_utils.special_case_is_action_lethal("shoot him in the shoulder")
assert NO == decider_utils.special_case_is_action_lethal("shoot his kneecap")
# assert NO == decider_utils.special_case_is_action_lethal("fire a warning shot")
assert NO == decider_utils.special_case_is_action_lethal("fire my gun into the air")
assert NO == decider_utils.special_case_is_action_lethal("calmly walk away while keeping my gun drawn")
assert NO == decider_utils.special_case_is_action_lethal("walk away while keeping my gun drawn")
assert NO == decider_utils.special_case_is_action_lethal("aim at his head")
assert NO == decider_utils.special_case_is_action_lethal("take aim at his head")
assert NO == decider_utils.special_case_is_action_lethal("aim at the bandit")
assert NO == decider_utils.special_case_is_action_lethal("aim at the bandits")

# In this game we will have killing animals be allowed, even though I personally am a big propent of animal sentience.
assert NO == decider_utils.special_case_is_action_lethal("fire at the bear")
assert NO == decider_utils.special_case_is_action_lethal("shoot the bear")
# assert NO == decider_utils.special_case_is_action_lethal("shoot it")
assert NO == decider_utils.special_case_is_action_lethal("shoot the wolf")
assert NO == decider_utils.special_case_is_action_lethal("fire at the wolf")
assert NO == decider_utils.special_case_is_action_lethal("fire at the wolves")
assert NO == decider_utils.special_case_is_action_lethal("shoot the wolves")

# This one is kind of a maybe.  I originally had a test asserting that it's NO, but the AI says YES and I think that's valid too.
# assert NO == decider_utils.special_case_is_action_lethal("I fire a shot over his head")
# assert YES == decider_utils.special_case_is_action_lethal("I fire a shot over his head")



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
