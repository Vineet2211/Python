greeting = "GOOD MORNIMG,"
name="VINEET"
print(type(name))

#Concatenating two String
c = greeting + name
print(c)
name="VINEET"
print(name[4])
#name[3] = "d"--> Does not work
print(name[1:6])
print(name[:5])  # is same as name[0:5]
print(name[1:])  # is same as name[1:6]
c = name[-6:-1]  # is same as name[1:5]
print(c)

name = "VineetIsGood"
# d= name[0::3]
d = name[:0:-1]
print(d)