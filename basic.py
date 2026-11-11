#built in functions in python.

# this is a comment 

"""
this is a multi line comment
"""


print(" trying the print function ")

print("shows me what is in the brackets")

#this one shows me the length of the string in the brackets
print(len('eye balls')) 

#this one shows me the length of the list in the brackets. Didnot know that lists have a length too.
print(len(['eye balls','potato','gulp'])) 

#input function.

input('enter your name: ')

name = input('enter your First name: ')
lastname = input('enter your last name: ')
age = input('enter your age: ')
print(name)
print(lastname)
print(age)
print('your name is ' + name + ' ' + lastname + ' and your age is ' + age)

#round function. rounds the number to the nearest whole number.
print(round(3.4159))
print(round(3.5))

#returns absolute value
print(abs(-69))

#string and numbers can not be added together . either u transform all of the into intiger or string
print(int('2')+3)
print('23'+str(4)) 

# To use SUM() , the given numbers must be a list . returns summation
print(sum([1,2,69]))

# min() doesnt always  have to take a list . But  can take a list. returns minimum or smallest number
print(min(12,150,0,-12))
print(min([12,150,0,-12]))

#max() doesnt always  have to take a list . But  can take a list. returns minimum or smallest number
print(max(12,150,0,-12))
print(max([12,150,0,-12]))

#type() returns data type
print(type('bns'))
print(type("bns"))
print(type(230))
print(type(230.0))
print(type(1 + 2j)) # python uses j as a complex number indicator
print(type([1,2,3]))#list
print(type((1,2,3))) # need to research what a tuple means here . IG i will know later . 
print(type({1,2,3}))#set
print(type({'name':'Fardin'})) #dict or data structure
print(type(True))
print(type(1<0))
print(len('Fardin')<len('ehsan'))

#range()
print(range(10))
print(range(1,10,1)) # 1st number is lower end , middle is maxend , last is how much increment 

#list() gives a list.EZ XD.
print(list(range(1,10,1))) #good
print(list([0,1]))#not good LMAO

#id()
print(id(1)) # id returns an unique intiger identifier for the object . google says it might be the actual memory address

#dir
print(dir(2)) # returns related properties and methods for that specific object
print(dir('fardin')) # very good 