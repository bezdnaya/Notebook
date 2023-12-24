import time
from model import *

def main_menu ():
    data = download_notes()
    
    act = input ("Добро пожаловать в журнал заметок!\nНажмите \n1 если хотите посмотреть все заметки\n2 если хотите добавить новую заметку\n3 если хотите удалить заметку по id \n4 если хотите изменить заметку\n5 если хотите отсортировать список заметок по дате\n")
    if act == "1":
        print("\n"*100)
        print_list(data)
        time.sleep(5)
        back = input("Введите m, если хотите вернуться в основное меню\n")
        if back == "m" or "M":
            main_menu()
    elif act == "2":
        push_to_json(new_note())
        time.sleep(3)
        print("\n"*50)
        main_menu()
    elif act == "3":
        id = input("Введите id заметки которую хотите удалить\n")
        delete_note(data, int(id))
        time.sleep(3)
        print("\n"*50)
        main_menu()
    elif act == "4":
        edit_note(data, int(input("Введите id заметки которую хотите изменить\n")))
        time.sleep(2)
        print("\n"*50)
        main_menu()
    elif act == "5":
        sort_by_date(data)
        time.sleep(5)
        back = input("Введите m, если хотите вернуться в основное меню\n")
        if back == "m" or "M":
            main_menu()

main_menu()