#! /usr/bin/python3
import sys
lines = sys.stdin.readlines()
for line in lines:
    l = line.split()
    try:
        num = int(l[0]) #if success, is a number, o.w. is a word
    except:
        lst.append(l[0])
        count -= 1
        if count == 0: #get to the last word of this test case
            lst = sorted(lst, key=lambda x: x[:2]) #sort only by the first two letters
            for i in lst:
                print(i)
            print("\n")
    else:
        if num == 0: #input terminates
            break
        lst = []
        count = num
