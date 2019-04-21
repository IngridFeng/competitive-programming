#! /usr/bin/python3
import sys
lines = sys.stdin.readlines()
l, w, n, r = [int(i) for i in lines.pop(0).split()] #parse input values

ns = {}
reachable = {}
counter = 1
for li in lines:
    ns[counter] = [int(i) for i in li.split()] #save coordinates of cranes into dictionary
    reachable[counter] = []
    counter += 1

ms = {"left": [-l, 0], "right": [l, 0], "bot": [0, -w], "top": [0, w]}
bag = {"left": False, "right": False, "bot": False, "top": False}
count = 0
for m in ms:
    for n in ns:
        if (ms[m][0] - 2*ns[n][0])**2 + (ms[m][1] - 2*ns[n][1])**2 <= r**2*4:
            #check the distance less than or equal to r
             reachable[n].append(m) #save all the walls a crane can reach
             bag[m] = True #if a wall is reachable by at least one crane
    if not bag[m]:
        print("Impossible") #impossible when a wall is not reachable by any cranes
        sys.exit()

#when a crane can reach all walls
for i in range(1, n+1):
    all = set(reachable[i])
    if len(all) == 4:
        print(1)
        sys.exit()
#when two cranes can reach all walls
for i in range(1, n+1):
    for j in range(1, n+1):
        all = set(reachable[i] + reachable[j])
        if len(all) == 4:
            print(2)
            sys.exit()
#when three cranes can reach all walls
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            all = set(reachable[i] + reachable[j] + reachable[k])
            if len(all) == 4:
                print(3)
                sys.exit()
#when four cranes can reach all walls
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            for l in range(1, n+1):
                all = set(reachable[i] + reachable[j] + reachable[k] + reachable[l])
                if len(all) == 4:
                    print(4)
                    sys.exit()
