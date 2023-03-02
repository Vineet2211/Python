from datetime import date


name=input("Enter your name\n")
print("Good Afternoon,"+name)

# New Programme
letter='''Dear <|NAME|>,
Hii Vineet You are selected in Apple!
Bill
Date: <|DATE|>
'''
name=input("Enter Your Name\n")
date=input("Enter the Date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)