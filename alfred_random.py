import string
import sys
from random import SystemRandom

def main(args):
    r = SystemRandom()
    try:
        try:
            _min = int(args[1])
            _max = int(args[2])
        except:
            _min = 0
            _max = int(args[1])
    except:
        _min = 0
        _max = 10
    try:
        if args[0] == 'simple':
            l = list(string.letters + string.digits)
            r.shuffle(l)
            return ''.join(l[0:_max])
        if args[0] == 'strong':
            l = list(string.letters + string.digits + string.punctuation)
            r.shuffle(l)
            return ''.join(l[0:_max])
        if args[0] == 'integer':
            return r.randint(_min, _max)
        return r.uniform(_min, _max)
    except:
        return r.random()

if __name__ == '__main__':
    print main(sys.argv[1:])