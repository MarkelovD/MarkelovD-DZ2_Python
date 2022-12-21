# 1 задача
# Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.
# nums = int(input("введите число N: "))
# numbersInList =1
# count =1
# table = []
# for i in range (1,nums+1):
#     numbersInList *=i
#     table.append(numbersInList)
# print(table)

# 2 задача
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# a = float(input("введите вещественное число: "))
# sum = 0
# for i in str(a):
#     if i != ".":
#         sum+=int(i)
# print(sum)

#3 задача
# задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# nums = int(input("введие число: "))
# sumLibrary = 0
# library = {}
# for i in range(1, nums+1):
#     library[i] = round(((1+1/i)**i),2)
#     sumLibrary += library[i]
# print(library)
# print(round(sumLibrary,2))

# 4 задача
# алгоритм перемешивания 

import datetime
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def random_position(max_znach):
    random_nums = datetime.datetime.now().microsecond/10**6 #случайный множитель зависит от времени
    return random_nums*max_znach # получение случайного индеска из списка

for i in range(len(a)-1,-1,-1):
    j= int(random_position(i+1))
    a[i],a[j] = a[j],a[i]
print(a)