from random import randint

num = 8

Hidden_Pattern=[['~'for x in range(num)] for y in range (num)]
Guess_Pattern=[['~'for x in range(num)] for y in range (num)]

def create_board():
    
    some_str = ''
    for i in range (len(Guess_Pattern)):
        some_str+=" ".join(Guess_Pattern[i])+'\n'
    return(some_str)

print(create_board())
    