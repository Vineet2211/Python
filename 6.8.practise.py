text=input("Enter the Text\n")

if("make a money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("Click this" in text):
    spam=True
else:
    spam=False
    
    if(spam):
        print("This text is Spam")
    else:
        print("This text is not Spam")
    