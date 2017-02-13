# An example of using recursion to check whether a word is a palindrome.

def isPal(x):
'''
x is a string with no spaces and puncuation marks
'''
    x=x.lower()
    if len(x)<=1:
        return True
    else:
        return (x[0]==x[-1]) and (isPal(x[1:-1]))
