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
