sub1=int(input("Enter the first subject marks\n"))
sub2=int(input("Enter the second subject marks\n"))
sub3=int(input("Enter the third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are Fail because your sub marks is not greater than 33")
elif(sub1+sub2+sub3)/3<40:
    print("You are Fail because your sub marks is not greater than 40")
else:
    print("Congratulation you are passed the Exam")