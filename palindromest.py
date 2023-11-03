def is_palindrome(n):
 n_str=str(n)
 n_rev=n_str[::-1]
 if n_str==n_rev:
  return True
 return False
n=str(input("Enter a string:"))
result=is_palindrome(n)
if(result==True):
  print("The string is palindrome")
else:
  print("The string is not palindrome")
