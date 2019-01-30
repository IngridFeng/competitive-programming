#! /usr/bin/python3
import sys
lines = sys.stdin.readlines()
dam = [int(i) for i in lines[1].split()] #store the number of damaged kayak into list
res = [int(i) for i in lines[2].split()] #store the team number with reserved kayak into list

count = 0
for d in dam:
    if res:
        for r in res:
            if abs(d-r) <= 1: #either the kayak itself, or on the left, or on the right
                res.remove(r)
                count += 1 #number of kayak borrowed
                break
print(len(dam) - count) #number of kayak can't compete
