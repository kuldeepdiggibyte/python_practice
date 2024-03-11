#code for string slice
#str = "This is a string"
#print(str[0:3])
#print(str[:5])
#print(str[5:])

#str1 = "string contains various alphabets and in English their are 26 alphabets"
#print(str1.find('ins')) #if word not present in string then returns -1 or returns index of first alphabet match
#print(str1.count('various alphabet')) #returns count of alphabet or word
#print(str1.capitalize())
#print(str1.upper())
#print(str1.lower())

#join

greeting = "Hello"
name = input("Enter your name : ")

print(greeting + " "+ name + ", " + "welcome" )
print('''{},{},welcome'''.format(greeting,name))
print(f"{greeting}, {name} welcome")

#replace
str = "hello world"
str1 = str.replace("world","universe")
print(str1)