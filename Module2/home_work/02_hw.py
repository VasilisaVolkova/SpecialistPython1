# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

n = int(input("Введите n: "))

if n % 10 == 1:
    print("На лугу пасется ", n, "корова")
elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
    print("На лугу пасется ", n, "коровы")
else:
    print("На лугу пасется ", n, "коров")
