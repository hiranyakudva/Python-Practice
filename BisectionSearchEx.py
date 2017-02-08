# This code is an example of Bisection search which is a powerful way to 
# reduce computation time by eliminating half of the results at a time.
# This is a guessing game where yoou guess a number between 0 and 100 and
# the computer guessess the number by taking your feedback on its guess.

print('Please think of a number between 0 and 100!')
low=0
high=100
print('Is your secret number 50?')
print('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
response=raw_input()
while response!='c':
    if response=='h':
        high=(low+high)/2
        print 'Is your secret number ', str((low+high)/2), '?' 
        print('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
        response=raw_input()
    elif response=='l':
        low=(low+high)/2
        print 'Is your secret number ', str((low+high)/2), '?' 
        print('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
        response=raw_input()
    else:
        print('Sorry, I did not understand your input.')
        print 'Is your secret number ', str((low+high)/2), '?' 
        print('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
        response=raw_input()
if response=='c':
    print'Game over. Your secret number was: ',str((low+high)/2)      
        
