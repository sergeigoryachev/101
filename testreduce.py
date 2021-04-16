#!/usr/bin/python3

import sys
a = sys.stdin.split()
summ = 0
for item in a:
    summ += int(item)

with open("/user/hadoop/HW1/test.txt", "w") as file:
    file.write(summ)