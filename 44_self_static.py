class Employee():
    company = "Google"
    
    def __init__(self, salary):
        self.salary = salary
    
    def getsalary(self):
        print(f"The salary for the employee working at {self.company} is {self.salary}")
    
    @staticmethod
    def greet():
        print("Have a nice day")

azzu = Employee(10000)
azzu.getsalary()
azzu.greet()
