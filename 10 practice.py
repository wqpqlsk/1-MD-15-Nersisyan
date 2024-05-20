import os
import json
def num1_2():
    with open("lab10.json", mode="r", encoding='utf8') as file:
        a = json.load(file)
        b = (a['products'])
        for i in range(3):
            print("Название", b[i]['name'])
            print("Цена", b[i]['price'])
            print("Вес", b[i]['weight'])
            if b[i]['available'] == True:
                print("В наличии")
            else:
                print("Нет в наличии!")
num1_2()

def num3():
    d = {}
    with open("блокнот.txt", mode="r", encoding='utf8') as file:
        l1 = file.read().splitlines()

    for l in l1:
        word = l.strip().split(' - ')
        if len(word) == 2:
            en = word[0]
            ru = word[1].split(", ")
            for w in ru:
                d[w] = en
    sort = dict(sorted(d.items()))
    with open("блокнот.txt", 'w', encoding='utf-8') as f:
        for ru_word, en_word in sort.items():
            f.write(f'{ru_word} - {en_word}\n')
    print(d)
num3()
