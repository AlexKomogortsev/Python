# Task 6

a = int(input('Напишите сколько км спортсмен пробежал в первый день:'))
b = int(input('Напишите сколько км итого спортсмен должен пробежать:'))
i = 1

while a <= b:
    a = float(a * 1.1)
    i = i + 1
print('на %d-й день спортсмен достиг результата - не менее %d км' % (i, b))

input('Введите Enter')