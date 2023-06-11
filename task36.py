# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть 
# распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: 
# бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции
# умножения.
# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6]
for i in range(len(a)):
    for j in range(len(b)):
        print(a[i] * b[j], end=' ')
    print()




# def operation (i, j):
#      return i * j
     
# a = [1, 2, 3, 4, 5, 6]
# b = [1, 2, 3, 4, 5, 6]
# print_operation_table = list(map([operation(i, j) for j in range(len(b)) for i in range(len(a))], a, b))
# print(print_operation_table)

