dic={}
n1=int(input("Total number of elements in dict is : "))
for i in range(n1):
    dic[i]=input("Enter element : ")
print("Dictionary in ascending order")
print(sorted(dic.items(), key = lambda kv:(kv[1], kv[0])))
print("Dictionary in descending order")
print(sorted(dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))


