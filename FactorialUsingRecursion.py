def fact(x):
    '''
    x: int
    returns: int, factorial of x
    '''
    if x==0:
        return 1
    else:
        return x*fact(x-1)
