import main
import random
cons=main.ConsoleGame()
mat=cons.create()
print(mat)
while True:
    choice=int(input("Enter 1 to play:"))
    if choice==1:
         print('start the game')
         inp=eval(input('Enter a number below 100:'))
         ans=cons.check(inp)
         if ans==1:
            print('You suck!')
         else:
            print('You got it man!')
    else:
        print('enter the proper choice')
