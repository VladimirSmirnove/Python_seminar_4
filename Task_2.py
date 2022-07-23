# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def Factor(n):
    My_list = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            My_list.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        My_list.append(n)
    return My_list
print(Factor(int(input("Введите натуральное число: "))))
