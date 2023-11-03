num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
operation=input("Choose an arithematic operation(+,-,*,/,** for exponention,// for floor division and % for modulo):")
if operation=="+":
   result=num1+num2
elif operation=="-":
   result=num1-num2  
elif operation=="*":
   result=num1*num2 
elif operation=="/":
   result=num1/num2
elif operation=="**":
   result=num1**num2
elif operation=="//":
   result=num1//num2
elif operation=="%":
   result=num1%num2
else:
   print("Invalid input")
print("The result of arithematic operation is:",result)
   
