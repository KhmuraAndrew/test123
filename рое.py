import string
import random
k=int(input("Введите колличество паролей:"))
d=int(input("Введите длинну пароля:"))
s=int(input("Введите сложность пароля [1-3]:"))
a=""
if s==1:
    a=string.ascii_lowercase
elif s==2:
    a=string.ascii_lowercase+string.digits
elif s==3:
    a=string.ascii_letters+string.digits+string.punctuation
r=""
for _ in range(k):
    r = ""
    for i in range(d):
        r+= random.choice(a)
    print("Ваш пароль",r)
