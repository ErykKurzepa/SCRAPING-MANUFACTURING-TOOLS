from app import all_items

USER_CHOICE = '''
Enter one of the following

- 'd' to search tool with specific diameter
- 's' to search tool with specific ID number
- 'n' to just get the next available cutting tool on the url
- 'q' to exit

Enter your choice: '''


def print_page():
    page_number = input('Enter url number that you would like to see: ')
    cheapest_items = sorted(all_items, key=lambda x: x.serial)[:5]
    for item in cheapest_items:
        print(item)


def diameter():
    print('Enter tool diameter that you are looking for: ')
    available_diameters = {item.diameter for item in all_items}
    item_diameter = float(input(f'Choose from available diameters {available_diameters}: '))
    items = [item for item in all_items if item.diameter == item_diameter]
    for line in items:
        print(line)


def serial():
    item_serial = input('Enter tool ID number that you are looking for: ')
    items = [item for item in all_items if item.serial.upper() == item_serial.upper()]
    for line in items:
        print(line)


item_generator = (x for x in all_items)


def get_next():
    print(next(item_generator))


user_choices = {
    'n': get_next,
    'd': diameter,
    's': serial
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('n', 'd', 's'):
            user_choices[user_input]()
        else:
            print('Please choose a valid command.')
        user_input = input(USER_CHOICE)


menu()
