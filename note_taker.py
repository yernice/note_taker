import utils

while True:
    print("Menu:")
    print("1. Add a new note")
    print("2. View previous notes")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 4:
        break
    elif choice == 1:
        utils.new_note()
        print("New Entry Added")
    elif choice == 2:
        utils.list_notes()
    else:
        print("No Such Choice. Enter again")


print("Finish")
