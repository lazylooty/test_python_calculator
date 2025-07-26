import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self,master):
        self.master = master
        self.inputdata = ''
        self.master.title('Calculator')
        self.master.iconbitmap('main.ico')
        self.master.geometry('400x400')
        self.master.minsize(300,300)

        self.current_input = '0'
        self.display = ttk.Entry(master, width=30, font=('JetBrains Mono', 24, 'bold'), justify='right')
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipadx=5, ipady=10, sticky='nsew')
        self.display.insert(0, self.current_input)

        for i in range(5): self.master.grid_columnconfigure(i, weight=1)
        for i in range(5): self.master.grid_rowconfigure(i, weight=1)

        self.buttons_num = {
            '7': (1,0), '8': (1,1), '9': (1,2),
            '4': (2,0), '5': (2,1), '6': (2,2),
            '1': (3,0), '2': (3,1), '3': (3,2),
            '.': (4,0), '0': (4,1)
        }
        self.buttons_func = {
            '+': (2,3), '-': (2,4),
            'x': (3,3), '/': (3,4)
        }

        self.style = ttk.Style()
        self.style.theme_use('clam') 
        self.style.configure('TButton', 
                             font=('JetBrains Mono', 14, 'bold'),
                             background='#E0E0E0',
                             foreground='black',
                             borderwidth=1, relief='flat') 
        self.style.map('TButton',
                       background=[('active', '#C0C0C0'), ('!active', '#E0E0E0')],
                       foreground=[('active', 'black'), ('!active', 'black')])

        self.style.configure('C.TButton', 
                             font=('JetBrains Mono', 14, 'bold'), 
                             background='red',
                             foreground='white',
                             borderwidth=1) 
        self.style.map('C.TButton',
                       background=[('active', "#914848"), ('!active', "#FF5858")],
                       foreground=[('active', 'white'), ('!active', 'black')])

        self.style.configure('Equal.TButton', 
                             font=('JetBrains Mono', 14, 'bold'), 
                             background='green',
                             foreground='white',
                             borderwidth=1) 
        self.style.map('Equal.TButton',
                       background=[('active',  "#2B5F43"), ('!active', "#3E8A60")],
                       foreground=[('active', 'white'), ('!active', 'black')])
        
        for num, tupl in self.buttons_num.items():
            btn = ttk.Button(self.master, text=num,  command=lambda b=num: self._click_button(b))
            btn.grid(row=tupl[0], column=tupl[1], padx=5, pady=5, ipady=5, ipadx=5, sticky='nsew')
        
        for func, tupl in self.buttons_func.items():
            btn = ttk.Button(self.master, text=func, command=lambda b=func: self._click_button(b))
            btn.grid(row=tupl[0], column=tupl[1], padx=5, pady=5, ipady=5, ipadx=5, sticky='nsew')
        
        self.c_btn = ttk.Button(self.master, text='C', style='C.TButton', command=self._clear_display)
        self.c_btn.grid(row=1, column=3, columnspan=2, padx=5, pady=5, ipady=5, ipadx=5, sticky='nsew')

        self.return_button = ttk.Button(self.master, text='=', style='Equal.TButton', command=self._return_button)
        self.return_button.grid(row=4, column=2, columnspan=3, padx=5, pady=5, ipady=5, ipadx=5, sticky='nsew')
    
    def _click_button(self,b):
        if self.current_input == '0':
            self.current_input = b
        elif b =='x':
            self.current_input += '*'   
        elif b == '.':
            operators = ['*','-','+','/']
            idx_op = int()
            for i in operators:
                if i in self.current_input:
                    if idx_op < self.current_input.rfind(i):
                        idx_op = self.current_input.rfind(i)

            if idx_op:
                if b not in self.current_input[idx_op+1:]:
                    self.current_input += b
                
            else:
                if b not in self.current_input:
                    self.current_input += b

        else:
            self.current_input += b

        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_input)

    def _clear_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, '0')
        self.current_input = '0'
    
    def _return_button(self):
        try:
            result = eval(self.current_input)
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
            self.current_input = str(result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, 'ERROR')
            self.current_input = '0'
    
root = tk.Tk()
CalculatorApp(root)
root.mainloop()