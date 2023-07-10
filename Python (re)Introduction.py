from tkinter import *
import webbrowser

# in this project im going to make buttons that link websites to them.

parentwindow = Tk()
parentwindow.geometry('990x540')
parentwindow.title("webpage")

def open():
    webbrowser.open("https://github.com/liamhardman10")


def click():
    print("button has been clicked.")


photo1 = PhotoImage(file=r"C:\Users\Liam\Downloads\GitHub.png")

button1 = Button(parentwindow,
                text="My GitHub ",
                command=open,
                font=("Helvetica", 50),
                fg="white",
                bg="#554e74",
                activeforeground="#b0b0b0",
                activebackground="#38334c",
                state=ACTIVE,
                image=photo1,
                compound='right')
                
photo2 = PhotoImage(file=r"C:\Users\Liam\Downloads\LinkedIn.png")


button2 = Button(parentwindow,
                text="My LinkedIn ",
                command=open,
                font=("Helvetica", 50),
                fg="white",
                bg="#554e74",
                activeforeground="#b0b0b0",
                activebackground="#38334c",
                state=ACTIVE,
                image=photo2,
                compound='right')




    


button1.pack()

button2.pack()

parentwindow.mainloop()
