import time
passcode = "12345"
pass_length = len(passcode)
tries = 0

def check_password():
    global tries
    print("Enter passcode")
    pass_attempt = input("Must be 5 digits only!\n")
    pass_attemptLength = len(pass_attempt)
    
    if pass_attemptLength != pass_length:
        print("Password cannot be more or less than 5 digits! Try again\n")
        tries+=1
        check_password()
    else:
        if passcode == pass_attempt:
            print("Accessing phone")
        else:
            print("Incorrect passcode. Please try again! ")
            tries+=1
            print(tries)
            check_password()
    if tries == 3:
        print("You have been locked out of the account. Try again in one minute.")
        time.sleep(60)


check_password()