# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = input("Введите произвольный текст: ")
count_dot = text.count(".")
count_coma = text.count(",")

if count_dot > count_coma:
    print("Точек тут больше, их ", count_dot)
elif count_dot < count_coma:
    print("Запятых тут больше, их ", count_coma)
else:
    print("Одинаково")
