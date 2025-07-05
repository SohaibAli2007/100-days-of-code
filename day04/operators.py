1 + 1 #addition
4 ** 2 #exponents
4//2 #floor division: rounds down
4 % 3 #modular: gives remainder of division

age = 8
age += 8 #combining arithmetic operator with assignment operator
print(age)

a = 1
b = 2
a == b #comparison operators
a != b 


#boolean operators
condition1 = True
condition2 = False
not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True

print(0 or 1) ## 1
print([] or False) ## '[]'
#or prints out the value that is not False

#and only evaluates 2nd argument if 1st is False

#bitwise operators
# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# ~ performs a binary NOT operation
# << shift left operation
# >> shift right operation

#is and in operators

#ternary operators
def is_adult(age):
    if age > 18:
        return True
    else:
        return False
    
def is_adult(age):
    return True if age> 18 else False
#cleans up code to make it one line only


