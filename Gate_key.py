from random import randint

secret = randint(1,1000)



for _ in range(7):
    x = int(input("enter number: "))
    if x == secret:
        print("you won")
        break
    else:
    
        if x > secret:
                print("the number is large")
        else:
                print("the  number is smaller")

else:
     print("you lost")