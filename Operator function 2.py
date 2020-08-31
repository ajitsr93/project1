#1. setitem(ob, pos, val) :- This function is used to assign the
# value at a particular position in the container.
#Operation – ob[pos] = val

import operator

li = [1, 5, 6, 7, 8]  #this is an object

print ("The original list is : ",end="")
for i in range(0, len(li)):
    print(li[i], end=" ")

print("\r")   #Doubt1 how the fuck this works ??? never studied

operator.setitem(li,4,99)   #role of setitem in my understanding is to replace an item in list

print("The modified list after setitem() is : ", end="")
for i in range(0, len(li)):
    print(li[i], end=" ")

print("\r")

print('thanks!')

#  this setitem thing can be done by normal asignment. This is a long cut to be honest
# first import then setitem . lengthy and complicated.


#############################################
#2. delitem(ob, pos) :- This function is used to
# delete the value at a particular position in the container.
#Operation – del ob[pos]
print("The modified list after setitem() is : ", end="")
for i in range(0, len(li)):
    print(li[i], end=" ")

print("\r")

operator.delitem(li,1)

print ("The modified list after delitem() is : ",end="")

for i in range(0, len(li)):
    print(li[i], end=" ")

print("\r")
######################

#3 Getitem simply retrieves the element from list

print ("The 4th element of list is : ",end="")
print (operator.getitem(li,3))


#4   setitem(ob, slice(a,b), vals) :-
# This function is used to set the values in a particular range in the container.

import operator
li = [1, 5, 6, 7, 8]
print ("The original list is : ",end="")
for i in range(0,len(li)):
    print (li[i],end=" ")

print ("\r")

operator.setitem(li,slice(1,4),[2,3,4])

print ("The modified list after setitem() is : ",end="")

for i in range(0, len(li)):
    print(li[i], end=" ")

print("\r")

print('Thanks')

#5 delitem

operator.delitem(li, slice(2, 4))

# printing modified list after delitem()
print("The modified list after delitem() is : ", end="")
for i in range(0, len(li)):
    print(li[i], end=" ")

print("\r")

#do these operators work on dictionaries as well ?
# how these for loops have been implemented ?
# how does slice work ? can it be used in genral ?
# Lets finich with these operator functions and then come back to doubts...

#6 getitem
#6. getitem(ob, slice(a,b)) :- This function is used to
# access the values in a particular range in the container.
print ("The 1st and 2nd element of list is : " , operator.getitem(li,slice(0,2)))


