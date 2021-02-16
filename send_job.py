from __future__ import print_function
from tasks import add

def main():
    res = add.delay(4,4)
    print(res.get(timeout=1))

if __name__ == '__main__':
    main()
