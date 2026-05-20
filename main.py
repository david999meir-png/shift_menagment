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