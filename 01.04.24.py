def a1():
    str = {"Россия": "Москва", "Нидерланды": "Амстердам", "Франция": "Париж", "Швейцария": "Берн"}
    for key in str:
        print(key, str[key])

        print(str["Россия"])
        a = list(str.keys())
        a.sort()
        for n in a:
            print(n, ":", str[n])
a1()

print("задание 2")
def a2():
    a = 0
    b = input("Введите слово: ")
    v = {"А": 1, "В": 1, "Е": 1, "И": 1, "Н": 1, "О": 1, "Р": 1, "С": 1, "Т": 1, "Д": 2, "К": 2, "Л": 2, "М": 2, "П": 2,
         "У": 2, "Б": 3, "Г": 3, "Ё": 3, "Ь": 3, "Я": 3, "Й": 4, "Ы": 4, "Ж": 5, "З": 5, "Х": 5, "Ц": 5, "Ч": 5, "Ш": 8,
         "Э": 8, "Ю": 8, "Ф": 10, "Щ": 10, "Ъ": 10}
    for n in b:
        for key in v:
            if n in key:
                a += (v.get(key))
    print(a)
a2()