#!/usr/bin/python3

from sys import argv
from random import choice, randint
from itertools import repeat

File = open('Dictionary', 'r').read().splitlines()
Len = 20
Count = 1

def Pwgen(File, Len):
    Password = ''
    while len(Password) < Len:
        coin = randint(0, 1)
        RandomWorld = choice(File)
        RandCut = randint(1, len(RandomWorld))
        RandInt = randint(0, 9)
        if coin == 1:
            Password = Password + RandomWorld[:RandCut].capitalize()
        else:
            Password = Password + str(RandInt)
    return Password[:Len]

if __name__ == "__main__":
    try:
        if argv[1]:
            Len = int(argv[1])
        if argv[2]:
            Count = int(argv[2])
    except:
        pass

    for __ in repeat(None, Count):
        Password = Pwgen(File, Len)
        print(Password)
