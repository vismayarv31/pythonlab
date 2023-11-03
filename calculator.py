def calculator(n1,operator,n2):
   if operator =="+":
      return add(n1, n2)

   elif operator == "-":
      return sub(n1, n2)

   elif operator == "*":
      return multi(n1, n2)    
   elif operator == "/":
      return  div(n1, n2)
   elif operator == "**":
      return po(n1,n2)    
   else:
       print("Invalid Operator")
    
def add(n1, n2):
   return n1 + n2
def sub(n1, n2):
   return n1 - n2
def multi(n1, n2):
   return n1 * n2
def div(n1, n2):
   return n1 / n2    
def po(n1,n2):
   return n1 ** n2
n1 = int(input("Enter the First Number:"))
n2 = int(input("Enter the Second Number: "))
operator=input("Enter the operation to be performed:+,-,*,/,**: ")
print(calculator(n1,operator,n2))
