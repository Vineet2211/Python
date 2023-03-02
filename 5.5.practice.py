mydict={
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Option are",mydict.keys())
a=input("Enter the Hindi Word\n")
print("The meaning of your word is:",mydict[a])

#Below line will not throw an error if the key is not present in the Dictonary
print("The Meaning of your word is:",mydict.get(a))