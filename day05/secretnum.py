import random
comp_number = random.randrange(1,100)

correct = False
tries = 0

while correct == False:
    print(comp_number)
    print(f"tries: {tries}")
    user_number = int(input("I'm thinking of a number between 1-100 \nWhat number is it? -->"))

    def check():
        if user_number > comp_number:
            print("Your value is greater than the guess!\n")
        else:
            print("Your value is less than the guess!\n")

    if user_number != comp_number:
        print("\nNice try! Unfortunately it is incorrect")
        check()
        tries+=1
        if tries == 10:
            print("Too late! Number will be reset!\n\n")
            comp_number = random.randrange(1,100)
        continue
        
    else:
        print("\nGreat job! You guessed the correct number!")
        correct = True






