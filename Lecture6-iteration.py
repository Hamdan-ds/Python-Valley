sum = 0
for x in range(1,11):
	#sum = sum + x
	sum += x
print(sum)

mul = 1
for y in range(1,6):
	#mul = mul * y
     mul *= y
print(mul)

"""
value_1 = 16
for y in range(1,11):
    print(value_1,"x",y,"=",value_1*y)
"""
table = 7
for a in range(1,11):
	print(f"{table} x {a} = {table*a}")

first = 1
second = 0

for a in range(1,11):
	third = first + second
	print(third,end=" ")
	first = second
	second = third
