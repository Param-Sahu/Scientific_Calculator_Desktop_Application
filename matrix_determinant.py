import tkinter as tk
from tkinter import messagebox
import numpy as np

def calculate_determinant():
    global matrix_size,entry_2x2,entry_3x3,root,message
    if matrix_size.get() == '2x2':
        try:
            a11 = float(entry_2x2[0][0].get())
            a12 = float(entry_2x2[0][1].get())
            a21 = float(entry_2x2[1][0].get())
            a22 = float(entry_2x2[1][1].get())
            matrix = np.array([[a11, a12], [a21, a22]])
            det = np.linalg.det(matrix)
            message.config(text=f'The determinant is: {det:.2f}',font='Calibri 13')
            message.grid(row=5,column=0,columnspan=2)
        except ValueError:
            messagebox.showerror("Input error", "Please enter valid numbers.")
    elif matrix_size.get() == '3x3':
        try:
            a11 = float(entry_3x3[0][0].get())
            a12 = float(entry_3x3[0][1].get())
            a13 = float(entry_3x3[0][2].get())
            a21 = float(entry_3x3[1][0].get())
            a22 = float(entry_3x3[1][1].get())
            a23 = float(entry_3x3[1][2].get())
            a31 = float(entry_3x3[2][0].get())
            a32 = float(entry_3x3[2][1].get())
            a33 = float(entry_3x3[2][2].get())
            matrix = np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])
            det = np.linalg.det(matrix)
            message.config(text=f'The determinant is: {det:.2f}',font='Calibri 13')
            message.grid(row=5,column=0,columnspan=3)
            #messagebox.showinfo("Determinant", f"The determinant is: {det:.2f}")
        except ValueError:
            messagebox.showerror("Input error", "Please enter valid numbers.")

def update_matrix_entries():
    global matrix_size,entry_2x2,entry_3x3,message
    for row in entry_2x2:
        for entry in row:
            entry.grid_forget()
    for row in entry_3x3:
        for entry in row:
            entry.grid_forget()

    if matrix_size.get() == '2x2':
        for i in range(2):
            for j in range(2):
                entry_2x2[i][j].grid(row=i+1, column=j, padx=2, pady=2)
    elif matrix_size.get() == '3x3':
        for i in range(3):
            for j in range(3):
                entry_3x3[i][j].grid(row=i+1, column=j, padx=2, pady=2)
    message.config(text='')

def determinant():
    global matrix_size,entry_2x2,entry_3x3,root,message
    # Initialize the main window
    root = tk.Tk()
    root.title("Matrix Determinant Calculator")

    # Dropdown menu for selecting matrix size
    matrix_size = tk.StringVar(root)
    matrix_size.set('2x2')  # default value

    size_menu = tk.OptionMenu(root, matrix_size, '2x2', '3x3', command=lambda _: update_matrix_entries())
    size_menu.grid(row=0, column=0, columnspan=2, pady=10)

    # Entries for 2x2 matrix
    entry_2x2 = [[tk.Entry(root,font='Calibri 13') for _ in range(2)] for _ in range(2)]

    # Entries for 3x3 matrix
    entry_3x3 = [[tk.Entry(root,font='Calibri 13') for _ in range(3)] for _ in range(3)]
    message = tk.Label(root,text='')
    # Placeholders initially for 2x2 matrix
    update_matrix_entries()

    # Button to calculate determinant
    calc_button = tk.Button(root, text="Calculate Determinant", command=calculate_determinant,font='Calibri 13')
    calc_button.grid(row=4, column=0, columnspan=3, pady=10)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    determinant()