import re

#pulls text in from a text file
t = open("C:\\Users\\cathe\\PythonProjects\\TextIn.txt", "r")

#puts text in a string
myString = t.read()

#Splits sting into an array
myList = re.split('\n',myString)

#Defines nartural sort
def natural_key(string_):
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

#Sorts with natural sort
myList.sort(key = natural_key)

#Create a pyramid with the words
def create_pyramid(nums):
 rows = int(len(myList))
 k = round(rows/2)
 countwords=1
 g=1

 for i in range(1, rows+1):
     for space in range(1, (rows-i)+1):
         print("  ", end="")

     while g!= i:
         g+=1
         print(myList[countwords],end=" ")
         countwords+=1
     g=1


create_pyramid(myList)







