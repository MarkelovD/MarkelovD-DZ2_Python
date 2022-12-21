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

nums = int(input("введие число: "))
sumLibrary = 0
library = {}
for i in range(1, nums+1):
    library[i] = round(((1+1/i)**i),2)
    sumLibrary += library[i]
print(library)
print(round(sumLibrary,2))
