"""print("Hello World!")

for i in range(10):
    print("My name is Sohaib Ali")
"""

name = input("What is your name? ")
if name == "Sohaib":
    password = str(input("Enter your password: "))
    if password == "DioBrando1234":
        print("You have completed Day 01 of 100 Days of Code!")
    else:
        print("You have failed to complete Day 01 of 100 Days of Code...")
else:
    print("incorrect! Try again! ")