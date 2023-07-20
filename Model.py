import json
import datetime
import os
import View
import Controller


def DTofNote():
    current_dateTime = datetime.datetime.now()
    abc = f"{str(current_dateTime.year)}-{str(current_dateTime.month)}-{str(current_dateTime.day)} " \
          f"{str(current_dateTime.hour)}:{str(current_dateTime.minute)}:{str(current_dateTime.second)}"
    rez = datetime.datetime.strptime(abc,
                                     '%Y-%m-%d %H:%M:%S').timestamp()
    return rez


def findId(dictJson):
    global os
    global Controller
    return len(dictJson) + 3


def addNote(noteTitle, bodyTitle):
    newNote = dict()
    dictJson = json.load(open("note.json"))
    id1 = findId(dictJson)
    newNote[id1] = [noteTitle, bodyTitle, DTofNote()]
    dictJson.update(newNote)

    json.dump(dictJson, open("note.json", 'w'), indent=2,
              ensure_ascii=False)
    View.massegeAboutAdd()


def readJson(nums):
    with open("note.json") as file:
        View.formaMenu()
        data = json.load(file)
        if nums == "all":
            for key, value in data.items():
                print(f'{key}: {value[0]}')
                print(f'{value[1]}')
                date_time = datetime.datetime.fromtimestamp(value[2])
                print(f'{date_time}')
        elif nums in data.keys():
            print(f'{int(nums)}: {data[nums][0]}')
            count = 0
            for i in data[nums][1]:
                if (i == " ") and (count > 100):
                    count = 0
                    print()
                else:
                    count += 1
                    print(i, sep="", end="")
            print()
            date_time = datetime.datetime.fromtimestamp(data[nums][2])
            print(f'{date_time}')
        else:
            View.errorId()
        View.formaMenu()


def sortJson():
    newDictSort = dict()
    with open("note.json", "r") as file1:
        dictJson = json.load(file1)
        qw = input("Сортировку проводить по id или по time? id/time: ")
        if qw == "time":
            newDictSort = dict(
                sorted(dictJson.items(), key=lambda item: item[1][2]))
        elif qw == "id":
            newDictSort = dict(
                sorted(dictJson.items(), key=lambda item: int(item[0])))
        else:
            View.errorEnter()
    with open('note.json', 'w') as file:
        json.dump(newDictSort, file, indent=2, ensure_ascii=False)


def editJson(num):
    newDickJson = dict()
    flag = False
    with open("note.json") as file:
        data = json.load(file)
        if num in data.keys():
            flag = True

    if flag == True:
        with open("Note.json", "r") as file1:
            dictJson = json.load(file1)
            newNoteTitle = input("Введите новый заголовок: ")
            newBodyTitle = input("Заметка: ")
        for key, value in dictJson.items():
            if key != num:
                newDickJson[key] = value
            else:
                value[0], value[1], value[
                    2] = newNoteTitle, newBodyTitle, DTofNote()
                newDickJson[key] = value
        with open('note.json', 'w') as file:
            json.dump(newDickJson, file, indent=2, ensure_ascii=False)
            View.goodCange()
    else:
        View.dontFindId()


def clearJson(num):
    newDickJson = dict()  # словарь-буфер
    flag = False
    with open("Note.json") as file:
        data = json.load(file)
        if num in data.keys():
            flag = True

    if flag == True and num != "all":
        with open("Note.json", "r") as file1:
            dictJson = json.load(file1)
        for key, value in dictJson.items():
            if key != num:
                newDickJson[key] = value
        with open('Note.json', 'w') as file:
            json.dump(newDickJson, file, indent=2, ensure_ascii=False)
            View.messegeAboutDalete()
    elif num == "all":
        with open("Note.json", "w") as file1:
            json.dump(dict(), file1, indent=2, ensure_ascii=False)
            View.MessegeAboutAllDalete()
    else:
        View.errorEnterID()
