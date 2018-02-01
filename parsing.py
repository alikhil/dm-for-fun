#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  30 09:32:20 2018

@author: alikhil
"""


# 
banned = ["<1>\n", "<2>\n","<3>\n","<4>\n"] #, "ls\n", "cd\n"]
sessions = []
current = 0
# I have concatenated all session files to single file using following command:
# cat USER* > total.txt

tokens = {}

with open("UNIX_user_data/total.txt", "r") as f:
    while(f.readable() ):
        line = f.readline()
        if line.startswith("**SOF**"):
            sessions.append(set())
            
        elif line.startswith("**EOF**"):
            current += 1
        elif line == "":
            
            break
        elif line in banned:
            continue
        else:
            token = line[:-1]
            if not tokens.get(token, False):
                tokens[token] = set()

            tokens[token].add(current)
            sessions[current].add(token)

# print all tokens
print(sorted([(len(tokens[key]), key) for key in tokens.keys()]))

with open("sessions.csv", "w") as f:
    
    for session in sessions:
        f.write(",".join(map(lambda s: '"%s"' % (s), session)) + "\n")
        