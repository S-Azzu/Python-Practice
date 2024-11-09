class person:
    country="india"
class Employee:
    company="Azooba"
    def takebreath(self):
       print("I am breathing") 
    def getsalary(self):
        print(f"The salary of employee is{self.getsalary}")
    def takebreath(self):
        print("I am employee so I am happy now!")
class programmer(Employee):
    company="MCQ"
    def takebreath(self):
       
       print("I am breathing fastly") 
    def getsalary(self):
        print(f"The salary of employee is{self.getsalary}")
    def takebreath(self):
        super().takebreath()
        print("I am employee so I am happy now!")
p=person()
pr=programmer()
pr.takebreath()
print(pr.company)
e=Employee()
e.takebreath()
print(e.company)
