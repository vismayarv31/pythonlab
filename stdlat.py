days=int(input("Number of Total Days:"))
n=int(input("Enter the number of students:"))
student_list=[]
for i in range (0,n):
	name=input("Name of the Student:")
	attendance=int(input("Attendance of the Student:"))
	percentage=((attendance/days)*100)
	student_list.append((name,percentage))
student_list.sort()
print(student_list)

for i in student_list:
	print(i[0],i[1],"%")	
