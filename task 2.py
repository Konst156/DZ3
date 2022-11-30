# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_data = [int(i) for i in input('Введите список из нескольких чисел через пробел: ').split()]
if len(list_data) % 2 == 0:
    list_mp = [list_data[i] * list_data[-i-1] for i in range(int(len(list_data)/2))]
else:
    list_mp = [list_data[i] * list_data[-i-1] for i in range(int(len(list_data)/2+1))]
print(list_mp)