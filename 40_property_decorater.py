class employee:
    company="schiender electric"
    salary=13000
    salarybonus=500

    @property 
    def totalsalary(self):
        return self.salary+self.salarybonus

e=employee()
print(e.totalsalary)

