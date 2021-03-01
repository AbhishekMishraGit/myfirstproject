

import random
import time



def game_Introduction():
    print("Welcome to the door game!")
    time.sleep(2)
    print("Rules are simple, you have to pass through walls by selecting a door.")
    time.sleep(4)
    print("each wall have 2 doors")
    time.sleep(2)
    print("every time u have to select a door")
    time.sleep(3)
    print("if u select the right door then u will be pass to the next wall")
    time.sleep(5)
    print("and there again, u have to select the right door")
    time.sleep(5)
    print("u have to do this untill u open the last door of last wall")
    time.sleep(5)
    print("if u open the right door of last wall, then u will win the game")
    time.sleep(5)
    print("but if at any piont u select the wrong door at any wall, then u will loose the game")
    time.sleep(5)
    print()
    print("are u ready?")
    time.sleep(5)

game_Introduction()

play_Again = 'yes'
while play_Again == 'yes':
    
    n = 0
    level = random.randint(1,5)

    
    while level > 0:
        wall_Count = level
        print('Total no. of wall in Your Game is: ' + str(wall_Count))
        n = n+1
        level = level-1
        time.sleep(2)
        print('you have reached infront of wall: ' + str(n))
        time.sleep(2)
        print('Please Select any one door out of two.')
        print('enter "1" for door(1) and "2" for door(2)')
        door = int(input())
        

        while door != 1 and door != 2:
            print('please enter 1 or 2')
            door = int(input())
        print('you selected door: ' + str(door))
        

        gameOver = 0
        doorUHave = random.randint(1,2)
        
        
        if doorUHave == door:
            

            if level != 0:
                print('u choose the right door, now u have reached to the next Wall...')
            else:
                print('Congratulations!!! U hAvE wOn ThE gAmE')

                
            print('******************')
            print('******************')
            time.sleep(5)

            
        else:
            print('u selected the wrong door, u loose the game...')
            print('game over!')
            print('******************')
            print('******************')
            time.sleep(3)
            break

        
    play_Again = input('Do you want to play Again(yes or no): ')
    time.sleep(3)
    print('#############################################')
    time.sleep(3)
    print('#############################################')
