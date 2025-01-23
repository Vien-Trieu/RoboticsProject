# """Created By Vien Trieu and Raiz Mohammed 
#    Created on 10/5/2023 
#    This code is set up to make the iRobot Create 2 drive 4 feet then turn and drive 4 feet then turn four times. We used many different types of methods but ended up just using the regular time.sleep
#    Once we got it to finally drive four feet and stop, we just copied and pasted to see how it would do, and it liked to just do its own thing and we tweaked the last two drive and turns as they were not
#    allowing us to drive the robot right on the tape. We also have this code splt up to show where each drive and turn is. This robot now should be able to drive 4 feet turn and do this 4 times to make a
#    a perfect square."""
import serial
import time

# start commands
START = b"\x80"
RESET = b"\x07"
SAFE_MODE = b"\x83"



DRIVE_FORWARD = b"\x91\x01\x32\x01\x32" 
DRIVE_BACKWARDS = b"\x89\xFF\x40\x40\x00" 
TURN_RIGHT = b"\x91\xC8\x40\x40\x40"

STOP = b"\x91\x00\x00\x00\x00"





class Robot:

    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.connection = serial.Serial(port, baudrate=baudrate, timeout=1)



    def connection_and_start(self):
        # Opening the port
        #self.connection.open()
        # Start up
        self.connection.write(START)
        print("Start")
        self.connection.write(START+SAFE_MODE)
        time.sleep(2)

    def drive_forward(self):
        #print("Driving Forward")
        self.connection.write(DRIVE_FORWARD)
        #time.sleep(duration)

    def drive_backwards(self):
        #print("Driving Backwards")
        self.connection.write(DRIVE_BACKWARDS)
        #time.sleep(duration)

    def drive_turn(self):
       # print("Turning")
        self.connection.write(TURN_RIGHT)
        #time.sleep(duration)

    def drive_stop(self):
        print("Stopping")
        self.connection.write(STOP)
        #time.sleep(duration)

    


# def open_image():
#     file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
#     if file_path:
#         image = Image.open(file_path)
#         photo = ImageTk.PhotoImage(image)
#         canvas.config(width=image.width, height=image.height)
#         canvas.create_image(1000, 1000, anchor=tk.NW, image=photo)
#         canvas.image = photo
# # #GUI
# root = tk.Tk()
# root.title("GUI")
# canvas = tk.Canvas(root, width=1000, height=1000)
# canvas.pack()

# def on_key_press(key):
#     print(f'Key pressed: {key}')
# # Load and add an image to the window
# key_w = tk.Button(canvas, text='W')
# key_a = tk.Button(canvas, text='A')
# key_s = tk.Button(canvas, text='S')
# key_d = tk.Button(canvas, text='D')
# key_w.pack(side=tk.TOP)
# key_a.pack(side=tk.LEFT)
# key_s.pack(side=tk.LEFT)
# key_d.pack(side=tk.LEFT)

# # key_w = DRIVE_FORWARD
# IMAGE = "C:/Users/Falle/Downloads/bwnjamin.png"
# img = Image.open(IMAGE)
# img = img.resize((1000, 1000))
# img = ImageTk.PhotoImage(img)

# canvas.create_image(300, 300, anchor=tk.NW, image=img)
# canvas.image = img
# IMAGE = "C:/Users/Falle/Downloads/bwnjamin.png"
# img = Image.open(IMAGE)
# img = img.resize((200, 200))
# img = ImageTk.PhotoImage(img)
# root.mainloop() #boo