import os
import csv
def num2():
    print ("Нужно купить:")
    with open ('number2.csv', mode='r') as file:
        rfile = csv. reader (file)
        for row in rfile:
            name, k, price = "".join(row).split(";")
            print(f" {name} - {k} шт. за (price} руб.")
