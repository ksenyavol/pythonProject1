import json
import datetime
import os
import Controller
import Model

def menu():
    formaMenu()
    global os
    global datetime
    global Controller
    global Model
    print("add - добавить элемент в заметки")
    print("read - читать заметку по id или все заметки")
    print("edit - редактировать заметку по id")
    print("sort - осуществить сортировку заметок")
    print("clear - удалить заметку по id или все заметки")
    print("exit - выход")
    formaMenu()

def miniMenu():
    formaMenu()
    with open("note.json") as file:
        data = json.load(file)
        print("Оглавление: ")
        for key, value in data.items():
            print(f'{key} - {value[0]}')
    formaMenu()

def formaMenu():
    print("*" * 30)

def errorId():
    print("Некорректный id")

def errorEnter():
    print("Неверный ввод")

def errorEnterID():
    print("Такой id не найден")

def massegeAboutAdd():
    print(f"Заметка добавлена")

def goodCange():
    print("Заметка изменена успешно")

def dontFindId():
    print("Такой id не найден")

def messegeAboutDalete():
    print("Заметка удалена")

def MessegeAboutAllDalete():
    print("Все заметки удалены")