import openai
from debug_logger import debug_print

YES = True
NO = False


def yesno(question, text, default):
    prompt = text + "\n\n" + question
    hopefully_word_yes_or_no = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=20,  # At first I tried max_tokens = 1 or 2,  but the davinci-002 model produced zero output (immediate stop) unless I increased max_token to around 20
        frequency_penalty=0,
        presence_penalty=0,
        n=1,
    )["choices"][0]["text"]

    hopefully_word_yes_or_no = hopefully_word_yes_or_no.upper().strip()
    debug_print(hopefully_word_yes_or_no)

    result = default

    if default == YES:
        if hopefully_word_yes_or_no.startswith("N"):
            result = NO

    if default == NO:
        if hopefully_word_yes_or_no.startswith("Y"):
            result = YES

    debug_print(f"Returning {result}")
    return result
