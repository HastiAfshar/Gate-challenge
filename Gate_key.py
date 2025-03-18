from random import randint
from rich.console import Console

console=Console()

console.print("Are you ready for an adventure?You must guess the secret key to the gate(Yes or No)" , style="green_yellow")

secret = randint(1,1000)



for _ in range(12):
    
    key = int(console.input("[blue1]Enter the secret key to the gate to enter: [/blue1]" ))
    
    if key == secret:
        console.print("You won! Congratulations,you guessed the secret key" , style ="gold1")
        break
    else:
        len= abs(key - secret)

        if len < 20 :
            console.print("BOOOOM!You're just inches away! One guess and you got it" , style ="chartreuse1") 
        
        elif 20 < len < 50 :
             console.print("just one step away from the right number!", style="yellow1")
        
        elif  50 <= len < 80 :
            console.print("the number is near,focus!" , style="dark_orange")
       
        elif 80 <= len < 120 :
            console.print("Hmm...You're getting there!fine-tune your guesses" , style = "orange_red1")
        
        elif 120 <= len < 150 :
            console.print("still a bit off! But don't worry , change your path" , style="magenta3")
        
        else:
            console.print("Turn around,the number is far away" , style="deep_pink1")
    
        

else:
     console.print(f"you lost!the secret key was {secret}." , style ="red1")