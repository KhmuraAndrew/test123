#Задание 1
#x=int(input("Введите число:"))
#n=0
#for i in range (0,x+1):
#    n=n+i
#print(n)


#Задание 2
#a=int(input("Введите число:"))
#for i in range(0,a+1):
#    if i%2>0:
#        print(" ", end="")
#    else:
#        print(i, end="")

#Задание 3
#x=int(input("Введите число:"))
#n=1
#for i in range (1,x+1):
#    n=n*i
#print(n)

#Задание 4
#x=int(input("Введите число:"))
#n=1
#for i in range (0,11):
#    s=x*i
#    print(x,"*",i,"=",s)

#Задание 5
#x=int(input("Введите число:"))
#b=int(input("Введите число:"))
#a=int(input("Введите число:"))

#if a>b and a>x:
#    print(a)
#elif b>a and b>x:
#    print(b)
#else:
#    print(x)

#Задание 7
#a=int(input("введите число"))
#summ=(a//1000)%10+((a//100)%10)+((a%100)//10)+a%10
#print(summ)

#Задание6
#a=int(input("введите число"))
#if a%2==0 or a%3==0 or a%5==0:
#    print(a,"-не простое число")
#elif a%2>0 or a%3>=0 or a%5>=0:
#    print(a,"-простое число")

#Задание 8
a=int(input("введите число"))
digit=a%10
a2=digit
a=a//10
while a>0:
    digit=a%10
    a=a//10
    a2=a2*10
    a2=a+digit
print(a2)


