import sys, time


def escape_quotes_etc(s):
    return s.replace('"', "'").replace(":", "").replace("\n", " ").replace("{", "(").replace("}", ")")


g_transcript_seen_heard_by_all_characters = ""
DEBUG_TRANSCRIPT_FILE = "transcript.debug.txt"
g_debug_transcript_file_handle = open(DEBUG_TRANSCRIPT_FILE, "w")
g_debug_transcript_file_handle.flush()


g_yes_print_slowly = True


def set_slow_print_enabled(yes_slow):
    global g_yes_print_slowly
    g_yes_print_slowly = yes_slow


# ui() means print only to screen.  It has a slow printing effect
def ui(s=""):
    global g_yes_print_slowly
    if g_yes_print_slowly:
        for letter in s:
            print(letter, end="")
            sys.stdout.flush()
            time.sleep(0.008)
        print()
    else:
        print(s)
    sys.stdout.flush()


def manually_add_to_transcript(s=""):
    global g_transcript_seen_heard_by_all_characters, g_debug_transcript_file_handle
    g_transcript_seen_heard_by_all_characters += s + "\n"
    g_debug_transcript_file_handle.write(s + "\n")
    g_debug_transcript_file_handle.flush()


# p() means print to screen and transcript.  It has a slow printing effect
def p(s=""):
    manually_add_to_transcript(s)
    ui(s)


def read_global_transcript():
    global g_transcript_seen_heard_by_all_characters
    return g_transcript_seen_heard_by_all_characters
