DEBUG_FILENAME = "debug_log.txt"
debug_file = open(DEBUG_FILENAME, "a")  # We let the file get implicitly closed when python exits

def debug_print(s):
  debug_file.write(s + "\n")
  print(s)
