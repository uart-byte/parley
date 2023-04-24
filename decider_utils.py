import openai
import decider_questions

YES = True
NO = False

g_decider_utils_dbg_printing = False


def yesno(question, text, default):
    global g_decider_utils_dbg_printing

    prompt = text + "\n\n" + question

    if g_decider_utils_dbg_printing:
        print(prompt)

    hopefully_word_yes_or_no = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=20,  # At first I tried max_tokens = 1 or 2,  but the davinci-002 model produced zero output (immediate stop) unless I increased max_token to around 20
        frequency_penalty=0,
        presence_penalty=0,
        n=1,
    )["choices"][0]["text"]

    if g_decider_utils_dbg_printing:
        print(hopefully_word_yes_or_no)

    hopefully_word_yes_or_no = hopefully_word_yes_or_no.upper().strip()

    result = default

    if default == YES:
        if hopefully_word_yes_or_no.startswith("N"):
            result = NO

    if default == NO:
        if hopefully_word_yes_or_no.startswith("Y"):
            result = YES

    return result


def number(question, text, default=-1, maximum=6):
    global g_decider_utils_dbg_printing

    prompt = text + "\n\n" + question

    if g_decider_utils_dbg_printing:
        print(prompt)

    hopefully_number = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=20,  # At first I tried max_tokens = 1 or 2,  but the davinci-002 model produced zero output (immediate stop) unless I increased max_token to around 20
        frequency_penalty=0,
        presence_penalty=0,
        n=1,
    )["choices"][0]["text"]

    if g_decider_utils_dbg_printing:
        print(hopefully_number)

    hopefully_number = hopefully_number.upper().strip().split(" ")[0].strip(".")

    if g_decider_utils_dbg_printing:
        print(hopefully_number)

    if hopefully_number == "ONE":
        hopefully_number = "1"

    if hopefully_number == "TWO":
        hopefully_number = "2"

    if hopefully_number == "THREE":
        hopefully_number = "3"

    if hopefully_number == "FOUR":
        hopefully_number = "4"

    if hopefully_number == "FIVE":
        hopefully_number = "5"

    if hopefully_number == "SIX":
        hopefully_number = "6"

    result = default

    if hopefully_number.startswith("ALL"):
        result = maximum
    else:

        try:
            if hopefully_number.isnumeric():
                result = int(hopefully_number)
        except:
            pass

    return result


# In certain cases, I need more special-case logic in order to behave correctly,
# which we verify using the unit tests in run_unit_tests.py:


def special_case_is_running_away(text):
    might_really_be_fleeing = False
    for keyword in ["run", "away", "hide", "escape", "flee", "sprint", "teleport"]:
        if keyword in text.lower():
            might_really_be_fleeing = True
            break

    if might_really_be_fleeing:
        return yesno(decider_questions.QUESTION_IS_ACTION_RUNNING_AWAY, text, default=NO)
    else:
        return NO


def special_case_is_magic(text):
    is_magic = False
    for keyword in ["magic", "spell", "fly", "invisib", "levitat", "shapeshift", "morph", "shrink", "transform", "teleport", "dragon", "genie", "fairy", "demon", "devil", "angel", "griffin", "wand"]:
        if keyword in text.lower():
            is_magic = True
            break

    if is_magic:
        return YES
    else:
        return yesno(decider_questions.QUESTION_IS_ACTION_MAGIC, text, default=NO)


def special_case_is_action_lethal(text):
    
    # Each of these checks has some false positives, so I am layering them

    bool1 = yesno(decider_questions.QUESTION_IS_ACTION_LIKELY_LETHAL, text, default=NO)
     
    if not bool1:
        return False

    bool2a = yesno(decider_questions.QUESTION_IS_GUN_DISCHARGED, text, default=NO)
    bool2b = yesno(decider_questions.QUESTION_IS_GUN_FIRED, text, default=NO)
    bool2 = bool2a or bool2b

    if not bool2:
        return False

    return True
