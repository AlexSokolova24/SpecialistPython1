# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Введите 1-е число: "))
second_number = int(input("Введите 2-е число: "))
my_list = []
new_list = []
el = first_number
while el <= second_number:
    my_list.append(el)
    el += 1
for numbers in my_list:
    if numbers % 3 == 0:
        new_list.append(numbers)
print(new_list)


# TODO: your code here
