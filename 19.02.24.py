def a1():
    parol = input("Введите пароль: ")
    parol1 = input("Повторите пароль: ")
    if parol == parol1:
        print("Пароль принят")
    else:
        print("Пароль не принят")
a1()

def a2():
    n = int(input("Введите номер места в плацкартном вагоне: "))
    if n > 36:
        print("боковое")
    else:
        print("купе")
    a = n
    if a % 2:
        print("нижнее")
    else:
        print("верхнее")
a2()

def a3():
    a = int(input("Введите год: "))
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        print("Год ", a, " - високосный")
    else:
        print("Это год не високосный")
a3()

def a4():
    n = int(input("Выберите цвет: '1' - красный, '2' - синий,'3' - желтый: "))
    n1 = int(input("Выберите цвет:  '1' - красный,' 2' - синий, '3' - желтый: "))
    if n == 1 and n1 == 2 or n == 2 and n1 == 1:
        print("Получился фиолетовый")
    elif n == 1 and n1 == 3 or n == 3 and n1 == 1:
        print("Получился оранжевый")
    elif n == 2 and n1 == 3 or n == 3 and n1 == 2:
        print("Получился зеленый")
    else:
        print("Ошибка")
a4()
