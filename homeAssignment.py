import sys

def collatz(number):
    n = 0
    if (number % 2) == 0:
        n = number // 2
    else:
        n = number * 3 + 1
    print(n)
    return n

print('Input integer value greater than 0 and watch')
while True:
    try:
        m = int(input())
        if m < 0:
            print('Please input something greater than 0.')
            continue
        while True:
            if m != 1:
                m = collatz(m)
            else:
                print('Have you seen that?!')
                sys.exit()
    except ValueError:
        print('Please input non zero integer.')

