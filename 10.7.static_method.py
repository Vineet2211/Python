class Employee:
    company="Google"

    def getSalary(self,signature):
        print(f"Salary for this Employee working in {self.company} is {self.salary} \n {signature}")

        @staticmethod
        def greet():
            print("Good Morning , Sir")

        @staticmethod
        def time():
            print("The Time is 9Am in the Morning")

harry=Employee()
harry.salary=100000
harry.getSalary("Thanks!") #
Employee.getSalary(harry,"Thanks")
harry.greet() #Employee.greet()
harry.time()