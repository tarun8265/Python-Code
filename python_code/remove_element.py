a = []
n = int(input("enter number of element:"))
for i in range(n):
    a.append(int(input('enter element:')))
print("old list:",a)
new = list(set(a))
print("remove_duplicate element:",new)    
new.sort(reverse=True)
print("asending order:",new)



a = []
n = int(input("enter number of element:"))
for i in range(n):
    a.append(int(input('enter element:')))
print("old list:",a)
new = set(a)
print(new)