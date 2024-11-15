import tkinter as tk

def logic():
    expression = entry.get()

    # Evaluate the expression
    try:
        result = eval(expression)
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("My Calculator")
root.geometry("300x500")

# Title label
label_title = tk.Label(root, text="Expression Calculator")
label_title.pack()

# Instruction label
label_instruction = tk.Label(root, text="Enter a mathematical expression")
label_instruction.pack()

# Entry widget for input
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Button to evaluate the expression
button = tk.Button(root, text="Evaluate", command=logic)
button.pack()

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop

root.mainloop()
