# 2 Задайте натуральное число N.
#  Напишите программу, которая составит список простых множителей числа N.
 

n = int(input("Введите число: "))
n_list = []
x = 2 
while x <= n:
    if n % x == 0:
        n_list.append(x)
        n //= x
    else:
        x += 1
print(f"Простые множители числа -> {n_list}")

