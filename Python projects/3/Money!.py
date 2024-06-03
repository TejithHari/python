#import..........
import time
import random

#Start of the game
print('Welcome to Money!')

# Printing the place
scene = ['Beach','Bank','Treehouse','Friend\'s house','Your house']
sceneprinter = random.choice(scene)
print('Place = ' + sceneprinter)
print('There are secret codes!Crack e\'m!')

#set money to 0
money = 0

#I have put while True so it will run forever
while True:
    score = input('Type 1 To get some money!|Press Q to exit....|Your input: ')
    if money == 1001:
        print('Congrats!You have passed 1000!!!!!')

    if score == '1':
        money = money + 1
        print('You earn one point!')
        print('Money in your bank is : ' + str(money))

    elif score == 'q':
        print('Bye Bye.......')
        print('Come again to play Money!')
        print('Money in your bank is : ' + str(money))
        print('Coming soon : Money!-2')
        time.sleep(10)
        break

    #secret codes
    elif score == '2014365':
        print('YOU HAVE CRACKED THE SECRET CODE! SO HERE IS A BONUS: YOU GET 100 DOLLARS!!!!!')
        money = money + 100
        print('Money in your bank is : ' + str(money)) 
        
    elif score == '2014365123':
        print('YOU HAVE CRACKED THE TOP SECRET CODE! SO HERE IS A MEGA BONUS: YOU GET 1000 DOLLARS!!!!!')
        money = money + 1000
        print('Money in your bank is : ' + str(money)) 

    # last part  
    else:
        print('Enter a VALID action.....')
