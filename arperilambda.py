l=int(input("Enter the Length of Rectangle:"))
b=int(input("Enter the Breadth of Rectangle:"))
area=lambda l1,b1:l1*b1
print("Area of the Rectangle is",area(l,b))
per=lambda l,b:2*(l+b)
print("Perimeter of rectangle is",per(l,b))
a=int(input("Enter length of one side of square:"))
area=lambda a:a*a
print("Area of square is:",area(a))
per=lambda a:4*a
print("Perimeter of square is:",per(a))

