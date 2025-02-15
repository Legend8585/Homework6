# Практическое задание по теме: "Словари и множества"
# Цель: Написать программу на языке Python, используя Pycharm, для работы со словарями и множествами.
# 1. В проекте, где вы решаете домашние задания, создайте модуль 'homework6.py' и напишите весь код в нём.
# 2. Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
my_dict = {'Nuriddin' : 1985, 'Anton' : 1984, 'Sasha' : 1986, 'Jenya' : 1995}
#   - Выведите на экран словарь my_dict.
print(my_dict)
#   - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
print(my_dict.get('Nuriddin'))
print(my_dict.get('Denis'))
#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict.update({'Dinara' : 1990})
my_dict['Katya'] = 1988
#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
a = my_dict.pop('Sasha')
print(a)
#   - Выведите на экран словарь my_dict.
print(my_dict)
# 3. Работа с множествами:
#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
my_set = {1,2,3,3,2,1,'a', 'up',"a"}
#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
print(my_set)
#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.add(5)
my_set.add(6)
#   - Удалите один любой элемент из множества my_set.
my_set.remove('up')
#   - Выведите на экран измененное множество my_set.
print(my_set)