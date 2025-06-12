from datetime import datetime
import os

def new_note():
    today = datetime.now()
    title = input("How do you want to name your note?")
    file_path = f"notes\{title}.txt"
    new_note = open(f"{file_path}", "a")
    time = today.strftime("%H:%M")
    new_note.write(f"{time}\n")

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

    tags_choice = input("Do you want to add tags to it? y/n \n")
    if tags_choice:
        folder_path = f"notes\\"
        add_tag(title, folder_path, file_path)

def list_notes():
    num = 1
    print("These are all the entries: ")
    for entry in os.listdir("notes"):
        print(f"{num}. {entry}")
        num += 1

    while True:
        print("Do you want to check the contents of any of them? y/n")
        choice = input("Enter a letter: ")
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
    num = 1
    print("These are all the notes: ")
    for entry in os.listdir("notes"):
        print(f"{num}. {entry}")
        num += 1

    while True:
        choice = int(input("Which note do you want to change? Enter a number: "))
        num = 1        
        found = False
        for entry in os.listdir("notes"):
            if num == choice:
                found = True
                today = datetime.now()
                edit_note = open(f"notes\{entry}", "a")
                time = today.strftime("%H:%M")
                edit_note.write(f"{time}\n")

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

                break

            num += 1

        if not found: 
            print("There is no such note")
        
        leave = input("Have you finished? y/n \n")
        if leave == 'y':
            break

def add_tag(title, folder_path, file_path):
    print("Write tags and separate them with enter. Write EOF to declare that you have finished")
    tags_list = []
    while True:
        line = input()
        if line == "EOF":
            break
        tags_list.append(line)
    
    new_file_path = folder_path + title + "_" + "_".join(tags_list) + ".txt"
    os.rename(file_path, new_file_path)
    
