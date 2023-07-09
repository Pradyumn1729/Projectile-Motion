from tkinter import *
import math
root = Tk()
root.title("Projectile_Motion")
root.geometry("1500x1500")
my_canvas=Canvas(root, width=1200 , height=400 , bg="white")
my_canvas.pack(pady=100)


def Start():
    start.config(state=DISABLED)
    stop.config(state=NORMAL)
    xo = 50
    yo = 350
    theta = 45
    theta *= math.pi / 180
    u = 100
    t=0
    t1=0.1
    g = 9.8
    _R = ((u * u) * math.sin(2 * theta)) / g
    x = xo
    y = yo
    while(y<=yo):
        y = yo - u * math.sin(theta) * t + 0.5 * g * t ** 2
        x = xo + u * math.cos(theta) * t
        my_canvas.delete("ball")
        my_canvas.create_oval(x-10 , y-10, x+10 ,y+10 ,fill="purple", tags="ball")
        my_canvas.update()
        t += t1
        root.after(10)

def Stop():
    start.config(state=NORMAL)
    stop.config(state=DISABLED)
    x, y, _, _ = my_canvas.coords("ball")
    print("x position:", x)
    print("y position:", y)


start=Button(root,text="Start",command=Start)
start.pack()
stop=Button(root,text="Stop",command=Stop)
stop.pack()
root.mainloop()

