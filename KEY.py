#KEY GENERATOR (RANDOM)

import string
import random


def key_code():
    a = random.choice(string.ascii_letters)
    b = random.choice(string.ascii_letters)
    c = random.choice(string.ascii_letters)
    e = random.randint(0, 9)
    d = [str(a),str(b),str(c),str(e)]
    g = random.sample(d, k = 4)
    firstblock = ''.join(g) + '-'
    a = random.choice(string.ascii_letters)
    b = random.choice(string.ascii_letters)
    c = random.choice(string.ascii_letters)
    e = random.randint(0, 9)
    d = [str(a),str(b),str(c),str(e)]
    g = random.sample(d, k = 4)
    secondblock = ''.join(g) + '-'
    a = random.choice(string.ascii_letters)
    b = random.choice(string.ascii_letters)
    c = random.choice(string.ascii_letters)
    e = random.randint(0, 9)
    d = [str(a),str(b),str(c),str(e)]
    g = random.sample(d, k = 4)
    thirdblock = ''.join(g) + '-'
    a = random.choice(string.ascii_letters)
    b = random.choice(string.ascii_letters)
    c = random.choice(string.ascii_letters)
    e = random.randint(0, 9)
    d = [str(a),str(b),str(c),str(e)]
    g = random.sample(d, k = 4)
    fourthblock = ''.join(g)
    fulllenght = firstblock + secondblock + thirdblock + fourthblock
    return fulllenght
