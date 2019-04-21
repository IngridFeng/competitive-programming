#! /usr/bin/python3
import sys
lines = sys.stdin.readlines()
#store all the variables got from input
num_p = int(lines[0])
ps = [int(i) for i in lines[1].split()]
num_o = int(lines[2])
os = [int(i) for i in lines[3].split()]
#make a table for all the possible combination of prices to facilitate dynamic programming
table = [-2] * 31000
table[0] = 0
for i in range(len(ps)):
    p = ps[i]
    for j in range(0, 30001):
        if table[j] == -1:
            table[j+p] = -1
        elif table[j] >= 0:
            if table[j+p] == -2:
                table[j+p] = i
            else:
                table[j+p] = -1
#loop through each order and check the result
for o in os:
    sol = []
    if table[o] == -1:
        print("Ambiguous")
    elif table[o] == -2:
        print("Impossible")
    else:
        while o > 0:
            sol.append(table[o] + 1)
            o -= ps[table[o]]
        if o < 0:
            print("Ambiguous")
        else:
            for s in sorted(sol):
                print(s, end=' ')
            print('')
