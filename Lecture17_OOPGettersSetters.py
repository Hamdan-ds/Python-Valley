class Employee:

	def __init__(self,eSalary,eDesc,eName,eEdu):
		self.empSalary = eSalary
		self.empDesc = eDesc
		self.empName = eName
		self.empEdu = eEdu

	def setSalary(self,eSalary):
		self.empSalary = eSalary

	def setDesc(self,eDesc):
		self.empDesc = eDesc

	def setEdu(self,eEdu):
		self.empEdu = eEdu

	def getName(self):
		return self.empName

	def getSalary(self):
		return self.empSalary

	def getEdu(self):
		return self.empEdu

	def getDesc(self):
		return self.empDesc


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
