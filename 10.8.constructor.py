class Employee:
    company="Google"

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is Created!")

        def getDetails(self):
            print(f"The name of the Employee is {self.name}")
            print(f"The Salary of the Employee is {self.salary}")
            print(f"The Subunit of the Employee is {self.subunit}")

            def getsalary(self,signature):
                print(f"Salary for this Employee working in {self.company} is {self.salary} \n{signature}")
                
                @staticmethod
                def greet():
                    print("Good Morning , Sir")

                @staticmethod
                def time():
                    print("The time is 9AM in the Morning")
                    
harry=Employee("Vineet",100000,"Youtube")
#harry = Employee()--> This Throws an eror (missing 3 required positional argument:)
harry.getDetails()