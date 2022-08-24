#!/usr/bin/python3
def pow(a, b):
    p = a
    for i in range(1, b):
        p = a * p
    return p
