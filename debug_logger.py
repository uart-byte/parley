DEBUG_FILENAME = "debug_log.txt"
debug_file = f.open(DEBUG_FILENAME, "w+")  # We let the file get implicitly closed when python exits

def debug_print(s):
  debug_file.write(s + "\n")
  debug_file.flush()
