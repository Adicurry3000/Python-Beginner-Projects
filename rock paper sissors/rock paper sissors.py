# rock v/s paper => rock wins
# paper v/s scissor => scissor wins
# scissor v/s rock => rock wins

import random
computer_score=0
player_score=0
print('rules of winning rock paper scissors game are as follows : \n'
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n")

play =int(input('do you want to start playing ??? \n 1.yess \n 2.no'))

while play==1:
    turns = int(input('how many turns do you want'))
    name = input('what is your name???')
    print('hi', name, "we are going to play rock paper sissors ")
    print('hi', name, 'it is your turn choose \n 1.rock \n 2.paper \n 3.scissors')
    print('')
    for i in range(turns):
        print(name,"choise")
        choice = int(input())

        while choice > 3 or choice < 1:
            choice = int(input("enter valid input: "))
        if choice==1:
            choice_name='rock'
        elif choice==2:
            choice_name='paper'
        else:
            choice_name='sissors'


        print(name,"'s choice is:",choice_name)

        print("now it is computer's turn\n ..........")

        print('')

        comp_choice=random.randint(1, 3)

        while comp_choice==choice:
            comp_choice = random.randint(1, 3)


        if comp_choice==1:
            comp_choice_name='rock'
        elif comp_choice==2:
            comp_choice_name='paper'
        else:
            comp_choice_name='sissors'

        print ("computer's choice=",comp_choice_name)


        print('')

        print('')

        print(comp_choice_name,'v/s', choice_name)

        print('')

        if ((choice == 1 and comp_choice == 2) or
                (choice == 2 and comp_choice == 1)):
            print('paper wins')
            if comp_choice==2:
                computer_score=+1
            else:
                player_score=+1


        elif ((choice == 1 and comp_choice == 3) or
              (choice == 3 and comp_choice == 1)):
            print("rock wins")
            if comp_choice==1:
                computer_score=+1
            else:
                player_score=+1


        else:
            print("sissors wins")
            if comp_choice == 3:
                computer_score = +1
            else:
                player_score = +1
        print("computer=", computer_score, "          player score=", player_score)
    play=int(input('do you want to play again(1/2)'))



print ('thanks for playing')


























