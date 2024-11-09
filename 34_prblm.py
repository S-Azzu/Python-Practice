class Train:
    def __init__(self, name, fare, seats):
        self.name = name 
        self.fare = fare 
        self.seats = seats 
        
    def getstatus(self):
        print(f"Name of the train is {self.name}")
        print(f"Seats available in the train is {self.seats}")
        print("--------------------------------")
        
    def fareinfo(self):
        print(f"The fare of the train is {self.fare}")
        print("--------------------------------")
        
    def book_ticket(self):
        if self.seats > 0:
            print(f"Your ticket is booked! Your seat number is {self.seats}")
            self.seats -= 1
        else:
            print("Sorry for the inconvenience! The train is full") 

kurnool = Train("Kurnool Express:19888", 100, 300)          
kurnool.getstatus()
kurnool.book_ticket()
kurnool.book_ticket()
kurnool.book_ticket()
kurnool.getstatus()
