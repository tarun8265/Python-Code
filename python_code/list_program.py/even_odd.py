a = []
n = int(input("enter number of element:"))
for i in range(n):
    a.append(int(input("enter element:")))
    print(a) 
even = 0
odd = 0
for j in a:
    if a%2==0:
        even+=1
    else:
        odd+=1

print("even number:",even) 
print("odd number:",odd)          


