class Train:
    def __init__(self,name,Fare,seats):
       self.name=name 
       self.fare=Fare 
       self.seats=seats 
    def getstatus(self):
        print(f"Name of the Train is {self.name}")
        print(f"Seats available in a Train is {self.seats}")
        print("--------------------------------")
    def fareinfo(self):
        print(f"The fare of the Train is {self.fare}")
        print("--------------------------------")
    def Bookticket(self):
        if(self.seats>0):
            print(f"your ticket is booked!your seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("sorry for the inconvience!The train is full") 
kurnool=Train("kurnoolExpress:19888",100,300)          
kurnool.getstatus()
kurnool.Bookticket()
kurnool.Bookticket()
kurnool.Bookticket()
kurnool.getstatus()
    