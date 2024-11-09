class employee:
    company="google"
    def showdetails(self):
       print("this is an employee")
class programer:
    language="python"
    def getlanguage(self):
      print(f"The programer language{self.language} is ")
    def showdetails(self):
      print("This is a programer")
e=employee()
e.showdetails()
p=programer()
p.showdetails()

