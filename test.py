import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("Combobox")

selected_elem = tk.StringVar(value='value1')
combobox = ttk.Combobox(root, textvariable=selected_elem)
combobox['values'] = ('value1', 'value2', 'value3')
combobox.pack(fill=tk.X, padx=20, pady=20)

myLabel = tk.Label(root, text=selected_elem.get())
myLabel.pack()

# prevent typing a value
combobox['state'] = 'readonly'

# place the widget
combobox.pack(fill=tk.X, padx=5, pady=5)


# bind the selected value changes
def value_changed(event):
    """ handle the value changed event """
    myLabel.configure(text=selected_elem.get())
    myLabel.pack()


combobox.bind('<<ComboboxSelected>>', value_changed)

root.mainloop()