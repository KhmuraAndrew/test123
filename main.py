time=int(input("Введите часы:"))
time1=int(input("Введите минуты:"))
raz=int(input("Введите разницу во времени "))
p=time+raz
if p>=24:
    p-=24
if p<0:
    p+=24
print("Полученное время:",p,":",time1)