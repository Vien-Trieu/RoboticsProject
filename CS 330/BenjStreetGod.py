import keyboard
from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from tkinter import filedialog
from allCode import *
from PIL import Image, ImageTk
# root = Tk() 
# canvas = Canvas(root, width = 3000, height = 3000)  
# canvas.pack()  
# img = ImageTk.PhotoImage(Image.open("/Users/raiz/Desktop/Screenshot 2023-05-02 at 10.24.18 PM.png"))  
# canvas.create_image(2000, 1993, anchor=NW, image=img) 



# # def open_image():
# #     file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
# #     if file_path:
# #         image = Image.open(file_path)
# #         photo = ImageTk.PhotoImage(image)
# #         canvas.config(width=image.width, height=image.height)
# #         canvas.create_image(0, 0, anchor=tk.NW, image=photo)
# #         canvas.image = photo
# # #GUI
# # root = tk.Tk()
# # root.title("GUI")
# # canvas = tk.Canvas(root, width=500, height=500)
# # canvas.pack()

# def on_key_press(key):
#     print(f'Key pressed: {key}')
# # Load and add an image to the window
# key_w = tk.Button(canvas, text='W',command=lambda: on_key_press('w'))
# key_a = tk.Button(canvas, text='A', command=lambda: on_key_press('a'))
# key_s = tk.Button(canvas, text='S', command=lambda: on_key_press('s'))
# key_d = tk.Button(canvas, text='D', command=lambda: on_key_press('d'))
# key_w.pack(side=tk.TOP)
# key_a.pack(side=tk.LEFT)
# key_s.pack(side=tk.LEFT)
# key_d.pack(side=tk.LEFT)
# canvas.mainloop()







Robot = Robot('COM6',115200)
Robot.connection_and_start()
time.sleep(0.1)

w_pressed = False
a_pressed = False
s_pressed = False
d_pressed = False
wa_pressed = False
#W key hook code
def on_press_w(e):
    global w_pressed
    if not w_pressed:
        Robot.drive_forward()
        print("Going forward")
        w_pressed = True
def on_release_w(e):
    global w_pressed
    print('Stopped')
    Robot.drive_stop()
    w_pressed = False

#W and A key hook
def on_press_a(e):
    global a_pressed
    global w_pressed

    if w_pressed and not a_pressed:
        Robot.drive_turn_left()
    a_pressed = True

def on_release_a(e):
    global a_pressed
    global w_pressed
    if w_pressed and a_pressed:
        Robot.drive_stop()
    a_pressed = False


#A key hook code
def on_press_a(e):
    global a_pressed
    if not a_pressed:
        Robot.drive_turn_left()
        print("Going left")
        a_pressed = True
def on_release_a(e):
    global a_pressed
    print('Stopped')
    Robot.drive_stop()
    a_pressed = False

#S key hook code
def on_press_s(e):
    global s_pressed
    if not s_pressed:
        Robot.drive_backwards()
        print("Going backwards")
        s_pressed = True
def on_release_s(e):
    global s_pressed
    print('Stopped')
    Robot.drive_stop()
    s_pressed = False

#D key hook code
def on_press_d(e):
    global d_pressed
    if not d_pressed:
        Robot.drive_turn_right()
        print("Going right")
        d_pressed = True
def on_release_d(e):
    global d_pressed
    print('Stopped')
    Robot.drive_stop()
    d_pressed = False

# #w and a key hook 
# def on_press_wa(e):
#     global wa_pressed
#     if keyboard.is_pressed('w') and keyboard.is_pressed('a'):
#         Robot.drive_curve_left()
#         print("Going right")
#         wa_pressed = True
# def on_release_wa(e):
#     global wa_pressed
#     print('Stopped')
#     Robot.drive_stop()
#     wa_pressed = False


#Set up the keyboard event hook
keyboard.on_press_key('w',on_press_w)
keyboard.on_release_key('w', on_release_w)

keyboard.on_press_key('a',on_press_a)
keyboard.on_release_key('a', on_release_a)

keyboard.on_press_key('s',on_press_s)
keyboard.on_release_key('s', on_release_s)

keyboard.on_press_key('d',on_press_d)
keyboard.on_release_key('d', on_release_d)

#keyboard.on_press_key('w' and 'a', on_press_wa)
#keyboard.on_release_key('w' and 'a', on_release_wa)


try:
    keyboard.wait()
except KeyboardInterrupt:
    # Handle Ctrl+C to exit gracefully
    print("Exiting...")
finally:
    keyboard.unhook_all()


