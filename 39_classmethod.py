class employe:
    company="amazon"
    salary=100000
    Location="pune"

    #def changesalary(self,sal): >>>>>>>indirect method 
      #self.__class__.salary=sal
    @classmethod
    def changesalary(cls,sal):
        cls.salary=sal

e=employe()
print(e.salary)
e.changesalary(5000000)
print(e.salary)  

