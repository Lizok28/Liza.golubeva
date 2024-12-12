import matplotlib.pyplot as plt
import math


def f(x):
    return x - 2 * math.e ** (-2) #Вводим функцию


x = []
y = []


a = int(input('Введите a: '))
b = int(input('Введите b: '))  #Вводим данные
e = float(input('Введите e: '))


for i in range(a, b+1):
    x.append(i)
    y.append(f(i))

x0 = []
y0 = []
for i in range(a, b+1):
    x0.append(i)
    y0.append(0)
pip = 1
while abs(b-a)>= e:
    c = (a+b)/2
    if f(a)*f(c)<=0:
        b = c
    else:
        a = c
    plt.text(c, f(c), str(pip), color='purple', fontsize=12)
    pip += 1


print('Приблизительный корень =', c)


plt.plot(x,y, color='pink', marker='o')
plt.plot(x0,y0, color='black')
plt.show()