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
        print(f'the soldier {soldier_name} added.')

    except ValueError as e:
        print(e)


def handle_remove_soldier() -> None:
    try:
        soldier_id = input("ehter soldier id:\n")
        remove_soldier(soldier_id)
        print(f'the soldier {soldier_id} deleted.')

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
        print(f'duty {duty_name} added to {soldier_id}')

    except (ValueError, KeyError) as e:
        print(e)


def handle_update_status() -> None:
    try:
        soldier_id = input("ehter doldier id:\n")
        duty_name = input("enter duty name:\n")
        new_status = input("ehter duty's new status")

        update_duty_status(soldier_id, duty_name, new_status)
        print(f'duty {duty_name} updated to {new_status}')

    except (ValueError, KeyError) as e:
        print(e)


def handle_view_soldier_duties() -> None:
    try:
        soldier_id = input("ehter doldier id:\n")
        duties = get_soldier_duties(soldier_id)
        for duty in duties:
            print(f'duty name: {duty["name"]} | duty day: {duty["day"]} | duty status: {duty["status"]}')
    
    except KeyError as e:
        print(e)


def show_soldiers_menu() -> None:
    print("====================")
    print("-----soldiers menu-----")
    print("1. add soldier")
    print("2. remove soldier")
    print("3. show all soldiers")
    print("4. back to the main menu")


def show_duties_menu() -> None:
    print("====================")
    print("-----duties menu-----")
    print("1. add duty to soldier")
    print("2. update duty status")
    print("3. show soldier duties")
    print("4. back to the main menu")


def soldiers_user_choice_flow(choice):
    if choice == "1":
        handle_add_soldier()
        return True
    
    elif choice == "2":
        handle_remove_soldier()
        return True
    
    elif choice == "3":
        handle_view_soldiers()
        return True

    elif choice == "4":
        return False

    else:
        raise ValueError("wrong choice, please follow the menu")
        raise


def duties_user_choice_flow(choice):
    if choice == "1":
        handle_add_duty()
        return True
    
    elif choice == "2":
        handle_update_status()
        return True
    
    elif choice == "3":
        handle_view_soldier_duties()
        return True

    elif choice == "4":
        return False

    else:
        raise ValueError("wrong choice, please follow the menu")
        raise
    


def main() -> None:
    while True:
        try:
            show_menu()
            choice = get_user_choice()
            if choice == "1":
                show_soldiers_menu()
                inner_choice = get_user_choice()

                if inner_choice == "1":
                    handle_add_soldier()

                elif inner_choice == "2":
                    handle_remove_soldier()

                elif inner_choice == "3":
                    handle_view_soldiers()
                
                elif inner_choice == "4":
                    continue

                else:
                    raise ValueError("wrong choice, please follow the menu")
                
            elif choice == "2":
                show_duties_menu()
                inner_choice = get_user_choice()

                if inner_choice == "1":
                    handle_add_duty()
                
                elif inner_choice == "2":
                    handle_update_status()
                
                elif inner_choice == "3":
                    handle_view_soldier_duties()
                
                elif inner_choice == "4":
                    continue
                
                else:
                    raise ValueError("wrong choice, please follow the menu")
            
            elif choice == "3":
                print("good by...")
                break

            else:
                raise ValueError("wrong choice, please follow the menu")
        
        except ValueError as e:
            print(e)
            
main()