# Дан список. Вывести элементы списка, пронумеровав их начиная с единицы.
# Каждый элемент должен быть выведен с новой строки.

fruits = ["яблоко", "банан", "киви", "ананас", "груша", "персик"]
number = 0

for list_fruits in fruits:
    number += 1
    print(number, list_fruits)
