DEBUG_FILENAME = "debug_log.txt"


def debug_print(s=""):
    with open(DEBUG_FILENAME, "a") as f:
        f.write(s + "\n")
