a=int(input("enter the first number"))
b=int(input("enter the second number"))
x=1

for i in range(1,min(a,b)+1):
      if a%i==0 and b%i==0:
        x=i
print("the G.C.D og two number is:",x)
