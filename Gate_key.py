from random import randint
from rich.console import Console

console=Console()

question=console.input("[green_yellow]Are you ready for an adventure?😻🤔You must guess the secret key to the gate(yes or no) [/green_yellow]")

if question == "yes" :
    console.print("\n Great! Let the adventure begin.... \n" , style="orchid")
else:
    console.print("\n You just missed out on an exciting journey! \n" , style="bright_magenta")
    exit()

secret = randint(1,200)



for _ in range(12):
    
    key = int(console.input(" [blue1]Enter the secret key to the gate to enter:🏰🪄(Guess a number (1 to 200)) [/blue1]" ))
    
    if key == secret:
        console.print("\nYou won! Congratulations,you guessed the secret key 🏆🌻\n" , style ="gold1")
        break
   
    else:
        len= abs(key - secret)

        if len < 5 :
            console.print("\n💥BOOOOM!You're just inches away! One guess and you got it\n" , style ="chartreuse1") 
        
        elif 15 < len < 40 :
             console.print("\njust one step away from the right number!🔥\n", style="yellow1")
        
        elif  40 <= len < 80 :
            console.print("\nthe number is near,focus!🔎\n" , style="dark_orange")
       
        elif 80 <= len < 100 :
            console.print("\nHmm...You're getting there!fine-tune your guesses🌠🌟\n" , style = "orange_red1")
        
        elif 100 <= len < 150 :
            console.print("\nstill a bit off! But don't worry , change your path✨\n" , style="magenta3")
        
        else:
            console.print("\nTurn around,the number is far away🧨\n" , style="deep_pink1")
    
        

else:
     console.print(f"\nyou lost!the secret key was {secret}💔.\n" , style ="red1")