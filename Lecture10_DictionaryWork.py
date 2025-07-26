ali_math_marks = 54
ali_urdu_marks = 43
ali_comp_marks = 32
ali_phys_marks = 67
ali_chem_marks = 23

ali_marks = [54,43,32,67,23]

ali_papers = {"math":54,"urdu":43,"computer":32,"physics":67,"chemistry":23}

print(ali_papers)

for x in ali_papers:
	print(x," - ",ali_papers[x])

sum = 0
for t in ali_papers:
	sum += ali_papers[t]

print("Ali total marks:",sum)

ali_subjects = []
ali_pmarks = []

counter = 0
for x in ali_papers:

	ali_subjects.append(x)
	m = ali_papers[x]
	ali_pmarks.append(m)

print(ali_subjects)
print(ali_pmarks)

max = 0
min = float('inf')
minimum = 0
for x in ali_papers:
	if ali_papers[x] > max:
		max = ali_papers[x]
	elif ali_papers[x] < min:
		min = ali_papers[x]
print(max)
print(min)

print("-----------------<(*)>-------------------")
ali_status = {}

for x in ali_papers:
	if ali_papers[x] >= 40:
		ali_status[x] = "PASS"
	else:
		ali_status[x] = "FAIL"
print(ali_status)

paper = list(ali_papers.keys())
marks = list(ali_papers.values())

print(paper)
print(marks)