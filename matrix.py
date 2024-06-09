import tkinter as tk
from tkinter import messagebox
import numpy as np

def calculate_matrix(flag):
    global matrix_size,entry_2x2,entry_3x3,root,message
    if matrix_size.get() == '2x2':
        try:
            a11 = float(entry_2x2[0][0].get())
            a12 = float(entry_2x2[0][1].get())
            a21 = float(entry_2x2[1][0].get())
            a22 = float(entry_2x2[1][1].get())
            matrix = np.array([[a11, a12], [a21, a22]])
            det = np.linalg.det(matrix)
            if flag == 'Determinant':
                message.config(text=f'Determinant is:  {det:.2f}',font='Arial 12')
            elif flag == 'Inverse Matrix':
                if det == 0 :
                    message.config(text='Determinant is zero, Inverse of Matrix is not Possible.')
                else:
                    matrix_inverse = np.linalg.inv(matrix)
                    result_text = ''
                    result_text = "Inverse Matrix:\n\n"
                    for row in matrix_inverse:
                        result_text += '   '.join(f"{num:.2f}" for num in row) + "\n\n"
                    message.config(text=result_text,font='Arial 12')
            elif flag == 'Eigen Value':
                eigen_values = list(np.linalg.eig(matrix).eigenvalues)
                message.config(text=f'Eigen Values are : \n\n {(eigen_values[0]):.2f} \n\n{(eigen_values[1]):.2f}',font='Arial 12')
            
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
            if flag == 'Determinant':
                message.config(text=f'Determinant is:  {det:.2f}',font='Arial 12')
            elif flag == 'Inverse Matrix':
                if det == 0 :
                    message.config(text='Determinant is zero, Inverse of Matrix is not Possible.')
                else:
                    matrix_inverse = np.linalg.inv(matrix)
                    result_text = ''
                    result_text = "Inverse Matrix:\n\n"
                    for row in matrix_inverse:
                        result_text += '   '.join(f"{num:.2f}" for num in row) + "\n\n"
                    message.config(text=result_text,font='Arial 12')
            elif flag == 'Eigen Value':
                eigen_values = list(np.linalg.eig(matrix).eigenvalues)
                message.config(text=f'Eigen Values are : \n\n {(eigen_values[0]):.2f} \n\n {(eigen_values[1]):.2f} \n\n {(eigen_values[2]):.2f} ',font='Arial 12')

            message.grid(row=5,column=0,columnspan=3)
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

def matrix_GUI(title ,calculate):
    global matrix_size,entry_2x2,entry_3x3,root,message
    # Initialize the main window
    root = tk.Tk()
    root.title(title)

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
    
    # Button to calculate 
    calc_button = tk.Button(root, text=f"Calculate {calculate}", command=lambda :calculate_matrix(calculate),font='Calibri 13')
    calc_button.grid(row=4, column=0, columnspan=3, pady=10)

    # Run the main loop
    root.mainloop()

def determinant():
    matrix_GUI(title='Matrix Determinant Calculator',calculate='Determinant')

def inverse():
    matrix_GUI(title="Inverse Matrix Calculator",calculate='Inverse Matrix')
    
def eigen_values():
    matrix_GUI(title="Matrix Eigen Value Calculator",calculate='Eigen Value')


if __name__ == "__main__":
    # Funtions for Testing. Test one function at a time, Remaining other functions commented.
    determinant()
    #inverse()
    #eigen_values()
    pass