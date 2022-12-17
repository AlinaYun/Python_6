# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def generate_list(number_of_elements):
    return [randint(0, 100) for i in range (number_of_elements)]

def sum_odd_index(input_list):
    result = 0
    for index, value in enumerate (input_list):
        if index % 2 != 0:
            result += input_list[index]
    return result

number_of_elements = int(input("Введите число элементов в списке: "))
my_list = generate_list(number_of_elements)
print(my_list)
print (sum_odd_index(my_list))