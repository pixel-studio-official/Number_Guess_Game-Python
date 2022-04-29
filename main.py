import tkinter as tk
import tkinter.messagebox as mg
import random as rd

def game():
    global num
    num = 0

    app = tk.Tk()
    app.title("Number Guessing Game")

    r_num = rd.randint(0, 20)
    _try = tk.Label(app, text=f"Trys = 0")
    _try.pack()
    bs = tk.Label(app, text="?", font=("Arial", "30"))
    bs.pack()
    _input = tk.Entry(app)
    _input.pack()

    def check():
        text = _input.get()
        if r_num == int(text):
            bs.config(text="=")
            msg = mg.askyesno("You Won", "Good News The Number You Have Entered Is Correct!\n Do You Want To Continue")
            if msg:
                app.destroy()
                game()
            else:
                app.destroy()
        else:
            global num
            num = num+1
            _try.config(text=f"Trys = {num}")
            if int(text) < r_num:
                bs.config(text="<")
            if int(text) > r_num:
                bs.config(text=">")


    tk.Button(app, text="Check", command=check).pack()

    app.mainloop()
game()
