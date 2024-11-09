class number:
    def __init__(self,num1):
       self.num=num1
    def __add__ (self,num2):
        print("lets add")
        return self.num+num2.num
    def __mul__(self,num2):
        print("lets multiply")
        return self.num*num2.num
    
n1=number(4)
n2=number(6) 
sum=n1+n2
print(sum)
mul=n1*n2
print(mul)
 