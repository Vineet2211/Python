mydict={
    "fast":"In a Manner",
    "harry":"A Coader",
    "marks":[1,2,5],
    "anotherdict":{"Vineet":"Coder"},
    1:2
}

#dictonary methods
print(list(mydict.keys()))  #Prints the keys of the Dictonary
print(mydict.values())  #Prints the keys of the Dictonary
print(mydict.items())  #Prints the (key,Value)for all contenets of the dictonary
print(mydict)
updatedict={
    "Lovish":"Friend",
    "Divya":"Friend",
    "Shubham":"Friend",
    "harry":"A Dancer"
}
mydict.update(updatedict)#update the dictonary by adding key-value pairs from updatedict
print(mydict)

print(mydict.get("harry")) #Prints the value associsted with key harry
#print(mydict("harry")) #Prints the value associsted with key harry

#The Diffrence between .get and []syntax in dictoneris
print(mydict.get("harry2"))#Returns none as harry2 is not present in the dictonary
#print(mydict["harry2"])   #Throws an error as harry2 is not present in the dictonary