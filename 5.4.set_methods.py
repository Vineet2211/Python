#An empty set created using the below syntax
b=set()
print(type(b))

#Adding the value to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(4)#Adding the repetedly does not change a set
b.add((4,5,6))

#Accessing the elements
#b.add({4:5})  cannot add list or dictonaryto sets
print(b)

#Length of the sets
print(len(b))   #prints the length of this set

#Removal of an Item
b.remove(5)  #Remove 5 from the set b 
#b.remove(15) #throws error because not present in the set
print(b)

print(b.pop())
print(b)