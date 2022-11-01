
import csv
from csv import writer
from re import search
import re

id = 0
selectedId = 0
user_choice_second = 0
input_update = 0


def get_next_id():
    global id
    id = count() + 1
    return id

def setSelected(entered_id):
    global selectedId
    selectedId = entered_id

def second_select(choice_second):
    global user_choice_second
    user_choice_second = choice_second

def update_data(data):
    global input_update
    input_update = data

def search_surname(entered_surname):
    global search
    search = entered_surname

def function_empl(func_empl):
    global func
    func = func_empl


def count(): # считаю ID: кол-во строк в файле + 1
    count = 0
    for line in open("data.csv"):
        count+= 1
    return count


def show_all_data(): # показать всю базу
    with open("data.csv","r") as f:
        data = csv.reader(f)
        for line in data:
            print(line)

def get_all_data(): # получить всю базу
    result = ""
    with open("data.csv","r") as f:
        data = csv.reader(f)
        for line in data:
            str_line = str(line)
            result = result + str_line + "\n"
    return result

def serch():        # поиск данных по фамилии
    with open("data.csv", "r") as inp:
        data = csv.reader(inp)
        for line in data:
            if(line[1]==search):
                print()
                print(line)
                print()


def search_func():  # выборка сотрудников по должности 
    with open("data.csv", "r") as inp:
        data = csv.reader(inp)
        for line in data:
            if(line[4]==func):
                print(line)


def add_new_employee(): # добавление нового сотрудника
    surname_employee = input("Введите фамилию: ")
    name_employee = input("Введите имя: ")
    tel_employee= input("Введите номер телефона: ")
    function_employee = input("Введите должность: ")
    with open("data.csv", "a",newline='', encoding="utf-8") as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow([get_next_id(),surname_employee,name_employee,tel_employee,function_employee])
        print()
        print("Добавлена запись о новом сотруднике")
        print()

def add_new_employee_from_telegram(): # добавление нового сотрудника
    with open("data.csv", "a",newline='', encoding="utf-8") as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow([get_next_id(),surname_employee,name_employee,tel_employee,function_employee])
        print()
        print("Добавлена запись о новом сотруднике")
        print()

def change_data():  # по номеру id меняем данные о сотруднике и перезаписываем строку
    with open("data.csv") as f:
        data = [r for r in csv.reader(f)]
        for line in data:
            if(int(line[0])==selectedId): 
                line[user_choice_second] = input_update
    with open('data.csv', 'w', encoding="utf-8", newline='') as f:
        csv.writer(f).writerows(data)


def delete_line():  # удаление данных о сотруднике по номеру id
    with open("data.csv", "r") as inp:
        newrows = []
        data = csv.reader(inp)
        for line in data:
            if(int(line[0])!=selectedId):  # в новый список добавила все строки, не равно id
                newrows.append(line)
    with open("data.csv", "w",newline='') as out: # записала эти строки в файл заново полностью
        csv_writer = writer(out)
        for line in newrows:
            csv_writer.writerow(line)
            print()
            print("Запись о сотруднике удалена")
            print()

