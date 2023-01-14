massive_corr=list(map(int,input("Введите последовательность чисел через пробел: ").split()))
number=int(input("Введите любое число: "))
print("Неотсортированный массив: ",massive_corr)
def sort(massive_corr):
    for i in range(len(massive_corr)):
        for j in range(len(massive_corr) - i - 1):
            if massive_corr[j] > massive_corr[j + 1]:
                massive_corr[j], massive_corr[j + 1] = massive_corr[j + 1], massive_corr[j]
    return massive_corr


def binary_search(massive_corr, number, left, right):
    if number <= min(massive_corr):
        x=print("Вы ввели число меньше минимального из списка")
    elif number > max(massive_corr):
        x=print("Вы ввели число превышающее максимальное из списка")
    else:
        middle = (right + left) // 2  # находим середину
        if massive_corr[middle] >= number and massive_corr[middle-1] <number:  # если элемент в середине,
            return middle-1  # возвращаем этот индекс
        elif number < massive_corr[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
            return binary_search(massive_corr, number, left, middle - 1)
        else:  # иначе в правой
            return binary_search(massive_corr, number, middle + 1, right)

print("Отсортированный массив: ",sort(massive_corr))

if binary_search(massive_corr, number, 0, len(massive_corr)-1) is None:
    print("Ваше число не удовлетворяет требованиям")
else: print("Номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу: ",binary_search(massive_corr, number, 0, len(massive_corr)-1))



