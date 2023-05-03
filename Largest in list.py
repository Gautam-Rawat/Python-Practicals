# WAP to find the maximum of a list of numbers


l=[20,1,15,11,9,26,59,78]

b=max(l)
print(b)

x=l[0]
for i in l:
    if x<i:
        x=i

print("maximum is : ",x)
