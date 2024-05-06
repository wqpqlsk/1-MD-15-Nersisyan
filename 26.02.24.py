def a1():
    a = int(input("Введите количество слов: "))
    r = ""
    for i in range(a):
        n = input("Введите слово: ")
        r += n + " "
        print(r)
a1()

def a2():
    r = ""
    while True:
        a = input("Введите слово: ")
        if a == "стоп":
            break
        r += a + " "
    print(r)
a2()

def a3():
    a = input("Введите слово: ")
    if "ф" in a:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")
a3()

def a4():
    from random import randint
    oshibk = 0
    prav = 0
    while oshibk < 3:
        a1 = randint(1, 10)
        b1 = randint(1, 10)
        summ = int(input(f"Сумма {a1} + {b1}: "))
    if summ == a1 + b1:
        print("Правильно!")
        prav += 1
    else:
        oshibk += 1
        print("Ответ неверный")
    print("Игра окончена. Правильных ответов: ", prav)
a4()