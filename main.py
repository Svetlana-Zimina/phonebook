def show(file_name: str) -> list[str]:
    """Вывод записей из справочника на экран."""

    file = open(file_name, 'r')
    return file.readlines()


def add(file_name: str, line_to_add: str) -> None:
    """Добавление новой записи в справочник."""

    file = open(file_name, 'a')
    file.write(f'{line_to_add}\n')
    file.close()


def search(file_name: str, search_params: str) -> list[str]:
    """Поиск записей по одному или нескольким параметрам."""

    search_list: list[str] = []
    with open(file_name, 'r') as data:
        for line in data:
            if search_params in line:
                search_list.append(line)
    return search_list


def edit(file_name: str, data_to_change: str, new_data: str) -> None:
    """Редактирование записей."""

    with open(file_name, 'r') as file:
        data = file.read()
        data = data.replace(data_to_change, new_data)
    with open(file_name, 'w') as file:
        file.write(data)


def main():
    """Главная функция."""

    file_name: str = 'phonebook.txt'

    command: str = input(
        'Выберите команду:\n' +
        'show - показать записи из справочника\n' +
        'add - добавить новую запись\n' +
        'edit - редактировать запись\n' +
        'search - поиск записи\n' +
        'exit - выйти из телефонного справочника\n'
    )

    if command == 'add':
        new_contact: str = input(
            'Введите <фамилию> <имя> <отчество> <организацию> '
            '<рабочий телефон> <личный телефон (сотовый)> через пробел\n'
        )

        add(file_name, new_contact)
        print('Запись успешно добавлена')
        main()

    elif command == 'show':
        data_list: list[str] = show(file_name)
        print(*data_list)
        main()

    elif command == 'search':
        search_params: str = input(
            'Введите параметры поиска через пробел. '
            'Не забудьте про регистр!\n'
        )
        found_record: list[str] = search(file_name, search_params)
        print(*found_record)
        main()

    elif command == 'edit':
        data_to_change: str = input('Введите контакт для замены\n')
        new_data: str = input('Введите измененный контакт\n')
        edit(file_name, data_to_change, new_data)
        print('Запись успешно отредактирована')
        main()

    elif command == 'exit':
        print('Хорошего дня!')

    else:
        print('Неизвестная команда. ВВедите команду из списка')
        main()


if __name__ == '__main__':
    main()
