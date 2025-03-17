from random import randint
from rich.console import Console

console=Console()

console.print("Are you ready for an adventure?" , style="blue1")

secret = randint(1,1000)



for _ in range(7):
    x = int(input("enter number: " ))
    if x == secret:
        print("you won")
        break
    else:
        len= abs(x - secret)

        if len < 10 :
            print("You got relly close, just think a little bit") 
        elif len < 50 :
            print("You got close , keep going")
        elif len < 100 :
            print("Your're a bit far , come close")
        else:
            print("You're too far,you're on the wrong path")
    
        

else:
     print(f"you lost number is {secret}")