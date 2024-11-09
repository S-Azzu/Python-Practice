num = int(input("enter your number: "))
prime=True
for i in range(2,num):
    if(num%i==0):
        break
        prime=False
if prime:
    print("this number is prime number ")
else:
    print("this is not a prime number")


