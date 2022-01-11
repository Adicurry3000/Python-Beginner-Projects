import random

name=input ("what is your name")

guesses=" "

print("hi", name, "time to play hang man")

play = input("press p to play and q to quit")

turns=10

words=['apple','banana','orange','pineapple','greenapple','grapes','cat','dog','wolf']

word = random.choice(words)

a=False


def play_game(turns=10,guesses=""):

    while turns > 0:
        failed = 0

        for char in word:

            if char in guesses:

                print(char)

            else:
                print('_')

                failed+=1
        if failed==0:
            a = 'you won'
            print (a)


        guess =input('enter a letter')

        guesses+=guess

        if guess not in word:

            turns-=1

            print ('wrong')

            print ('you have',turns,"turns left")

        if turns==0:
            print ("you lost")




while play=="p":
    while a != 'you won':
        play_game()
    play_again = input('do you want to play again . click p to play again and q to qwit')
    while play_again=="p":
        play_game()
else:
    print('see you soon')