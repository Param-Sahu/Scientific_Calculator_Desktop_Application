import tkinter as tk
from math import sin,cos,tan,log,log10,cbrt,sqrt,pi,e,factorial,gcd,lcm,exp
import matrix

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
        self.entry_display.xview_moveto(1) # Automatically shift Scrollbar after pressing backspace button.
        calculate(False) # Calculating Expression(Result) after pressing backspace button and printing on result_label.
    
    # GUI Class End


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
                        'facto':factorial,'exp':exp}
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
        
        # Try block end.

    except:  # Error Handling 
        if flag == True:  # printing Error message on entry_display if any error encountered after pressing = button.
            main.entry_display.delete(0,tk.END)
            main.entry_display.insert(tk.END, "Error")
        else : 
            result_label.config(text='',borderwidth=2) # Printing nothing on result_label in case of any error .
            result_label.grid(row=1,columnspan=4,column=0,padx=2,pady=2)
    
    # calculate function end.


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
    # toggle_unit function end.


def calculate_HCFLCM(functions):
    
    try:
        global label_hcf,label_lcm
        window = functions
        #Function to Calculate HCF and LCM.
        num = (window.entry_display.get()).split(sep=',')
        while '' in num:
            num.remove('')
        numbers = [int(x) for x in num]
        HCF = gcd(*numbers)
        LCM = lcm(*numbers)
        label_hcf.config(text=f'HCF : {HCF}')
        label_hcf.grid(row=7,column=0,columnspan=3)
        label_lcm.config(text=f'LCM : {LCM}')
        label_lcm.grid(row=8,column=0,columnspan=3)
    except:
        label_hcf.config(text='HCF : ')
        label_lcm.config(text='LCM : ')
    # Calculate HCF LCM function End.

def calculate_average(functions):
    try :
        global label_avg
        num = (functions.entry_display.get()).split(sep=',')
        while '' in num:
            num.remove('')
        numbers = [float(x) for x in num]
        average = sum(numbers)/len(numbers)
        label_avg.config(text=f'Average :  {average}')
        label_avg.grid(row=7,column=0,columnspan=3)
    except:
        label_avg.config(text='Average : ')
    


def open_window(flag,title):
    global entry,label_hcf,label_lcm,label_avg,new_window
    new_window = tk.Tk() # Creating Window for HCF and LCM calculator.
    if flag == 'hcflcm':
        label_hcf = tk.Label(new_window,text='HCF : ',font='Arial 12')
        label_lcm = tk.Label(new_window,text='LCM : ',font='Arial 12')
    elif flag == 'avg':
        label_avg = tk.Label(new_window,text='Average : ',font='Arial 12')
    window_function = GUI(new_window,title) # Accessing GUI Function like entry, clear_display etc.
    info_label = tk.Label(new_window,text=f'Enter comma seperated values',font='Calibri 13')
    info_label.grid(row=0,column=0,columnspan=3)
    entry = tk.Entry(new_window,width=30,borderwidth=5,font='Arial 12')
    entry.grid(row=1,column=0,columnspan=3)
    window_function.entry(entry)  # Accessing Entry widget in GUI Class.

    # Defining Buttons
    Buttons = [
                        ('7', '8', '9'),
                        ('4', '5', '6'),
                        ('1', '2', '3'),
                        ('0', 'C','<<'),
                        (',','ANS')
                        ]
    # Arranging Buttons
    for i,row in enumerate(Buttons):
        for j,value in enumerate(row):
            if value == 'C':
                button  = tk.Button(new_window,text=value,command= lambda : entry.delete(0,tk.END),padx=38,pady=20,font='Arial 12')
            elif value == '<<':
                button = tk.Button(new_window,text=value,command=window_function.backspace,padx=35,pady=20,font='Arial 12')
            elif value == 'ANS':
                if flag == 'hcflcm':
                    button = tk.Button(new_window,text=value,command=lambda v =window_function:calculate_HCFLCM(v),padx=30,pady=20,font='Arial 12')
                elif flag == 'avg':
                    button = tk.Button(new_window,text=value,command=lambda v =window_function:calculate_average(v),padx=30,pady=20,font='Arial 12')                    
            else : 
                button = tk.Button(new_window,text=value,command=lambda  V = value: window_function.update_display(V),padx=40,pady=20,font='Arial 12')
                # lambda V = value : remember all values at their particular time ,
                # If V not used and direct value pass as argument it will remember only last value.

            button.grid(row=i+2,column=j)





# Graphical User Interface Creation

root = tk.Tk() #Creating Window
root.iconbitmap('calculator.ico') # Set Icon image of Calculator Window.
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

special_label = tk.Label(root,text='Advanced Calculators',font='Arial 14')
special_label.grid(row=1,column=7)

angle_unit = 'Deg'
# Button values
button_values = [
    ('  7', '8', '9', '/',angle_unit,'cbrt(','facto(','Determinant'),
    ('  4', '5', '6', '×','sin( ','  ln( ','    ^   ','Inverse'),
    ('  1', '2', '3', ' -','cos(',' log(','    ²   ','Eigen Value'),
    ('  0', 'C', '=', '+','tan( ','  pi ','    ³   ','HCF & LCM'),
    ('<<', '(', ')', ' .','sqrt(','  e  ','exp(','Average Calculator')
]


# Creating buttons
for i, row in enumerate(button_values):
    for j, value in enumerate(row):
        
        if i==0 and j==4:
            unit_button = tk.Button(root,text=value,command=toggle_unit,padx=40,pady=20,font='Arial 12')
            unit_button.grid(row=i+2,column=j,padx=5,pady=5)
            continue
        if value == "HCF & LCM":
            btn = tk.Button(root,text=value,padx=50,pady=20,command=lambda :open_window('hcflcm',"HCF & LCM Calculator"),font='Calibri 12')
            btn.grid(row=i+2,column=j)
            continue

        btn = tk.Button(root, text=value, padx=40, pady=20,font= 'Arial 12')
        if value == '=':
            btn.config(command=lambda equal_to_flag = True: calculate(equal_to_flag))
        elif value == 'C':
            btn.config(command=main.clear_display)
        elif value == "Determinant":
            btn.config(text=' Determinant ',command=matrix.determinant)
        elif value == "Inverse":
            btn.config(text='     Inverse      ',command= matrix.inverse)
        elif value == "Eigen Value":
            btn.config(text='Eigen Values',command= matrix.eigen_values)
        elif value == "Average Calculator":
            btn.config(text='Average Calculator',font='Calibri 13',padx=20,pady=17,command= lambda : open_window('avg','Average Calculator'))
        elif value == '<<':
            btn.config(command=main.backspace)
        else:
            btn.config(command=lambda v=value.strip(): main.update_display(v)) #strip() function removed white space which is used for adjustment.
        btn.grid(row=i + 2, column=j)   
        # row = i+ 2 , because 0th row is reserved for entry_display and 1st row is reserved for result_label Label.


# Bind the destroy event of the root window to the on_root_destroy function
def on_root_destroy(event):
    global new_window
    try:
        while new_window.winfo_exists():
            new_window.destroy()
    except:
        pass
root.bind("<Destroy>", on_root_destroy)
root.mainloop()