#Nested Dictionary

std_info = {"Ali":[45,56,67,12],"Kashif":[56,23,78,32],"Jamal":[78,56,34,89],"Farman":[67,45,89,78]}
# std_status = {"Ali":"B","Kashif":"C","Jamal":"A","Farman":"C"}
for names in std_info:
	print(names,end=" ")
	# print(std_info[names])
	# print(sum(std_info[names]))
	sum = 0
	for m in std_info[names]:
		print(m,end=" ")
		sum += m
	print(sum,end=" ")
	percent = sum/400 * 100
	print(percent)
