import keyboard
import tk
import tkinter
from tkinter import Tk
from tkinter import *
import tkinter as tk


def move(direction):
    if direction == 'w':
        canvas.move(player, 0, -5)
    elif direction == 'a':
        canvas.move(player, -5, 0)
    elif direction == 's':
        canvas.move(player, 0, 5)
    elif direction == 'd':
        canvas.move(player, 5, 0)

def on_key_press(event):
    direction = event.keysym.lower()
    if direction in ['w', 'a', 's', 'd']:
        move(direction)

def on_button_click(direction):
    move(direction)

root = tk.Tk()
root.title("Canvas with WASD Controls")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

# Create a player (rectangle) on the canvas
player = canvas.create_rectangle(50, 50, 70, 70, fill="blue")

def change_color(color):
    canvas.itemconfig(player, fill=color)

button_orange = tk.Button(root, text="ORANGE", command=lambda: change_color('orange'))
button_red = tk.Button(root, text="RED", command=lambda: change_color('red'))
button_green = tk.Button(root, text="GREEN", command=lambda: change_color('green'))
button_yellow = tk.Button(root, text="YELLOW", command=lambda: change_color('yellow'))

# Position the color buttons
button_orange.place(x=20, y=350)
button_red.place(x=100, y=350)
button_green.place(x=180, y=350)
button_yellow.place(x=260, y=350)

# Create buttons for 'w', 'a', 's', 'd'
button_w = tk.Button(root, text="W", command=lambda: on_button_click('w'))
button_a = tk.Button(root, text="A", command=lambda: on_button_click('a'))
button_s = tk.Button(root, text="S", command=lambda: on_button_click('s'))
button_d = tk.Button(root, text="D", command=lambda: on_button_click('d'))

# Position the buttons
button_w.place(x=50, y=250)
button_a.place(x=20, y=280)
button_s.place(x=50, y=310)
button_d.place(x=80, y=280)

# Bind the canvas to the keyboard events
root.bind("<KeyPress>", on_key_press)

# Make sure the canvas has focus to capture the keyboard events
canvas.focus_set()

root.mainloop()
