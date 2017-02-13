# This is an example of how a complex problem can be solved easilyusing recursion.
# Check https://en.wikipedia.org/wiki/Tower_of_Hanoi for more info on Towers of Hanoi.

def printMove(fr,to):
    print 'Move from ', str(fr), 'to ', str(to)

def Towers(n, fr, to, spare):
    if n==1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
