import tkinter as tk

def calculate():
    try:
        num1 = float(userEntry1.get())
        num2 = float(userEntry2.get())
        sign = signEntry2.get()

        if sign == "+":
            result = num1 + num2
        elif sign == "-":
            result = num1 - num2
        elif sign == "*":
            result = num1 * num2
        elif sign == "/":
            result = num1 / num2
        else:
            labelResult.config(text="Enter the valid sign")
    
        labelResult.config(text=f"Result = {round(result, 2)}")
      
        return
    except ValueError:
        labelResult.config(text=f"Enter a valid number")
    except ZeroDivisionError:
        labelResult.config(text=f"Cannot divide by zero")

        


root = tk.Tk()

root.title("Calculator")


root.geometry("300x400")

label = tk.Label(root, text="The New Redisigned Calcultor")
label.pack(padx=10, pady=5)

label_num1 = tk.Label(root, text="Enter the number 1: ")
label_num1.pack()
# this is num1 text box
userEntry1 = tk.Entry(root, width=30)
userEntry1.pack()

label_num2= tk.Label(root, text="Enter the number 2: ")
label_num2.pack()
# this is num2 textbox
userEntry2 = tk.Entry(root, width=30)
userEntry2.pack()

labelInst = tk.Label(root, text="Enter the operation")
labelInst.pack()

signEntry2 = tk.Entry(root, width=30)
signEntry2.pack()

button_result = tk.Button(root, text="Calculate", command=calculate)
button_result.pack(padx=10, pady=5)

labelResult = tk.Label(root, text="")
labelResult.pack(padx=10, pady=5)

root.mainloop()


    




