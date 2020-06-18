"""
    This script executes an arbitrary command line using
    information from an external file. It can be used
    in a variaty of situations with small modifications.

    Author: Renato Montenegro Rustici
"""
import sys
import subprocess

try:
    source_file = open("source.txt", mode="rt", encoding="utf-8")
except OSError as systemError:
    print(f"Error opening source.txt: {systemError}")
    sys.exit(1)

lines = source_file.readlines()
source_file.close()

for line in lines:
    line = line.replace("\n", "")
    print(f"Dealing with {line}: ", end = "")
    ret_code = subprocess.run(["ls", "-l", line], stdout=subprocess.DEVNULL)
    
    if ret_code.returncode == 0:
        print("\x1b[1;32m" + "done!" + "\x1b[0m" + "\n")
    else:
        print("\x1b[1;31m" + "error!" + "\x1b[0m" + "\n")
        