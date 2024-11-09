def  digit(num1,num2,num3):
     if(num1>num2):
          if(num1>num3):
             return num1
          else:
             return num3
     else:
         if(num2>num3):
               return num2
         else:
               return num3
m=digit(2,3,96)
print("the value of greater digit is "+str(m))
     
    

      