for x in range(1,6):
	for y in range(1,6):
		print(y,end=" ")
	print("")
print("-----------------------------------------------------")
for x in range(1,6):
	for y in range(1,6):
		print(x,end=" ")
	print("")
print("----------------------h-------------------------------")
for x in range(1,6):
	for y in range(1,x+1):
		print(x,end=" ")
	print("")
print("-----------------------------------------------------")
for x in range(1,6):
	for y in range(1,x+1):
		print(y,end=" ")
	print("")
print("-----------------------------------------------------")
for x in range(1,6):
	for y in range(1,x+1):
		print("*",end=" ")
	print("")
print("-----------------------------------------------------")
for x in range(1,11):
	for y in range(10,x-1):
		print(" ",end="")
	for z in range(1,x+1):
		print("-",end=" ")
	print("")
print("_________________________________________________________")
for x in range(1,11):
	for y in range(10,x,-1):
		print(" ",end="")
	for z in range(1,x+1):
		print("o",end=" ")
	print("")

for x in range(10,0,-1):
	for y in range(10,x,-1):
		print(" ",end="")

	for z in range(1,x+1):
		print("*",end=" ")
	print("")

print("----------------------------------------------------------")