#!/usr/bin/python3
""" doc """


def validUTF8(data):
    """ doc """
    i = 0
    for ints in data:
        if i <= 128:
            if (ints.bit_length() >= 8):
                return False
        else:
            if (ints.bit_length() >= 10):
                return False
        i += 1
    return True
