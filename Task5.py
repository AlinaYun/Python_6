# ДОПОЛНИТЕЛЬНО, НО НЕОБЯЗАТЕЛЬНО:
# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

from random import randint

# - создает список из рандомных четырех значных чисел
def create_list (number_of_elem):
    return [randint(1000, 10000) for i in range (number_of_elem)]

# - принимает с консоли цифру и удаляет ее из всех элементов списка
def delete_digit(input_list, number_to_delete):
    return list(filter(lambda x: x != number_to_delete, input_list))

# - цифры каждого элемента суммирует пока результат не станет однозначным числом
def replace_element(list):
    for i in range(len(list)):
        while list[i] > 9:
            list[i] = sum_digits(list[i])
    return list 

def sum_digits(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_digits(number//10)

# - из финального списка убирает все дублирующиеся элементы

def delete_duplecates(input_list):
    return list(set(input_list))

my_list = create_list(int(input("Введите количество элементов в списке: ")))
print(my_list)
number_to_delete = int(input("Введите число: "))
new_list = delete_digit(my_list, number_to_delete)
print(new_list)
new_list = replace_element(new_list)
print(new_list)
new_list = delete_duplecates(new_list)
print(new_list)