example = [1,2,3,4,5,6,7,]

from random import shuffle

shuffle(example)




def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)


mylist = ['','0','']    

shuffle_list(mylist)      # shuffles the broad

print(mylist)


def player_guess():

    guess=''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0,1 or 2")


    return int(guess)

myindex = player_guess()

def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)


# INITAL LILST
mylist = [' ','0',' ']

# SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

# USER GUESS
guess = player_guess()

# CHECK GUESS
check_guess(mixedup_list,guess)


