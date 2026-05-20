from soldier_manager import add_soldier, get_all_soldiers


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