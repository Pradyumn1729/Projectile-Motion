import tkinter as tk
import math

root = tk.Tk()
root.title("Projectile Motion")

canvas_width = 1200
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
v0 = 100
angle = math.pi / 4
vx = v0 * math.cos(angle)
vy = -v0 * math.sin(angle)
y0 = canvas_height - 50

def start_projectile_motion():
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    x0 = 50
    y0 = canvas_height - 50
    v0 = 100
    angle = math.pi / 4
    t = 0
    dt = 0.1
    x = x0
    y = y0
    vx = v0 * math.cos(angle)
    vy = -v0 * math.sin(angle)
    while y <= y0:
        x = x0 + vx * t
        y = y0 + vy * t + 0.5 * 9.81 * t ** 2
        canvas.delete("ball")
        canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="red", tags="ball")
        canvas.update()
        t += dt
        animation_id = root.after(10)

    return animation_id

def stop_projectile_motion():

    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    x, y, _, _ = canvas.coords("ball")
    time_of_flight = (y0 - y) / (-vy)
    print("x position:", x)
    print("y position:", y)
    print("time of flight:", time_of_flight)
    canvas.after_cancel()




start_button = tk.Button(root, text="Start", command=start_projectile_motion)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_projectile_motion, state=tk.DISABLED)
stop_button.pack()

root.mainloop()
