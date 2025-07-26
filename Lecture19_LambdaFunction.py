#Lambda Function
def test():
	print("Welcome to ITSAWK")


# Main Method
test()

mymethod = lambda : print("Welcome to Python Class")
mymethod()

methodparam = lambda x: print("Value of X:",x)
methodparam(5)

methodSUM = lambda x,y: x+y
print(methodSUM(5,3))

methodSalary = lambda days,wages: days * wages
print(methodSalary(25,100))

stdNames = ["Asad","Jamshed","Farooq","Wajid"]
addKhanay = list(map(lambda x:x+" Khan",stdNames))
print(addKhanay)

stdMarks = [25,45,56,67]
newMarks = list(map(lambda m:m+5,stdMarks))
print(newMarks)

aliMarks = [67,23,90,34,87]
# passMarks = list(filter(checkMarks(),aliMarks))
passMarks = list(filter(lambda m:m>40,aliMarks))
print(passMarks)

students = ["Khalid Khan","Fahim Shah","Zubair Nawaz","Shahid Aslam","Munawar Bilal"]
fNames = list(map(lambda n:n.split(" ")[0].upper(),students))
print(fNames)


students = ["Khalid Khan","Fahim Shah","Zubair Nawaz","Shahid Aslam","Munawar Bilal"]
