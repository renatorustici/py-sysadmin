######################################################
#
# This script receives a specialy formatted file
# called paths by default containing information 
# retrieved from multipath -ll command and outputs a
# CSV file containing LUN information.
#
# Author: Renato Montenegro Rustici
# September 2020
#
######################################################

import sys, os, re

source = open('paths-completao.txt', 'r')

diskAlias = ""
diskID = ""
diskSize = ""
diskLUN = ""

processedLines = 0

print("Generating multipath info...\n")

for line in source:
    if re.search("^size", line):
        column = line.split(' ')
        diskSize = column[0].split('=')[1]
        diskSize = diskSize.replace(".0", "")
        diskSize = diskSize.replace("G", "")
    elif re.search("\(", line):
        if processedLines > 0:
            print(f"{diskAlias},{diskID},{diskLUN},{diskSize}")
            diskAlias = ""
            diskID = ""
            diskSize = ""
            diskLUN = ""
            column = line.split(' ')
            diskAlias = column[0]
            diskID = column[1].replace("(", "")
            diskID = diskID.replace(")", "")
        else:
            column = line.split(' ')
            diskAlias = column[0]
            diskID = column[1]
            diskID = column[1].replace("(", "")
            diskID = diskID.replace(")", "")
    elif re.search("^\| \`-", line):
        column = line.split(' ')[2]
        column = column.split(':')
        diskLUN = column[3]

    processedLines += 1

print(f"{diskAlias},{diskID},{diskLUN},{diskSize}")
print (f"\n{processedLines} lines where processed.\n")

source.close()
