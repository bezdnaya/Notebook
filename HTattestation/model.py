
from datetime import datetime
import json
from random import randint


        

def download_notes():
    try:
        with open('C:\Python ht\HTattestation\list_of_notes.json', "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Ваш документ не найден")

def push_to_json(list):
    try:
        data = json.load(open('C:\Python ht\HTattestation\list_of_notes.json'))
    except:
        data =[]
    data.append(list)
    with open ("C:\Python ht\HTattestation\list_of_notes.json", "w") as file:
        json.dump(data, file, indent = 2, ensure_ascii= False)
    print("Заметка успешно сохранена")


def set_id():
    id = randint(1, 999)
    try:
        data = json.load(open ('C:\Python ht\HTattestation\list_of_notes.json'))
    except:
        data = []
    ids = []
    for item in data:
        ids.append(item['id']) 
    
    if id not in ids:
        return id
    else:
        set_id()



def new_note():
    id = set_id()
    name = input("Введите название заметки: ")
    body = input("Напишите что-нибудь, например ваши мысли: ")
    date = str(datetime.strftime(datetime.now(), "%d-%m-%Y, %H:%M"))

    new_note = {
        'id' : id,        
        'name' : name,
        'text': body,
        'date' : date
    }
    return new_note

def is_id(list, id): 
    ids = []
    for i in range(len(list)):
        ids.append(list[i]['id']) 
    if id in ids:
        return ids.index(id)
    else:
        print("Такого id нет в списке")
        return -1

def watch_note(list, id):
    index = is_id (list, id)
    if index >= 0:
        print(list[index]['text'])
    else:
        print ("Такого id не существует")

def delete_note (list, id):
    index = is_id(list, id)
    if index >= 0:
        list.pop(index)
        with open ("C:\Python ht\HTattestation\list_of_notes.json", "w") as file:
            json.dump(list, file, indent = 2, ensure_ascii= False)
        print("Заметка успешно удалена")

    else:
        print("Операция невозможна. Такого id не существует")

def edit_note (list, id):
    index = is_id(list, id)
    if index >= 0:
        act = input("Введите\n1 - если хотите изменить id\n2 - если хотите изменить название заметки\n3 - если хотите изменить тело заметки: ")
        if act == "1":
            list[index]['id'] = input("Введите новый id: ")
        elif act == "2":
            list[index]['name'] = input("Введите новое название заметки: ")
        elif act == "3":
            list[index]['text'] = input("Введите новый текст заметки: ")
            list[index]['date'] = str(datetime.strftime(datetime.now(), "%d-%m-%Y, %H:%M"))
        with open ("C:\Python ht\HTattestation\list_of_notes.json", "w") as file:
            json.dump(list, file, indent = 2, ensure_ascii= False)
        print("Заметка успешно отредактирована")
        

def sort_by_date (list):
    act = input ("Введите \n1, если хотите увидеть сначала ранние заметки\n2 - если хотите увидеть сначала поздние заметки\n")
    if act == "1":
        sorted_list = sorted(list, key= lambda d: d['date'], reverse=False)
        print_list(sorted_list)
    elif act == "2":
        sorted_list = sorted(list, key= lambda d: d['date'], reverse=True)
        print_list(sorted_list)

def print_list (list):
    for i in range (len(list)):
        print ("-" * 60)
        print ("| " + str(list[i]['id']) + " | " + list[i]['name'] + " | " + list[i]['text'] + " | " + list[i]['date'] + " | ")



            



    

        

