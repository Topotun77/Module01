my_list = ['apple', 'banana', 'orange', 'kiwi', 'pear']
print("Работа со списками:\nСписок:", my_list)
print("Первый элемент списка:", my_list[0])
print("Последний элемент списка:", my_list[-1])
print("Элементы с 3-го по 5-й включительно:", my_list[2:5])
my_list[2] = "_wildberries_"
print("Измененный список:", my_list)

my_dict = {"one": "один",
           "two": "два",
           "three": "три",
           "four": "четыре",
           "five": "пятый"}
print("\nРабота со словарями:\nСловарь:", my_dict)
print("Перевод слова 'two' -", my_dict["two"])
my_dict["five"] = "пять"
my_dict["six"] = "шесть"
print("Измененный словарь:", my_dict)
