import tkinter as tk
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen.get()))
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen.get() + text)
root = tk.Tk()

root.title("Calculator")
screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold")
screen.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)
btns = [ ['7','8','9','/'],
         ['4','5','6','*'],
         ['1','2','3','-'],
         ['0','C','=','+'] ]
for row in btns:
    frame = tk.Frame(root)
    frame.pack()
    for char in row:
        btn = tk.Button(frame, text=char, font="lucida 15 bold", width=6, height=2)
        btn.pack(side=tk.LEFT, padx=2, pady=2)
        btn.bind("<Button-1>", click)
root.mainloop()
