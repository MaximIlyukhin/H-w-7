def main_menu() -> int:
    print('Главное меню.')
    menu_list = ['Показать все контакты',
                 'Открыть файл',
                 'Сохранить файл',
                 'Создать контакт',
                 'Изменить контакт',
                 'Удалить контакт',
                 'Выход'
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    user_input = int(input('Введи команду >: '))
    return user_input

def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()


def db_success(db: list):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False

def write_fail(db):
    data = open('database.txt', 'w', encoding='UTF-8')
    for i in range(len(db)):
        a = []
        for val in db[i].values():
            a.append(val)
        data.write(';'.join(a) + '\n')
    data.close()

def create_contact():
    print('Создание нового контакта.')
    new_contact = dict()
    new_contact['lastname'] = input('\tВведите фамилию >: ')
    new_contact['firstname'] = input('\tВведите имя >: ')
    new_contact['phone'] = input('\tВведите телефон >: ')
    new_contact['comment'] = input('\tВведите комментарий >: ')
    return new_contact

def change_contact(db):
    print('Изменение контакта.')
    print(show_all(db))
    num_1 = int(input('Напиши номер изменяемого контакта >: '))
    for i, key in enumerate(db[num_1-1].keys()):
        print(i+1, key)
    num_2 = int(input('Напиши номер изменяемого параметра >: '))
    for i, key in enumerate(db[num_1-1].keys()):
        if i == num_2-1:
            new_key = key
    db[num_1-1][new_key] = input('Напиши правильный вариант параметра >: ')

def delete_contact(db):
    print('Удаление контакта.')
    print(show_all(db))
    return int(input('Напиши номер удаляемого контакта >: ')) - 1

def exit_program():
    print('Завершение программы.')
    exit()


