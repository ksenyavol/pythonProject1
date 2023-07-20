# Итоговое задание
# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время
# создания  или последнего изменения заметки. Сохранение заметок
# необходимо сделать  в формате json или csv формат (разделение полей
# рекомендуется делать  через точку с запятой). Реализацию
# пользовательского интерфейса студент может делать как ему удобнее,
# можно делать как параметры запуска  программы (команда, данные),
# можно делать как запрос команды с консоли и последующим вводом
# данных, как-то ещё, на усмотрение студента.

import json
import datetime
import Model
import os
import View


def start():
    sizeOfDictJson = os.path.getsize("Note.json")
    if sizeOfDictJson == 0:
        with open("Note.json", "w") as file1:
            json.dump(dict(), file1, indent=2, ensure_ascii=False)
    View.formaMenu()
    print(f"Дата: {datetime.datetime.fromtimestamp(Model.DTofNote())}")

    command = ""
    while (command != "exit"):
        View.menu()
        command = input("Введите команду: ")
        if command == "add":
            NoteTitle = input("Введите заголовок: ")
            bodyTitle = input("Заметка: ")
            Model.addNote(NoteTitle, bodyTitle)
            input()
        elif command == "read":
            View.miniMenu()
            nums = input(
                "Введите номер id (или all) для вывода всех заметок ")
            Model.readJson(nums)
            input()
        elif command == "edit":
            View.miniMenu()
            nums = input("Введите номер id для редактирования ")
            Model.editJson(nums)
            input()
        elif command == "sort":
            Model.sortJson()
            input()
        elif command == "clear":
            View.miniMenu()
            nums = input(
                "Введите номер id (или all) для удаления всех заметок ")
            Model.clearJson(nums)
            input()
        elif command == "exit":
            print("Выход")
            break
