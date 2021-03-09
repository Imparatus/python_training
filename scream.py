import random




retry = "Y"

random_number = random.randint(1,10)


while True: #loop forever, True is always true
    print(random_number)
    guess = int(input("Guess a number from 1-10: "))  
     #just for testing
    if guess > random_number:
        print("Too Fucking High, Try again!: ")#guess = int(input("Too Fucking High, try again: "))  
    elif guess < random_number:
        print("Too Fucking Low, Try again!: ")#guess = int(input("Too Fucking Low, try again: "))
    else:
        pa = input("You won. PA? :")
        if pa == "y":
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thanks for playing!")
            break
    
    
