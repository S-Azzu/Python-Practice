sub1=int(input("enter your sub1  marks\n"))
sub2=int(input("enter your sub2 marks\n"))
sub3=int(input("enter your sub3 marks\n"))
if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail")

elif(sub1+sub2+sub3)/3<40:
    print("you are fail") 
else:
    print("congatulations!you are pass")   