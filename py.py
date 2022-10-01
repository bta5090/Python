
from re import A
from xml.etree.ElementInclude import include

import random


def surprise(x, y, z):

    f = random.choice([x, y, z])

    return f


b = input("What is your first number?\n")
c = input("What is your second number?\n")
d = input("What is your last number?\n")

surprise(b, c, d)