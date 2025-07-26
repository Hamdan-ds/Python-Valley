class Employee:

	def __init__(self,eSalary,eDesc,eName,eEdu):
		self.__empSalary = eSalary
		self.__empDesc = eDesc
		self.__empName = eName
		self.__empEdu = eEdu

	def setSalary(self,eSalary):
		self.__empSalary = eSalary

	def setDesc(self,eDesc):
		self.__empDesc = eDesc

	def setEdu(self,eEdu):
		self.__empEdu = eEdu

	def getName(self):
		return self.__empName

	def getSalary(self):
		return self.__empSalary

	def getEdu(self):
		return self.__empEdu

	def getDesc(self):
		return self.__empDesc


obj1 = Employee(25000,"Manager","Khalid Khan","BSCS")
print("-------------------------------- Default Values ----------------------------------")
print("Employee Name:",obj1.getName())
print("Employee Description:",obj1.getDesc())
print("Employee Education:",obj1.getEdu())
print("Employee Salary:",obj1.getSalary())


print("-------------------------------- After Updates ----------------------------------")
obj1.setSalary(35000)
obj1.setEdu("MSCS")
print("Employee Name:",obj1.getName())
print("Employee Description:",obj1.getDesc())
print("Employee Education:",obj1.getEdu())
print("Employee Salary:",obj1.getSalary())

print("---"*20)
class Bike:
    def __init__(self, name: str, model: str, company: str):
        self.__bike_name = name
        self.__bike_model = model
        self.__bike_company = company

    @property
    def name(self) -> str:
        return self.__bike_name

    @property
    def model(self) -> str:
        return self.__bike_model

    @property
    def company(self) -> str:
        return self.__bike_company

class Data(Bike):
    def __init__(self, color: str, engine: str, price: float, name: str, model: str, company: str):
        super().__init__(name, model, company)
        self.__bike_color = color
        self.__bike_engine = engine
        self.__bike_price = price

    @property
    def color(self) -> str:
        return self.__bike_color

    @color.setter
    def color(self, new_color: str):
        self.__bike_color = new_color

    @property
    def engine(self) -> str:
        return self.__bike_engine

    @property
    def price(self) -> float:
        return self.__bike_price

    @price.setter
    def price(self, new_price: float):
        self.__bike_price = new_price

    def __str__(self) -> str:
        return (f"Bike Details:\n"
                f"  Name    : {self.name}\n"
                f"  Model   : {self.model}\n"
                f"  Company : {self.company}\n"
                f"  Color   : {self.color}\n"
                f"  Engine  : {self.engine}\n"
                f"  Price   : {self.price}")

# Creating an object
bike1 = Data("Red", "1000cc", 159999, "Honda125", "G54", "Honda")

# Using __str__ method for clean output
print(bike1)

# Updating bike color
bike1.color = "Black"
print("\nAfter Updating Color:")
print(bike1)