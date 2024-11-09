class Employee:
    company="google"
class manager:
    company="cygnic"
    level=0
    def upgradelevel(self):
      self.level=self.level+1

class programer(Employee,manager):
    name="azzu"

p=programer()
p.upgradelevel()
print(p.level)
print(p.company)




