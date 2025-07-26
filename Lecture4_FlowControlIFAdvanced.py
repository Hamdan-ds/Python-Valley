a = 100
b = 20
c = 30

# FIND MAX using Logical Operator

if a>b and a>c:
	print("A is MAX")
elif b>a and b>c:
	print("B is MAX")
else:
	print("C is MAX")

# FIND MAX using Nested IF
if a>b:
	if a>c:
		print("A is Greater")
	else:
		print("C is Greater")
elif b>c:
	print("B is Greater")
else:
	print("C is Greater")


print("----------------------------")
#Using input to find max

a = int(input("Enter value of a :"))
b = int(input("Enter value of b :"))
c= int(input("Enter value of c :"))

if a > b and a > c:
	print("A is max")
elif b > a and b > c :
	print("B is max")
else:
	print("C is max")

if a > b:
	if a > c:
		print("A is greater")
	else:
		print("C is greater")
elif b > c :
	print("B is greater")
else:
	print("C is greater")
