# calculator_app.py
import tkinter as tk

class CalculatorApp:
   def __init__(self, master):
      self.master = master
      master.title("Калькулятор")
      self.display = tk.Entry(master, width=25, borderwidth=5, relief="sunken", font=('Arial', 16), justify="left")
      self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
      self.display.insert(0, "gaysex")

if __name__ == "__main__":
    root = tk.Tk()
    my_calculator = CalculatorApp(root)
    root.mainloop()      