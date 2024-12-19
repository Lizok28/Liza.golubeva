import math


def f(x):
   return math.sin(x)


a = float(input('Введите a: '))
b = float(input('Введите b: '))  #Вводим данные
n = int(input('Введите n: '))
h = (b-a)/n #Расчитываем h


lol = 0


for i in range(n):
   lol += f(a+h*i)
print('Методом левых прямоугольников =', h*lol)


lol = 0


for i in range(n):
   lol += f(a+h*(i+1))
print('Методом правых прямоугольников =', h*lol)


lol = 0


for i in range(1, n):
   lol += f(a+i*h)
print('Методом трапеции =', h*(f(a)/2 + f(b)/2 + lol))