class Employee:
    company="Google"
    salary=100
    
harry=Employee()
rajni=Employee()

#Creating instance attributr slalry for both the Objects
#harry.salary=300
#rajni.salary=400
harry.salary=45
print(harry.salary)
print(rajni.salary)

#Below line thorws eror as address is not present in instance?class
#print(rajni.address)