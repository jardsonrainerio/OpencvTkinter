import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import cv2
import datetime

class MainWindow():

    def __init__(self, window, cap):
        print('camera-ON')
        hora = ''
        self.window = window
        self.cap = cap
        #self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        #self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.width = "800"
        self.height = "500"
        self.interval = 20 # Interval in ms to get the latest frame
        # Create canvas for image
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.grid(row=0, column=0)
        # Update image on canvas
        self.update_image()

    def update_image(self):
        # Get the latest frame and convert image format
        self.image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB) # to RGB
        self.image = cv2.resize(self.image,(600,500),interpolation=cv2.INTER_LINEAR)
        self.image = Image.fromarray(self.image) # to PIL format
        self.image = ImageTk.PhotoImage(self.image) # to ImageTk format
        # Update image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        # Repeat every 'interval' ms
        self.window.after(self.interval, self.update_image)

        txt3 = Label(app, text=f"{datetime.datetime.now():%d/%m/%Y %H:%M:%S}", fg="white", bg="black", font=("helvetica", 10))
        txt3.place(x=625, y=90, width=150, height=30)



if __name__ == "__main__":
    app = tk.Tk()
    app.title("Alerta de Medicamentos")
    MainWindow(app, cv2.VideoCapture("video.mp4"))

    txt1 = Label(app, text="Texto em Python", background="#2AC77D", foreground="#000")
    txt1.place(x=625, y=10, width=150, height=30)

    txt2 = Label(app, text="Texto em Python", background="#2AC77D", foreground="#000")
    txt2.place(x=625, y=50, width=150, height=30)

    app.mainloop()