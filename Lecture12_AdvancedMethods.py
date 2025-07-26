
def test():
	print("It's a Test Method")
def salary(days,wages):
	netsal = days * wages
	print("Net Salary: ",netsal)

def obtainMarks(marks):
	sum = 0
	for m in marks:
		sum += m
	print("Obtain Marks: ",sum)

# Method Definition - Return Method
def area(length,width):
	totarea = length * width
	# print("Total Area: ",totarea)
	return totarea

def costcalc(area,loc):
	totcost = 0
	if loc == "peshawar":
		totcost = area * 500
	elif loc == "islamabad":
		totcost = area * 1500
	elif loc == "lahore":
		totcost = area * 2500
	return totcost


# Main Method
print("Welcome to the Main Method")

# Method Calling - Zero Parametarized Method
test()

# Method Calling - Parametarized Method
salary(27,200)
stdMarks = [45,12,67,34,89]
obtainMarks(stdMarks)
# Method Calling - Parametarized + Return Method
netArea = area(5,3)
print("NET Area:",netArea)
totcost = costcalc(netArea,"peshawar")
print("Total Area cost:",totcost)
