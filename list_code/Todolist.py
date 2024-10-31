import tkinter as tk

def addTask():
    task = taskEntry.get()

    if task:  # Check if the entry is not empty
        listBox.insert(tk.END, task)  # Add the task to the end of the Listbox
        taskEntry.delete(0, tk.END)

def deleteTask():
    if listBox.curselection():
        listBox.delete(listBox.curselection())


root = tk.Tk()
root.title("Todolist")
root.geometry("300x500")

label_title = tk.Label(root, text="Todolist")
label_title.pack(pady=20)

label_Instruct1 = tk.Label(root, text="Enter your task here")
label_Instruct1.pack(pady=10)

taskEntry = tk.Entry(root,width=30)
taskEntry.pack()

listBox = tk.Listbox(root, height=10, width=50)
listBox.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

button_add = tk.Button(button_frame,text="Add Task", command=addTask)
button_add.grid(row=30, column=20)

button_delete = tk.Button(button_frame, text='Delete Task', command=deleteTask)
button_delete.grid(row=30, column=40)

root.mainloop()

