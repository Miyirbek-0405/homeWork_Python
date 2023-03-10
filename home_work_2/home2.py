
# ===================================== start =======================================

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# 1 - герб, 0 - решка
# Ввод:
# 4 - число монет
# 0
# 1
# 1
# 1
# Вывод:
# 1

# import random
# cout_a = 0
# cout_b = 0
# n = int(input("enter n: "))
# for i in range(n):
#     temp = random.randint(0, 1)
#     print(temp, end=" ")
#     if temp == 1:
#         cout_a += 1
#     else:
#         cout_b += 1
# if cout_a < cout_b:
#     print(cout_a)
# elif cout_b < cout_a:
#     print(cout_b)
# else:
#     print("равно")

# ===================================== end =======================================


# ===================================== start =======================================

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# Ввод:
# 7
# 12
# Вывод
# 3 4 или 4 3

# sum = int(input("enter summa: "))
# mult = int(input("enter multi: "))
# d = sum*sum-4*mult
# if d > 0:
#     x1 = (sum-pow(d, 0.5))//2
#     x2 = (sum+pow(d, 0.5))//2
#     y1 = sum-x1
#     y2 = sum-x2
#     print(f"{x1,y1} или {x2,y2}")
# elif d == 0:
#     x = sum/2
#     y = sum-x
#     print(f"{x,y}")
# else:
#     print("не имеет корней брат)")

# ===================================== end =======================================


# ===================================== start =======================================

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.

# Ввод:
# 6
# Вывод
# 1 2 4
# Ввод
# 24
# Вывод
# 1 2 4 8 16

# num = int(input("enter num: "))
# for i in range(num):
#     if 2**i < num:
#         print(2**i, end=" ")
#     if 2**1 >= num:
#         break

# ===================================== end =======================================
