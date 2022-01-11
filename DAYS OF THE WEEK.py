run = True
while run == True:

    num = int(input('which day of the week you want to see?(1-7, 0 TO EXIT)'))

    if num == 1:
        print('SUNDAY')

    elif num == 2:
        print('MONDAY')

    elif num == 3:
        print("TUESDAY")

    elif num == 4:
        print("WEDNSDAY")

    elif num == 5:
        print("THURSDAY")

    elif num == 6:
        print("FRIDAY")

    elif num == 7:
        print("SATURDAY")

    elif num == 0:
        run = False

    else:
        print('INVALID INPUT!!')
        
    
