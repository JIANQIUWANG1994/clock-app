from tkinter import *
import time

main = Tk()
main.title('Digital Clock')
main.geometry("500x300")

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    time_zone = time.strftime("%Z")

    my_clock.config(text=hour + ":" + minute + ":" + second)
    my_clock.after(1000,clock)

    my_label2.config(text=day + " " + time_zone)


my_clock = Label(main, text="", font=("Arial", 80), fg="blue", bg="white")
my_clock.pack(pady=20)

my_label2 = Label(main, text="", font=("Arial", 14))
my_label2.pack(pady=10)

clock()

main.mainloop()