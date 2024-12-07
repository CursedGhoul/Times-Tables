num=int(input("Enter the number for the times table: "))

mylist=range(1,11)

for x in mylist:
    ans=x*num
    print(num, "x",x,"=", ans)