import tkinter as tk
from math import sin,cos,tan,log,log10,cbrt,sqrt,pi,e,factorial

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
        self.entry_display.xview_moveto(1) # Automatically shift Scrollbar 
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
        calculate(False) # Calculating Expression(Result) after pressing backspace button and printing on result_label.


root = tk.Tk() #Creating Window
root.iconbitmap('calculator.ico')
main = GUI(root,'Calculator') # Set Title of window and Calculator window is assign to main variable.


# Creating Entry Display 
entry_display = tk.Entry(root, width=35, borderwidth=2,font='Arial 20') # Creating Entry Display
entry_display.bind("<Key>","break") # Disable Keyboard Interrupts
entry_display.grid(row=0, column=0, columnspan=5, padx=10, pady=10,sticky = 'ew') # Position of Entry Display
main.entry(entry_display)  # Assigning entry_display of calculator window to main for modifiying.

# Creating Scrollbar for Entery Display.
scrollbar = tk.Scrollbar(root, orient='horizontal', command=entry_display.xview)
scrollbar.grid(row=0, column=5,sticky='ew')

# Configure the Entry widget to communicate with the Scrollbar
entry_display.config(xscrollcommand=scrollbar.set)
# Creating Result Label below entry display
result_label = tk.Label(root,borderwidth=2,anchor='w',font = "Arial 17")
result_label.grid(row=1,columnspan=4,column=0,padx=2,pady=2)

def calculate(flag):
    global result_label,angle_unit
    try:
        expression = main.entry_display.get()
        if '×' in expression: # Replacing Multiplication Sign by Multiplication operator.
            expression = expression.replace('×','*')
        
        if '^' in expression:
            expression = expression.replace('^','**')

        if '²' in expression:
            expression = expression.replace('²','**2')
        
        if '³' in expression:
            expression = expression.replace('³','**3')

        if angle_unit == 'Deg':  
            trigno_list = ['sin(','cos(','tan('] # list for trignometric function for replacement.
            for trigno in trigno_list:
                if trigno in expression:
                    expression = expression.replace(trigno,trigno+'(pi/180)*') # Converting Input Degree angle into Radian.


        function_dict = {'ln':log,'log':log10,'sin':sin,'cos':cos,'tan':tan,
                        'pi':pi,'e':e,'sqrt':sqrt,'cbrt':cbrt,
                        'facto':factorial}
        result = round( eval( expression , function_dict) ,  10) # Finally Performing Calulation (Evaluating) and round off upto 10 digits.
        ''' 
        By passing function_dict as 'globals' argument we ensure that eval function can "only" access these function present in dictionary.
        If we do not use function_dict , eval function can access all functions (built-in or user defined) which cause insecurity of code.
        '''


        if flag == True:  # When = button is pressed the flag value is True and answer will displayed on entry_display screen.
            main.entry_display.delete(0,tk.END)
            main.entry_display.insert(tk.END, str(result))
        else:  
            # Calculating result without pressing  eqaul_to button and answer will be displayed on answer_label. Flag value is False.
            result_label.config(text='Ans :  ' + str(result),anchor='w',borderwidth=2)
            result_label.grid(row=1,columnspan=4,column=0,padx= 2,pady=2)
    except:  # Error Handling 
        if flag == True:  # printing Error message on entry_display if any error encountered after pressing = button.
            main.entry_display.delete(0,tk.END)
            main.entry_display.insert(tk.END, "Error")
        else : 
            result_label.config(text='',borderwidth=2) # Printing nothing on result_label in case of any error .
            result_label.grid(row=1,columnspan=4,column=0,padx=2,pady=2)


def toggle_unit(): 
    # Function for changing Degree to Radian and Vice-Versa.
    global angle_unit
    global unit_button
    if angle_unit == "Deg":
        angle_unit = "Rad"
        unit_button.config(text=angle_unit)
    else:
        angle_unit = "Deg"
        unit_button.config(text=angle_unit)
    calculate(False) # Calculating Expression(Result) after pressing Deg/Rad Button.


angle_unit = 'Deg'
# Button values
button_values = [
    ('  7', '8', '9', '/',angle_unit,'cbrt(','facto('),
    ('  4', '5', '6', '×','sin( ','  ln( ','    ^   '),
    ('  1', '2', '3', ' -','cos(',' log(','    ²   '),
    ('  0', 'C', '=', '+','tan( ','  pi ','    ³   '),
    ('<<', '(', ')', ' .','sqrt(','  e  ','HCF & LCM')
]

# Creating buttons
for i, row in enumerate(button_values):
    for j, value in enumerate(row):
        
        if i==0 and j==4:
            unit_button = tk.Button(root,text=value,command=toggle_unit,padx=40,pady=20,font='Arial 12')
            unit_button.grid(row=i+2,column=j,padx=5,pady=5)
            continue
        if value == "HCF & LCM":
            btn = tk.Button(root,text=value,padx=25,pady=25)
            btn.grid(row=i+2,column=j)
            continue

        btn = tk.Button(root, text=value, padx=40, pady=20,font= 'Arial 12')
        if value == '=':
            btn.config(command=lambda equal_to_flag = True: calculate(equal_to_flag))
        elif value == 'C':
            btn.config(command=main.clear_display)
        elif value == '<<':
            btn.config(command=main.backspace)
        else:
            btn.config(command=lambda v=value.strip(): main.update_display(v)) #strip() function removed white space which is used for adjustment.
        btn.grid(row=i + 2, column=j)   
        # row = i+ 2 , because 0th row is reserved for entry_display and 1st row is reserved for result_label Label.

root.mainloop()