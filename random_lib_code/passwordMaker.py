import tkinter as tk
import random

def passwordGenerator():
    Alphabet_lowercase = "abcdefghikjklmnopqrstuvwxyz"
    Alphabet_uppercase = "ABCDEFGHIKKLMNOPQRSTUVWXYZ"
    num = '1,2,3,4,5,6,7,8,9,0'
    symbols = '!@#$%^&*'
    all_characters = Alphabet_lowercase + Alphabet_uppercase + num + symbols
    # password = random.choice(all_characters)
    entry = int(userInput.get())

    password = ''.join(random.choice(all_characters) for _ in range(entry))
    label_result.config(f"Result: {password}")

    # while len(password) == entry:
    #     password = ''.join(random.choice(all_characters))
    # label_result.config(f"Result: {password}")
    # return

root = tk.Tk()

root.geometry("300x300")

root.title("Password Generator")

label = tk.Label(root,text='Generate a strong password')
label.pack()

button_result = tk.Button(root, text="generate", command=passwordGenerator)
button_result.pack()

label_de = tk.Label(root,text='enter only numbers')
label_de.pack()

userInput = (tk.Entry(root,width=30))
userInput.pack()

label_result = tk.Label(root,text='')
label_result.pack()

root.mainloop()
