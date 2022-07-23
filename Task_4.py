# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = 2
def cooficent_1(a):
    a = random.randint(0,100)
    return a
a = cooficent_1(1)
def cooficent_2(b):
    b = random.randint(0,100)
    return b
b = cooficent_2(2)
def cooficent_2(c):
    c = random.randint(0,100)
    return c
c = cooficent_2(3)
f=open('file.txt','w')
f.write(str(f"{a} + {b}*x^{k} + {c} = 0"))
f.close()
print(f"{a} + {b}*x^{k} + {c} = 0")