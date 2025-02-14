import tkinter as tk

root = tk.Tk()

root.geometry("300x600")

root.title("Quick Weather")

# label = tk.Label(root,text="Today's weather", padx=20, pady=10)
# label.pack()

# label2 = tk.Label(root,text='Which city do you what the weather of?', pady=10,  anchor='w')
# label2.pack()

# CityinputText = tk.Entry(root, justify='left')
# CityinputText.pack()

button_result = tk.Button(root, text='Test',  pady=10)
button_result.pack()

label_3 = tk.Label(root,text='')
label_3.pack()

label_temp = tk.Label(root,text='')
label_temp.pack()

label_visibiliy = tk.Label(root,text='')
label_visibiliy.pack()

label_windspeed = tk.Label(root,text='')
label_windspeed.pack()


root.mainloop()




    
