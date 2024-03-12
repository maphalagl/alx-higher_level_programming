#!/usr/bin/python3
for dig1 in range(0, 9):
    for dig2 in range(dig1 + 1, 10):
        if dig1 == 8:
            print("{:d}{:d}".format(dig1, dig2))
            break
        print("{:d}{:d}".format(dig1, dig2), end=", ")
