#WAP program linear search

l=[]
n=int(input("Enter Total number of elements in your list"))

for i in range(0,n):
    l.append(int(input("Enter your {} element".format(i+1))))

a=int(input("Enter a number to find in the list"))

for i in range(n):
    if a==l[i]:
        print("Element Found at index number: ",i)
        break
    
else:
    print("Element not found ")
