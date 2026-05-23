from soldier_manager import add_soldier, get_all_soldiers, remove_soldier
from duty_manager import add_duty_to_soldier, update_duty_status, get_soldier_duties


def show_menu() -> None:
    print("====================")
    print("-----Main menu-----")
    print("1. soldier menager")
    print("2. duties menager")
    print("3. EXIT")
    print("====================")


def get_user_choice() -> str | int:
    choice = input("enter your choice:\n")
    return choice


def handle_add_soldier() -> None:
    try:
        soldier_id = input("ehter soldier id:\n")
        soldier_name = input("enter soldier name:\n")

        add_soldier(soldier_id, soldier_name)

    except ValueError as e:
        print(e)


def handle_remove_soldier() -> None:
    try:
        soldier_id = input("ehter soldier id:\n")
        remove_soldier(soldier_id)

    except KeyError as e:
        print(e)


def handle_view_soldiers() -> None:
    soldiers_data = get_all_soldiers()

    print("-------soldiers:-------\n")
    for soldier in soldiers_data:
        print(f'soldier name: {soldier["name"]} | soldier id: {soldier["id"]} | duties: {soldier["duties"]}')
        print("*" * 50)


def handle_add_duty() -> None:
    try:
        soldier_id = input("ehter doldier id:\n")
        duty_name = input("enter duty name:\n")
        duty_day = input("ehter duty day:\n")

        add_duty_to_soldier(soldier_id, duty_name, duty_day)

    except (ValueError, KeyError) as e:
        print(e)


def handle_update_status() -> None:
    try:
        soldier_id = input("ehter doldier id:\n")
        duty_name = input("enter duty name:\n")
        new_status = input("ehter duty's new status")

        update_duty_status(soldier_id, duty_name, new_status)

    except (ValueError, KeyError) as e:
        print(e)


def handle_view_soldier_duties() -> None:
    try:
        soldier_id = input("ehter doldier id:\n")
        get_soldier_duties(soldier_id)
    
    except KeyError as e:
        print(e)