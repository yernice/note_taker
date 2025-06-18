from datetime import datetime
import os

def new_note():
    # creating a new note
    today = datetime.now()
    title = input("How do you want to name your note?\n")
    file_path = f"notes\{title}.txt"
    new_note = open(f"{file_path}", "a")
    time = today.strftime("%H:%M")
    new_note.write(f"{time}\n")

    # writing into a note
    print("Write your entry and type 'EOF' on a separate line to inicate end of an entry:")
    paragraph = []
    while True:
        line = input()
        if line == "EOF":
            break
        paragraph.append(line)
    
    note = "\n".join(paragraph)
    new_note.write(note)
    new_note.write("\n\n")
    new_note.close()

    # adding tags
    tags_choice = input("Do you want to add tags to it? y/n \n")
    if tags_choice:
        add_tag(file_path)

def list_notes():
    num = 1
    print("These are all the entries: ")
    for entry in os.listdir("notes"):
        print(f"{num}. {entry}")
        num += 1

    while True:
        choice = input("Do you want to check the contents of any of them? y/n\n")
        if choice.lower() == 'n':
            break
        
        choice = int(input("Which one? Enter a number: "))
        num = 1        
        for entry in os.listdir("notes"):
            if num == choice:
                read = open(f"notes\{entry}")
                print(read.read())
                num -= 1
                read.close()

                break

            num += 1
            
        if num == choice:
            print("No such entry")

def change_notes():
    # list notes
    num = 1
    print("These are all the notes: ")
    for note in os.listdir("notes"):
        print(f"{num}. {note}")
        num += 1
    
    # change notes
    while True:
        choice = int(input("Which note do you want to change? Enter a number: "))
        num = 1        
        found = False
        # search for the note 
        for note in os.listdir("notes"):
            if num == choice:
                # opening a note
                found = True
                today = datetime.now()
                file_path = f"notes\{note}"
                edit_note = open(f"{file_path}", "a")
                time = today.strftime("%H:%M")
                edit_note.write(f"{time}\n")

                # writing into a note
                print("Write your entry and type 'EOF' on a separate line to inicate end of an entry:")
                paragraph = []
                while True:
                    line = input()
                    if line == "EOF":
                        break
                    paragraph.append(line)

                note = "\n".join(paragraph)
                edit_note.write(note)
                edit_note.write("\n\n")
                edit_note.close()

                # adding tags
                tags_choice = input("Do you want to add tags to it? y/n \n")
                if tags_choice:
                    add_tag(file_path)

                break

            num += 1

        if not found: 
            print("There is no such note")
        
        leave = input("Have you finished? y/n \n")
        if leave == 'y':
            break

def add_tag(file_path):
    print("Write tags and separate them with enter. Write EOF to declare that you have finished")
    tags_list = []
    while True:
        line = input()
        if line == "EOF":
            break
        tags_list.append(line)
    
    file_name, ext = file_path.split(".")
    new_file_path = file_name + "_" + "_".join(tags_list) + ".txt"
    os.rename(file_path, new_file_path)
    
