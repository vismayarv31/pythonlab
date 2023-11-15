student={}
n=int(input("Enter the number of students :"))
for i in range(0,n):
 name=input("Enter the name :")
 age=int(input("Enter the age :"))
 grade=input("Enter the grade :")
 student[name]=age,grade
 print("List of students : ",student)
