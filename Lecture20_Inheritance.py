class Bank:
	def __init__(self,bTitle,bLocation,bStatus):
		self.bankTitle = bTitle
		self.bankLocation = bLocation
		self.bankStatus = bStatus

	def test(self):
		print("IT's a Parent Class Test Method")
	def getTitle(self):
		return self.bankTitle

	def getLocation(self):
		return self.bankLocation

	def getStatus(self):
		return self.bankStatus


class Branch(Bank):
	def __init__(self,bTitle,bLocation,bStatus,pName,pAccount,pOBL):
		super().__init__(bTitle,bLocation,bStatus)
		self.personName = pName
		self.personAccount = pAccount
		self.personOBL = pOBL

	def getName(self):
		return self.personName

	def getAccount(self):
		return self.personAccount

	def getOBL(self):
		return self.personOBL

	def Work(self):
		print("IT's a Child class Work Method")

obj1 = Branch("Meezan","Saddar Cantt","Islamic","Khalid Khan","Saving",15000)
print("Bank Title:",obj1.getTitle())
print("Bank Location:",obj1.getLocation())
print("Bank Status:",obj1.getStatus())
print("Person Name:",obj1.getName())
print("Person Account:",obj1.getAccount())
print("Person Opening Balance:",obj1.getOBL())
obj1.test()
obj1.Work()