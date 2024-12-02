#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

import json

afileData = open('task01a.txt','r').read()
alist = json.loads(afileData)
print(f"task01a: {max(alist)}")

bfileData = open('task01b.txt','r').read()
blist = json.loads(bfileData)
print(f"task01b: {max(blist)}")

cfileData = open('task01c.txt','r').read()
clist = json.loads(cfileData)
print(f"task01c: {max(clist)}")