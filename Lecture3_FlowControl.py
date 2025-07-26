#Calculator

val1 = int(input("Enter first value:"))
val2 = int(input("Enter second value:"))

choice = input("Enter your choice (+,-,*,/)")

if choice == '+':
	sum = val1 + val2
	print("SUM of val1 & val2:",sum)
elif choice == '-':
	sub = val1 - val2
	print("SUB of val1 & val2:",sub)
elif choice == '*':
	mul = val1 * val2
	print("MUL of val1 & val2:",mul)
elif choice == '/':
	div = val1 / val2
	print("DIV of val1 & val2:",div)
else:
	print("Invalid choice entered...Enter a valid choice")
