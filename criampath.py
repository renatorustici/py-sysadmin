######################################################
#
# This script receives a specialy formatted file
# called luns.csv by default containing information 
# retrieved from multipath -ll command and outputs a
# multipath.conf file.
#
# Author: Renato Montenegro Rustici
# September 2020
#
######################################################

import sys, os

source = open('luns.csv', 'r')
output = open('multipath.conf', 'w')

processedLines = 0

print("Generating multipath.conf...")

output.write("multipaths {\n")

for line in source:
    column = line.split(',')

    # Column order:
    # [0] Disk Alias
    # [1] Disk ID
    # [2] LUN ID - just for comments
    # [3] Disk Size - just for comments

    output.write("    multipath {\n")
    output.write(f"        wwid {column[1]}\n")
    output.write(f"        alias {column[0]}\n")
    output.write(f"        # lun id {column[2]}\n")
    diskSize = column[3].replace("\n", "")
    output.write(f"        # original disk size {diskSize}GB\n")
    output.write("    }\n")

    processedLines += 1

output.write("}\n")

print (f"{processedLines} lines where processed.")

output.close()
source.close()
