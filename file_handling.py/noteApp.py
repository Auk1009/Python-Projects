#Note App

def add_note(title,content):
    with open('DatabaseForNoteApp.txt','a') as file:
        file.write("\n"+"Heading:-"+title+'\n')
        file.write(content)


def view_note():
    with open('DatabaseForNoteApp.txt','r') as file:
        print(file.read())

def clear_notes():
    with open('DatabaseForNoteApp.txt','w') as file:
        pass



while True:
    print('Welcome to the Note App')
    userinput = int(input('Add note(1), View Note(2), Clear Note(3)'))
    if userinput == 1:
        heading = input('Heading of the Note: ')
        contentinput = input(f'Write the content of {heading}: ')
        add_note(heading,contentinput)
        print(f"Title: {heading}")
        print(contentinput)
    elif userinput == 2:
        view_note()
    elif userinput == 3:
        clear_notes()