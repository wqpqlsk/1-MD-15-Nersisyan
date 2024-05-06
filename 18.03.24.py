def a1():
    a = int(input("Введите число: "))

    def mod(a):
        if a % 3 == 0:
            return "Число делится на 3"
        else:
            return "Число не делится на 3"

    b = mod(a)
    print(b)
a1()

def a2():
    try:
        a = float(input("Введите число: "))
        b = 100 / a
        print(f"Результат деления на 100: {b}")
    except ValueError:
        print("Ошибка. Введите число")
    except ZeroDivisionError:
        print("Ошибка. Деление на ноль")
a2()

day = int(input("Введите число: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))
def a(day, month, year):
    b = day * month
    if b == int(str(year)[-2:]):
        print("Дата магическая")
    else:
        print("Дата отстой")
print(a(day, month, year))