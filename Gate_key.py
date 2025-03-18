from random import randint
from rich.console import Console

console=Console()

console.print("Are you ready for an adventure?You must guess the secret key to the gate(Yes or No)" , style="blue1")

secret = randint(1,1000)



for _ in range(12):
    key = int(input("Enter the secret key to the gate to enter: " ))
    if key == secret:
        print("You won! Congratulations,you guessed the secret key")
        break
    else:
        len= abs(key - secret)

        if len < 20 :
            print("BOOOOM!You're just inches away! One guess and you got it") 
        elif 20 < len < 50 :
            print("just one step away from the right number!")
        elif  50 <= len < 80 :
            print("the number is near,focus!")
        elif 80 <= len < 120 :
            print("Hmm...You're getting there!fine-tune your guesses")
        elif 120 <= len < 150 :
            print("still a bit off! But don't worry , change your path")
        else:
            print("Turn around,the number is far away")
    
        

else:
     print(f"you lost!the secret key was {secret}.")