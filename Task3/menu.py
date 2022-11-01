
import model

# input_id_employee = 0
# user_choice_second = 0

def list_menu():
    global input_id_employee
    global user_choice_second 
    work_is_over = False

    while(not work_is_over):
        print("Выберите пункт меню: ")
        print("1. Показать всю базу")
        print("2. Поиск по фамилии")
        print("3. Выборка по должжности")
        print("4. Добавить нового сотрудника")
        print("5. Изменить данные сотрудника")
        print("6. Удалить запись о сотруднике")
        print("7. Завершение работы")
        user_choice_one = int(input())
        if(user_choice_one==7):
            work_is_over=True
            print("Завершение работы.")
            print()
        elif(user_choice_one == 1):  # показать всю базу сотрудников
            model.show_all_data()
        elif(user_choice_one == 2):  # поиск данных по фамилии сотрудника
            input_search_surname = input("Введите фамилию сотрудника: ")
            model.search_surname(input_search_surname)      
            model.serch()
        elif(user_choice_one == 3):
            input_function_employee = input("Введите должность сотрудников:")
            model.function_empl(input_function_employee)
            model.search_func()
        elif(user_choice_one == 4):  # добавить нового сотрудника        
            model.add_new_employee()
        elif(user_choice_one == 5): # изменить данные сотрудника по номеру id
            input_id_employee=int(input("Укажите id сотрудника:"))
            model.setSelected(input_id_employee)  
            print("Выберите параметр изменения: ")
            print("1. Фамилия")
            print("2. Имя")
            print("3. Номер телефона")
            print("4. Должность")
            user_choice_second = int(input())
            model.second_select(user_choice_second)
            input_update=input("Введите новые данные: ")
            model.update_data(input_update)
            model.change_data()
        elif(user_choice_one == 6):
            input_id_employee=int(input("Укажите id сотрудника:"))
            model.setSelected(input_id_employee)
            model.delete_line()

list_menu()