import math

i=int(1)
e=float(2.71828182)
print("Ingrese X, sera calculado (x+x^2/2+...x^n/n) hasta que de menos de 0.00001")
x=int(input())
while(x**i/math.factorial(i)>0.000001): i+=1
e+=e+x**i/math.factorial(i)
print("e elevado a ",x,"equivale",e)
