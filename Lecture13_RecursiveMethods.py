
def sumIteration(num):
	sum = 0
	for x in range(1,11):
		sum += x

	return sum

def sumRecursion(num):
	if num == 0:
		return num
	else:
		return num + sumRecursion(num - 1) # 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1


def factIteration(num):
	fact = 1
	for x in range(1,6):
		fact *= x

	return fact

def factRecursion(num):
	if num == 1:
		return num
	else:
		return num * factRecursion(num - 1) # 5 * 4 * 3 * 2 * 1

# Main Method
print(sumIteration(10))
print(sumRecursion(10))

print(factIteration(5))
print(factRecursion(5))

def sum_iteration(num):
	sum = 0
	for add_val in range(1,num + 1):
		sum += add_val
	return sum
print(sum_iteration(10))

def sum_recursion(num):
	if num == 0 :
		return 1
	else:
		return num + sum_iteration(num - 1)
print(sum_recursion(10))