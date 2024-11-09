class complex:
   def __init__(self,r,i):
      self.real=r
      self.imaginary=i
   def __add__(self,c):
       return complex(self.real + c.real,self.imaginary+c.imaginary)
   def __mul__(self,c):
       mulreal=self.real*c.real-self.imaginary*c.imaginary
       mulimag=self.real*c.imaginary+self.imaginary*c.real
       return complex(self.real * c.real,self.imaginary*c.imaginary)
   def __str__(self):
       return f"{self.real}+{self.imaginary}i"

c1=complex(1,5)
c2=complex(2,6)
print(c1+c2)
print(c1*c2)
   