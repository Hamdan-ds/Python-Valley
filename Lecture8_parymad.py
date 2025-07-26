for x in range(9,0,-1):
	sum = 0
	for y in range(10,x,-1):
		print(" ",end="")
	for z in range(1,x,+1):
		sum += z
		print(z,end=" ")
	print("=",sum,end=" ")
	print("")

for x in range(9,x,-1):
	for y in range(10,x,-1):
		print(" ",end="")
	for z in range(1,x,+1):
		print(x,end=" ")
	print("")

print("     1\n    2 2\n   3 3 3\n  4 4 4 4\n 5 5 5 5 5\n")