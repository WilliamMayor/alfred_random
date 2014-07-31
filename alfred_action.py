import sys
import alp
import alfred_random

def main(args):
    args = args[0].split(' ')
    r = alfred_random.main(args)
    sys.stdout.write(r)

if __name__ == '__main__':
    main(alp.args())