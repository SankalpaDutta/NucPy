import numpy as np 

##sim
person = "Sankalpa"
print("My name is {}".format(person))

print(f"May name is {person}")




d = {'a':123,'b':567}

print(f"Meine number is {d['a']}")




library = [('Author','Book','Pages'),('ACDoyale','SHolmes',67),('Achristy','HPoearo thriller stories',89)]


for book in library:
    print(f"Books are {book[1]}")

for author,book,pages in library:
    print(f"{author:{10}} {book:{10}}  {pages:->{10}}")




#reading a file

myfile = open("/home/sankalpa/NucPy/NucPy/test.txt")
print(myfile)
print(myfile.read())
myfile.seek(0)

content=myfile.read()
print(content)



# myfile.close()     # Always close file after use

with open("/home/sankalpa/NucPy/NucPy/test.txt") as mynewfile:
    myVariable=mynewfile.readlines()


print(myVariable)



#Reading PDF

#import PyPDF2

#myfile2= open("/home/sankalpa/NucPy/NucPy/sample.pdf",mode='rb') 

#pdf_reader=PyPDF2.pdf


# Regular Expression
#To find a certain keyword
# ability to find seperate groups of words
#ability to exclude number or puctuation








