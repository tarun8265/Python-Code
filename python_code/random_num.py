a = [1,2,3,4]
index=0
count=0
for i in a:

    print(f'index={index}',i)
    print(f'count={count}')
    index+=1
    count+=1

import string
import random

def password_generator(p,n=8):
    print(n)
    if n>=8 and n<=16:
        letter = string.ascii_lowercase
        LETTER = string.ascii_uppercase
        digit = '0123456789'
        symbol = "@#$%"
        string_ = letter+LETTER+digit+symbol

        # password = ''.join(random.sample(string,n))
        password = ''.join(random.sample(string_, n))
        return password
    else:
        return "please enter big digit 8to16"

n = int(input("enter length of password:"))
a = password_generator(1,n)
print(a)








   

























