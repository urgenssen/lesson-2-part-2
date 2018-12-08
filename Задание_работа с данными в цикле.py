# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print (name)
# ???


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print (name + " " + str(len(name)))
# ???


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for key in is_male:
    sex = is_male.get(key)
    if sex == True:
        print (key + " male")
    else:
        print (key + " female")


# ???


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

value_groups = len(groups)
print ("Всего " + str(value_groups) + " группы")
for group in groups:
    value_group = len(group)
    print ("В группе " + str(value_group) + " ученика")


# ???


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша', "Маша"],
  ['Оля', 'Петя', 'Гриша', 'Оля', 'Семён'],
]
number = 0
value = 0
for group in groups:
    string = ''
    number += 1
    for name in group:
        string = string + name + ", "
        value +=1
        if value == len(group):
            string = string[0:-2]
            value = 0
            break
# ', '.join(['abc', 'def'])
    
    print(f"Группа {number}: {string}")

groups = [
  ['Вася', 'Маша', "Маша"],
  ['Оля', 'Петя', 'Гриша', 'Оля', 'Семён'],
]
number = 0
for group in groups:
    string = ''
    number += 1
    print (f"Группа {number}:", ', '.join(group))
    


# ???