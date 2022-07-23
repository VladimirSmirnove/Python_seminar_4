#Вычислить число pi c заданной точностью d Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
d = 0.001
def Diapason(d):
    while 0.0000000001 <= d <= 0.1:
        print (f"d = {d}")
        return(d)
s = str(Diapason(d))
a = abs(s.find('.') - len(s)) - 1
print(f"π = {math.pi:.{a}f}")
