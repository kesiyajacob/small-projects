import tkinter as tk

calculation = ""
def addToCalculation(symbol):
    global calculation
    calculation += str(symbol)
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)


def evaluateCalculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        textResult.delete(1.0, "end")
        textResult.insert(1.0, calculation)
    except:
        clearField()
        textResult.insert(1.0, "Error")


def clearField():
    global calculation
    calculation = ""
    textResult.delete(1.0, "end")


root = tk.Tk()
root.geometry("325x300")


# TEXT BOX
textResult = tk.Text(root, height=2, width=21, font=("Ariel", 24))
textResult.grid(columnspan=5)


# NUMBER BUTTONS
# lambda allows parameters to be passed easily
btn1 = tk.Button(root, text="1", command=lambda: addToCalculation(1), height=2, width=5, font=("Ariel", 14))
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text="2", command=lambda: addToCalculation(2), height=2, width=5, font=("Ariel", 14))
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text="3", command=lambda: addToCalculation(3), height=2, width=5, font=("Ariel", 14))
btn3.grid(row=2, column=3)
btn4 = tk.Button(root, text="4", command=lambda: addToCalculation(4), height=2, width=5, font=("Ariel", 14))
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command=lambda: addToCalculation(5), height=2, width=5, font=("Ariel", 14))
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command=lambda: addToCalculation(6), height=2, width=5, font=("Ariel", 14))
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command=lambda: addToCalculation(7), height=2, width=5, font=("Ariel", 14))
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text="8", command=lambda: addToCalculation(8), height=2, width=5, font=("Ariel", 14))
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text="9", command=lambda: addToCalculation(9), height=2, width=5, font=("Ariel", 14))
btn9.grid(row=4, column=3)
btn0 = tk.Button(root, text="0", command=lambda: addToCalculation(0), height=2, width=5, font=("Ariel", 14))
btn0.grid(row=5, column=2)


# OPERATIONS
btnPlus = tk.Button(root, text="+", command=lambda: addToCalculation("+"), height=2, width=5, font=("Ariel", 14))
btnPlus.grid(row=2, column=4)
btnMinus = tk.Button(root, text="-", command=lambda: addToCalculation("-"), height=2, width=5, font=("Ariel", 14))
btnMinus.grid(row=3, column=4)
btnMul = tk.Button(root, text="x", command=lambda: addToCalculation("*"), height=2, width=5, font=("Ariel", 14))
btnMul.grid(row=4, column=4)
btnDiv = tk.Button(root, text="/", command=lambda: addToCalculation("/"), height=2, width=5, font=("Ariel", 14))
btnDiv.grid(row=5, column=4)

# BRACKETS
btnOpen = tk.Button(root, text="(", command=lambda: addToCalculation("("), height=2, width=5, font=("Ariel", 14))
btnOpen.grid(row=5, column=1)
btnClose = tk.Button(root, text=")", command=lambda: addToCalculation(")"), height=2, width=5, font=("Ariel", 14))
btnClose.grid(row=5, column=3)

# EQUALS + CLEAR
btnEquals = tk.Button(root, text="=", command=evaluateCalculation, height=2, width=14, font=("Ariel", 14))
btnEquals.grid(row=6, column=3, columnspan=2)

# No lambda b/c not taking any parameters, also no parentheses beside clearField because we want to pass the function,
# not call it
btnClear = tk.Button(root, text="C", command=clearField, height=2, width=14, font=("Ariel", 14))
btnClear.grid(row=6, column=1, columnspan=2)

root.mainloop()

