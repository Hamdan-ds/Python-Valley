ali_math_marks = 55
ali_comp_marks = 64
ali_urdu_marks = 23
ali_phys_marks = 78
ali_chem_marks = 34

ali_marks = [55,64,23,78,34]

print(ali_marks)

for x in range(0,5):
	print(ali_marks[x])

for x in range(0,5):
	if ali_marks[x]>=40:
		print("PASS")
	else:
		print("FAIL")

sum = 0
for x in ali_marks:
	sum += x

print("Obtain Marks: ",sum)

pass_list = []
fail_list = []

for x in ali_marks:
	if x>=40:
		pass_list.append(x)
	else:
		fail_list.append(x)

print("PASS Papers:",pass_list)
print("Fail Papers:",fail_list)

papers = ["Math","Computer","Urdu","Physics","Chemistry"]
for x in range(len(papers)):
	print(papers[x]," - ",ali_marks[x])

dictonery = zip(papers,ali_marks)
print(dict(dictonery))

dict1 = dict(paper=papers,marks=ali_marks)
print(dict1)

hamdan = ["english","urdu","math"]
# hamdan.append("biology")                             #adding only one argument
hamdan.extend(["physics","computer science","pak study"])              # adding multiple arguments
print(hamdan)

fahad = [20,33,1,23]
fahad[2] = 100
print(fahad)