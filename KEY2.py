#KEY GENERATOR (RANDOM)

import string
import random


def key_code():
    def key2():
        a = random.choice(string.ascii_letters)
        b = random.choice(string.ascii_letters)
        c = random.choice(string.ascii_letters)
        e = random.randint(0, 9)
        d = [str(a),str(b),str(c),str(e)]
        g = random.sample(d, k = 4)
        return g
    fulllenght = ''.join(key2()) + '-' + ''.join(key2()) + '-' + ''.join(key2()) + '-' + ''.join(key2())
    return fulllenght

