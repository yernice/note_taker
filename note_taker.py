import utils

while True:
    print("Menu:")
    print("1. Add a new note")
    print("2. View previous notes")
    print("3. Change notes")
    print("4. Search by Tags")
    print("0. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 0:
        break
    elif choice == 1:
        utils.new_note()
        print("New Entry Added")
    elif choice == 2:
        utils.list_notes()
    elif choice == 3:
        utils.change_notes()
    elif choice == 4:
        utils.search_by_tag()
    else:
        print("No Such Choice. Enter again")


print("Finish")
