list = [1,2,3,4,5]
# n = []
# add = 0    
# for i in list:
#     n.append(add+i)
#     add += i
# print(n)

n = [sum(list[:i+1]) for i in range(len(list))]
print(n)


