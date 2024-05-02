#!/usr/bin/python3
def islower(c):
    for i in range(ord('a'), ord('z')+1):
        if (ord(c) < ord('a') or ord(c) > ord('z')):
            return False
        elif (c == chr(i)):
            return True
    return False
