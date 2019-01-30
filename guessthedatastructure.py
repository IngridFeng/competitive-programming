#! /usr/bin/python3
import sys
lines = sys.stdin.readlines()
pos = 0
while pos < len(lines): #until EOF
    l = lines[pos].split()
    if len(l) == 1: #beginning of a test case, initiate all values
        end = pos + int(l[0])
        bags = {"p":[],"q":[],"s":[]}
        #use a dictionary of (key, value)-(string,list) to keep track of the bags and data structure
    else:
        tp, ele = int(l[0]), int(l[1])
        if tp == 1: #put element into the bag
            for key in bags:
                bags[key].append(ele)
        else: #take element out of the bag
            for key in list(bags):
                if ele not in bags[key]:
                    bags.pop(key) #no element in bag then delete this data structure
            if "p" in bags:
                if ele != max(bags["p"]): #not priority queue
                    bags.pop("p")
                else: #satisfy PQ up till now
                    bags["p"].remove(ele)
            if "q" in bags:
                if ele != bags["q"][0]: #not queue
                    bags.pop("q")
                else: #satisfy queue up till now
                    bags["q"].remove(ele)
            if "s" in bags:
                if ele != bags["s"][-1]: #not stack
                    bags.pop("s")
                else: #satisfy stack up till now
                    bags["s"].pop()
    if pos == end: #end of this test case
        if len(bags) > 1: #more than one DS
            print("not sure")
        elif "p" in bags:
            print("priority queue")
        elif "q" in bags:
            print("queue")
        elif "s" in bags:
            print("stack")
    if bags == {}: #got the result for this test case
        print("impossible")
        pos = end #force to the last line of this test case
    pos += 1 #go to next line
