from tkinter import *
from tkinter import messagebox
import converter
from expressiontree import ExpressionTree
import integrate

# This is the main class that runs the GUI using tkinter for the integral calculator. This programs creates
# the GUI that asks for the user to give a function, upper bound, lower bound, and number of subintervals. Then,
# this class does some error checking to make sure the inputs were valid. Then the function is passed into the
# converter.py file to create the postfix expression. Then the postfix expression is used to create an expression
# tree that can evaluate the function for a given input. Finally, the result is calculated with the help of the
# integrate.py file and its methods. Finally, the output it displayed to the screen.

root = Tk()
root.title('Integral Calculator')

# This function, taking in user arguments, actually does the calculation of the integral and displays the result
# on the tkinter window
def calculate(low, up, rec):
    infix_list = converter.formatting(func.get())
    postfix_list = converter.make_postfix(infix_list)
    # Checks if the user's expression was valid by seeing if the expression tree can be made
    try:
        expression = ExpressionTree(postfix_list)
    except IndexError:
        messagebox.showerror('Error', 'Invalid function syntax')
        return
    try:
        result = integrate.solve(expression, low, up, rec)
    # Checking for a situation such as integrating 1/x with bounds [0, 1]
    except ZeroDivisionError:
        messagebox.showerror('Error', 'Function can not be integrated with current bounds')
        return
    except MemoryError:
        messagebox.showerror('Error', 'Function can not be integrated with current bounds')
        return
    ans.config(text='Result: ' + str(result))

# This function checks the user inputs to the calculator were valid before any calculations are done
def check_errors():
    ans.config(text='')
    # Checks if the user put in valid lower and upper bounds
    try:
        low = float(lower.get())
        up = float(upper.get())
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers for the bounds. No fractions allowed')
        return
    # Checks the user put in a valid amount of intervals
    try:
        rec = int(rect.get())
    except ValueError:
        messagebox.showerror('Error', 'Please enter a valid whole number for the number of subintervals')
        return
    if rec < 2 or rec % 2 == 1:
        messagebox.showerror('Error', 'The number of subintervals must be even and greater than zero')
        return
    # Checks that the function box is not empty
    if len(func.get()) == 0:
        messagebox.showerror('Error', 'Please do not leave the function box empty')
        return
    # Checks from that the function has an equal amount of opening anc closing parentheses
    if not converter.valid_parentheses(func.get()):
        messagebox.showerror('Error', 'Function does not having equal opening and closing parentheses')
        return
    # Checks that the user only input valid tokens into the function box
    if not converter.valid_symbols(func.get()):
        messagebox.showerror('Error', 'Function has invalid symbols in it')
        return
    # If there were no errors now the integral can be calculated
    calculate(low, up, rec)

# Adds labels to the tkinter frame that display text about what each entry box means
label1 = Label(root, text='Function     f(x) =', font='Arial 12')
label1.grid(row=0, column=0, sticky='E')
label2 = Label(root, text='Lower limit', font='Arial 12')
label2.grid(row=1, column=0)
label3 = Label(root, text='Upper limit', font='Arial 12')
label3.grid(row=2, column=0)
label3 = Label(root, text='Number of subintervals', font='Arial 12')
label3.grid(row=3, column=0)

# Creates the entry boxes where the user can put in information
func = Entry(root, font='Arial 12', width=30)
func.grid(row=0, column=1, sticky='W', padx=(0, 20), pady=(4, 0))
lower = Entry(root, font='Arial 12', width=10)
lower.grid(row=1, column=1, sticky='W', padx=(0, 20))
upper = Entry(root, font='Arial 12', width=10)
upper.grid(row=2, column=1, sticky='W', padx=(0, 20))
rect = Entry(root, font='Arial 12', width=10)
rect.grid(row=3, column=1, sticky='W', padx=(0, 20))

# Button the user will click to get the answer for their integral
button = Button(root, text='Calculate', font='Arial 12', width=16, command=check_errors)
button.grid(row=4, column=0, columnspan=2, pady=(8, 8))

# This label will display the answer to the integral when the button is clicked
ans = Label(root, text="", font='Arial 12')
ans.grid(row=5, column=0, columnspan=2)

root.mainloop()