#1
def greatnum(a,b,c):
    if a>b:
        if a>c:
            print(f"{a} is the greatest number")
    elif b>a:
        if b>c:
            print(f'{b} is the greatest number')
    elif c>a:
        if c>b:
            print(f"{c} is the greatest number")
    else:
        print('Error')

greatnum(3,4,5)