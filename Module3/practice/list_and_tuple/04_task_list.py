# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

list_n = [-10, -3, -2, 10, 3, 4, -8]
summ = 0

for numbers in list_n:
    if numbers > 0:
        summ += numbers
print(summ)
