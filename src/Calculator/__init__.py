import tkinter
import math

class Calculator(object):
    
    def equals(self):
        try: 
            self.value = eval(self.ent.get())
        except SyntaxError or NameError:
            self.clearAll()
            self.ent.insert(0, "Incorrect input")
        else:
            self.clearAll()
            self.ent.insert(0, self.value)
        
    def squareroot(self):
        try: 
            self.value = eval(self.ent.get())
        except SyntaxError or NameError:
            self.clearAll()
            self.ent.insert(0, "Incorrect input")
        else:
            self.value = math.sqrt(self.value)
            self.clearAll()
            self.ent.insert(0, self.value)
    
    def square(self):
        try: 
            self.value = eval(self.ent.get())
        except SyntaxError or NameError:
            self.clearAll()
            self.ent.insert(0, "Incorrect input")
        else:
            self.value = math.pow(self.value, 2)
            self.clearAll()
            self.ent.insert(0, self.value)
             
    def clear1(self):
        end = len(self.ent.get())
        self.ent.delete(end - 1, end)
        
    def clearAll(self):
        end = len(self.ent.get())
        self.ent.delete(0, end)
        
    def action(self, arg):
        end = len(self.ent.get())
        self.ent.insert(end, arg) 

    
    def __init__(self, window):
        '''
        Constructor
        '''
        # window = tkinter.Tk()
        window.title("Calculator")
        window.geometry()
        self.ent = tkinter.Entry(window, width=30)
        self.ent.grid(row=0, column=0, columnspan=20, pady=10)
        self.ent.focus_set()
        
        tkinter.Button(window, relief="flat", background="#ECA6FF", text="=", width=12, command=lambda:self.equals()).grid(row=4, column=4, columnspan=2)
        tkinter.Button(window, relief="flat", background="#FF5733", text='AC', width=5, command=lambda:self.clearAll()).grid(row=1, column=4)
        tkinter.Button(window, relief="flat", background="#FF5733", text='C', width=5, command=lambda:self.clear1()).grid(row=1, column=5)
        tkinter.Button(window, relief="flat", background="#ECA6FF", text="+", width=5, command=lambda:self.action('+')).grid(row=4, column=3)
        tkinter.Button(window, relief="flat", background="#ECA6FF", text="x", width=5, command=lambda:self.action('*')).grid(row=2, column=3)
        tkinter.Button(window, relief="flat", background="#ECA6FF", text="-", width=5, command=lambda:self.action('-')).grid(row=3, column=3)
        tkinter.Button(window, relief="flat", background="#ECA6FF", text="/", width=5, command=lambda:self.action("/")).grid(row=1, column=3) 
        tkinter.Button(window, relief="flat", background="#ECA6FF", text="%", width=5, command=lambda:self.action('%')).grid(row=4, column=2)
        tkinter.Button(window, relief="flat", background="#FFDA33", text="7", width=5, command=lambda:self.action(7)).grid(row=1, column=0)
        tkinter.Button(window, relief="flat", background="#FFDA33", text="8", width=5, command=lambda:self.action(8)).grid(row=1, column=1)
        tkinter.Button(window, relief="flat", background="#FFDA33", text="9", width=5, command=lambda:self.action(9)).grid(row=1, column=2)
        tkinter.Button(window, relief="flat", background="#FFDA33", text="4", width=5, command=lambda:self.action(4)).grid(row=2, column=0)
        tkinter.Button(window, relief="flat", background="#FFDA33", text="5", width=5, command=lambda:self.action(5)).grid(row=2, column=1)
        tkinter.Button(window, relief="flat", background="#FFDA33", text="6", width=5, command=lambda:self.action(6)).grid(row=2, column=2)
        tkinter.Button(window, relief="flat", background="#FFDA33", text="1", width=5, command=lambda:self.action(1)).grid(row=3, column=0)
        tkinter.Button(window, relief="flat", background="#FFDA33", text="2", width=5, command=lambda:self.action(2)).grid(row=3, column=1)
        tkinter.Button(window, relief="flat", background="#FFDA33", text="3", width=5, command=lambda:self.action(3)).grid(row=3, column=2)
        tkinter.Button(window, relief="flat", background="#FFDA33", text="0", width=5, command=lambda:self.action(0)).grid(row=4, column=0)
        tkinter.Button(window, relief="flat", background="#ECA6FF", text=".", width=5, command=lambda:self.action('.')).grid(row=4, column=1)
        tkinter.Button(window, relief="flat", background="#ECA6FF", text="(", width=5, command=lambda:self.action('(')).grid(row=2, column=4)
        tkinter.Button(window, relief="flat", background="#ECA6FF", text=")", width=5, command=lambda:self.action(')')).grid(row=2, column=5)
        tkinter.Button(window, relief="flat", background="#ECA6FF", text="sqR", width=5, command=lambda:self.squareroot()).grid(row=3, column=4)
        tkinter.Button(window, relief="flat", background="#ECA6FF", text="x*x", width=5, command=lambda:self.square()).grid(row=3, column=5)
        
        window.configure(background="#a1dbcd")
        
        
root = tkinter.Tk()
obj = Calculator(root)
root.mainloop()
