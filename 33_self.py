class employee():
    company="google"
    def getsalary(self,salary):
     print(f"salary for the employee is working in these {self.company} is {self.salary}")
    @staticmethod
    def greet():
        print("Have a nice day")
 
azzu=employee()
employee.salary=10000
azzu.getsalary("congrates")
azzu.greet()

   
          
