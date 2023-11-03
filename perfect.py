n=int(input("Enter the number to be checked:"))
sum=0
for i in range(1,n):
  if n%i==0:
    sum=sum+i
if sum==n:
  print("The number",n,"is perfect number")
else:
  print("The number",n,"is  not perfect number")
