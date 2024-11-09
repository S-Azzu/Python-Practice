import random
randomnumber=random.randint(1,100)
userguess=None
guesses=0

while(userguess != randomnumber):
    userguess=int(input("enter your number:"))
    guesses+=1
    if(userguess==randomnumber):
        print("you guessed it right")
    else:
        if(userguess>randomnumber):
           print("you guessed it wrong!Enter a smaller number")
        else:
           print("you guessed it wrong!Enter a larger number")

print(f" you guessed the number in {guesses}guesses")
with open("highscore.txt","r")as f:
    highscore=int(f.read())
if(guesses<highscore):
    print("you have cracked the high score")
    with open("highscore.txt","w")as f:
        f.write(str(guesses))
