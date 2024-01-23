
number = [1,2,3,4,5,6]
valid_list = []
if len(number) <= 1:
    print('Enter valid list!')
else:
    response = len(number)//2
    data = number[::-1]
    data = data[:response]
    valid_list.extend(number[:response+1])
    valid_list.extend(data)
    print(valid_list)

