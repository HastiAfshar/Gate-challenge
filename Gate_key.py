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
    
        if secret > x :
                print("the number is larger")
        else:
                print("the  number is smaller")

else:
     print(f"you lost number is {secret}")