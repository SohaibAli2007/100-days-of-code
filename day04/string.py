#multi line string
print (""" I
       am
       
       awesome""")

#string methods
print("sohaib".upper())
print("sohaib".lower())
print("sOhAib person".title()) #capitalizes first letter of each word
#dont alter string variable, but modify it

name = "Sohaib"
print(len(name)) #prints length of string
print("ib" in name)
#in checks if there is a specific substring in a string

#escaping strings

name = "soh\"ib" #\ will escape a character and include what initially isnt allowed to be called
#or
name = 'So"haib' #different type of quote so it will incldue
