# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

a = [float(i) for i in input('Введите список из нескольких вещественных чисел через пробел: ').split()]

a_fraction = [round((a[i] - int(a[i])), 2) for i in range(len(a)) if a[i] - int(a[i]) != 0]

print(max(a_fraction) - min(a_fraction))