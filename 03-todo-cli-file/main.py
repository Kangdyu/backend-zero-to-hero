import sys

from todo_manager import TodoManager


def print_menu():
    print("=======================")
    print("=      Todo List      =")
    print("= (1) See Todo List   =")
    print("= (2) Add New Todo    =")
    print("= (3) Complete Todo   =")
    print("= (4) Remove Todo     =")
    print("= (5) Exit            =")
    print("=======================")


def main():
    todo_manager = TodoManager()
    
    while True:
        print_menu()

        try:
            choice = int(input("Select: "))
            match choice:
                case 1:
                    todo_manager.print_todo_list()
                case 2:
                    title = input("Title: ")
                    content = input("Content: ")
                    todo_manager.add_todo(title=title, content=content)
                case 3:
                    id = int(input("Enter the ID you want to complete: "))
                    todo_manager.complete_todo(id)
                case 4:
                    id = int(input("Enter the ID you want to remove: "))
                    todo_manager.remove_todo(id)
                case 5:
                    sys.exit(0)
                case _:
                    print("Please Enter the Integer between 1 ~ 5.")
        except ValueError:
            print("Please Enter the Valid Input.")


if __name__ == "__main__":
    main()
