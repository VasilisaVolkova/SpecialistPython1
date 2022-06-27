def my_abs(a):
    if a > 0:
        return a
    elif a < 0:
        a = -a
        return a
    else:
        return 0


print(my_abs(-5))
print(my_abs(5))
print(my_abs(0))
