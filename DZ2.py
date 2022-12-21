# 1 задача
# Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.
nums = int(input("введите число N: "))
numbersInList =1
count =1
table = []
for i in range (1,nums+1):
    numbersInList *=i
    table.append(numbersInList)
print(table)