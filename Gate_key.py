from random import randint
from rich.console import Console
import time


console=Console()

text="Are you ready for an adventure?😻🤔 you must guess the secret key to the gate(yes or no):"
for char in text:
    console.print(char,style="green_yellow" , end="")
    time.sleep(0.05)
question = console.input()    


if question == "yes" :
    console.print("\n Great! Let the adventure begin.... \n" , style="orchid")
else:
    console.print("\n You just missed out on an exciting journey! \n" , style="bright_magenta")
    exit()

secret = randint(1,100)


for _ in range(10):
    
    key = int(console.input(" [blue1]Enter the secret key to the gate to enter:🏰🪄(Guess a number (1 to 100)) [/blue1]" ))
    
    if key == secret:
        text = "\nYou won! Congratulations,you guessed the secret key 🏆🌻\n"
        for char in text:
            console.print(char,style="gold1" , end="")
            time.sleep(0.05)
        break
   
    else:
        len= abs(key - secret)

        if len < 3 :
            console.print("\n💥BOOOOM!You're just inches away! One guess and you got it\n" , style ="chartreuse1") 

        elif 3 <= len < 8:
             console.print("\nYou're very close!just a small change!🔥\n" , style = "plum1")
        
        elif 8 <= len < 15 :
             console.print("\njust some step away from the right number!🔥\n", style="yellow1")
        
        elif  15 <= len < 30 :
            console.print("\nthe number is near,focus!🔎\n" , style="dark_orange")
       
        elif 30 <= len < 50 :
            console.print("\nHmm...You're getting there!fine-tune your guesses🌠🌟\n" , style = "orange_red1")
        
        else:
            console.print("\nTurn around,the number is far away🧨\n" , style="deep_pink1")
    
        

else:
    text = f"You lost! the secret key was {secret}💔.\n"

    for char in text:
        console.print(char,style = "red1" , end="")
        time.sleep(0.05)


text="\nDid you enjoy the adventure? Choose one:great / good / bad \n"

for char in text:
    console.print(char,style="green_yellow" , end="")
    time.sleep(0.05)
question2=console.input()


if question2 == "great":
    console.print("\nWow!you're a true adventurer\n" , style="green3")

elif question2 == "good":
    console.print("\nNice!glad you have fun\n" , style="cyan2")

else:
    console.print("\nOh no!Next time,you'll have a enjoy!\n" , style="cyan1")


