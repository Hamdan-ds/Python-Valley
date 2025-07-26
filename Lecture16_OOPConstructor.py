#OOP CONSTRUCTOR
class Bike:

	def __init__(self,bColor,bPrice,bGears,bSeats):
		self.bikeColor = bColor
		self.bikePrice = bPrice
		self.bikeGears = bGears
		self.bikeSeats = bSeats



print("First Object Parameters")
obj1 = Bike("Black",15000,5,1)
print("Bike Color:",obj1.bikeColor)
print("Bike Price:",obj1.bikePrice)
print("Bike Seats:",obj1.bikeSeats)
print("Bike Gears:",obj1.bikeGears)

print("Second Object Parameters")
obj2 = Bike("Red",25000,6,2)
print("Bike Color:",obj2.bikeColor)
print("Bike Price:",obj2.bikePrice)
print("Bike Seats:",obj2.bikeSeats)
print("Bike Gears:",obj2.bikeGears)



class Bike:
    def __init__(self, bColor, bPrice, bGears, bSeats):
        self.bikeColor = bColor
        self.bikePrice = bPrice
        self.bikeGears = bGears
        self.bikeSeats = bSeats

    def show_details(self):
        print(f"Bike Color: {self.bikeColor}")
        print(f"Bike Price: {self.bikePrice}")
        print(f"Bike Gears: {self.bikeGears}")
        print(f"Bike Seats: {self.bikeSeats}")

print("First Object Parameters")
obj1 = Bike("Black", 15000, 5, 1)
obj1.show_details()

print("\nSecond Object Parameters")
obj2 = Bike("Red", 25000, 6, 2)
obj2.show_details()
