#Задайте последовательность чисел. Напишите программу, 
#которая выведет список неповторяющихся элементов исходной последовательности.

numbers = [20, 15, 30, 30, 40, 15]
def number_uniq(numbers):
    list_uniq = []

    for number in numbers:
        if number in list_uniq:
            continue
        else:
            list_uniq.append(number)
    return list_uniq
print(f"Список: {numbers}")
print(f"Измененный список: {number_uniq(numbers)}")