"""
by:mohamed fares
Creates a QR code from a given string and saves it as an image file.

This function takes a string input from the user, creates a QR code image using the pyqrcode library, and saves the image to a file named 'myqr.png'. A success message is displayed in a Tkinter window.
"""
import pyqrcode
import png
from PIL import ImageTk, Image
from pyqrcode import QRCode
import tkinter as tk 
from tkinter import *
import PIL.Image

window = Tk()  
window.geometry('300x350')
window.title('project(mohamedfares)')

Label(window,text='Lets Create QR Code',font='arial 15').pack()
# String which represents the QR code
s = tk.StringVar()
  
# Generate QR code
def create_qrcode():
    s1=s.get()
    qr = pyqrcode.create(s1)
    qr.png('myqr.png', scale = 6)
    Label(window,text='QR Code is created and saved successfully').pack()

Entry(window,textvariable=s,font='arial 15').pack()
Button(window,text='create',bg='pink',command=create_qrcode).pack()
window.mainloop()