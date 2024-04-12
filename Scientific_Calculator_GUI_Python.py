import tkinter as tk
from math import sin,cos,tan,log,log10,cbrt,sqrt,pi,e

class GUI:
    
    def __init__(self,root,title) :
        self.root = root
        self.title = title
        self.root.title(self.title)
    
    def entry(self,entry_display):
        self.entry_display = entry_display

    def update_display(self, value):
        current = self.entry_display.get()
        self.entry_display.delete(0, tk.END)
        self.entry_display.insert(tk.END, current + value)
        calculate(False)

    def clear_display(self):
        global result_label
        result_label.config(text='',borderwidth=2)
        self.entry_display.delete(0, tk.END)

    def backspace(self):
        global result_label
        current = self.entry_display.get()[:-1]
        self.entry_display.delete(0, tk.END)
        self.entry_display.insert(tk.END, current)
        result_label.config(text='Ans :  ' + str(current),borderwidth=2)
        calculate(False)


root = tk.Tk() #Creating Window
main = GUI(root,'Calculator') # Set Title of window and Calculator window is assign to main variable.


# Creating Entry Display 
entry_display = tk.Entry(root, width=45, borderwidth=2,font='Arial 20') # Creating Entry Display
entry_display.bind("<Key>","break") # Disable Keyboard Interrupts
entry_display.grid(row=0, column=0, columnspan=6, padx=10, pady=10) # Position of Entry Display
main.entry(entry_display)  # Assigning entry-display of calculator window to main for modifiying.

# Creating Result Label below entry display
result_label = tk.Label(root,borderwidth=2,anchor='w',font = "Arial 17")
result_label.grid(row=1,columnspan=4,column=0,padx=2,pady=2)

def calculate(flag):
    global result_label,angle_unit
    try:
        expression = main.entry_display.get()
        if '×' in expression: # Replacing Multiplication Sign by Multiplication operator.
            expression = expression.replace('×','*')
        
        if 'log' in expression:
            expression = expression.replace('log','log10')

        if 'ln' in expression:  #Do not shift this code above if 'log' in.. , Because it wlll replace 'ln' to 'log' them 'log' to 'log10'
            expression = expression.replace('ln','log')

        if angle_unit == 'Deg':
            trigno_list = ['sin(','cos(','tan(']
            for trigno in trigno_list:
                if trigno in expression:
                    expression = expression.replace(trigno,trigno+'(pi/180)*') # Converting Input Degree angle into Radian.


        result = round( eval( expression ) ,  10) # Finally Performing Calulation (Evaluating) and round off upto 10 digits.
            


        if flag == True:  # When = button is pressed the flag value is True and answer will displayed on entry_display screen.
            main.entry_display.delete(0,tk.END)
            main.entry_display.insert(tk.END, str(result))
        else:  
            # Calculating result without pressing  eqaul_to button and answer will be displayed on answer_label. Flag value is False.
            result_label.config(text='Ans :  ' + str(result),anchor='w',borderwidth=2)
            result_label.grid(row=1,columnspan=4,column=0,padx= 2,pady=2)
    except:
        if flag == True:
            main.entry_display.delete(0,tk.END)
            main.entry_display.insert(tk.END, "Error")
        else : 
            result_label.config(text='',borderwidth=2)
            result_label.grid(row=1,columnspan=4,column=0,padx=2,pady=2)


def toggle_unit():
    global angle_unit
    global unit_button
    if angle_unit == "Deg":
        angle_unit = "Rad"
        unit_button.config(text=angle_unit)
    else:
        angle_unit = "Deg"
        unit_button.config(text=angle_unit)
    calculate(False)


angle_unit = 'Deg'
# Button values
button_values = [
    ('7', '8', '9', '/',angle_unit,'cbrt('),
    ('4', '5', '6', '×','sin(','ln('),
    ('1', '2', '3', '-','cos(','log('),
    ('0', 'C', '=', '+','tan(','pi'),
    ('<<', '(', ')', '.','sqrt(','e')
]

# Creating buttons
for i, row in enumerate(button_values):
    for j, value in enumerate(row):

        if i==0 and j==4:
            unit_button = tk.Button(root,text=value,command=toggle_unit,padx=40,pady=20,font='Arial 12')
            unit_button.grid(row=i+2,column=j,padx=5,pady=5)
            continue

        btn = tk.Button(root, text=value, padx=40, pady=20,font= 'Arial 12')
        if value == '=':
            btn.config(command=lambda equal_to_flag = True: calculate(equal_to_flag))
        elif value == 'C':
            btn.config(command=main.clear_display)
        elif value == '<<':
            btn.config(command=main.backspace)
        else:
            btn.config(command=lambda v=value: main.update_display(v))
        btn.grid(row=i + 2, column=j, padx=5, pady=5)  

root.mainloop()