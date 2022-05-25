# ЗАДАНИЕ_1
# Создать репозиторий для решения задачи.
# Для решения создать 3 ветки.
# В первой ветке решение 1-3 задачи, в второй 4-6, в третьей - 7-10.
# Отправить мне. После одобрения вливать в main при помощи пулл-реквестов.

# У вас имеется словарь my_dict:

my_list = [42, 43]
my_dict = {
	'foo': {
		'a':12,
		'b': (1, 2, 3, 4, my_list)
	},
	'bar': {
		'c':12,
		'd': {5, 6, 7, 8}
	},
	'moo': {
		'e':12,
		'f': {'Lol': ['L', 'o', 'l']}
	},
}

# 1. Выведите на консоль значение ключа ‘foo’.
print(my_dict['foo'])
# 2. Выведите на консоль значение ключа ‘b’.
print(my_dict['foo']['b'])
# 3. Добавьте в my_list 44.
my_list.append('44')

# Снова выведите на консоль значение ключа ‘b’.
print(my_dict['foo']['b'])
# Выведите множество.
d = set(my_dict)
print(d)
# Добавьте в множество элемент 9.
d.update('9')
