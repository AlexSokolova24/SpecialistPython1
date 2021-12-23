# Дан словарь, содержащий данные о товаре из магазина
# "price" - цена товара в валюте "currency"
# "count" - количествотовара в магазине
# Считая,что курс доллара равен dollar_rate
# Вычислите цену всех товаров с названием "name" в долларах

item = {
    "name": "Кроссовки",
    "price": "7500",
    "currency": "rub",
    "count": "10",
}

price = int(item["price"])
count = int(item["count"])
dollar_rate = 74.12
summ_all_item = price * count
summ_in_dollar = summ_all_item/dollar_rate
print(summ_in_dollar)

# TODO: your code here
