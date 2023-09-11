a=int(input())
b=int(input())
c=int(input())
dis=b**2-4*a*c
if dis>0:
    print("Первый корень =",(-b+dis**0.5)/(2*a))
    print("Второй корень =",(-b-dis**0.5)/(2*a))
elif dis==0:
    print("Корень =",int((-b)/(2*a)))
elif dis<0:
    print("Нет корней")