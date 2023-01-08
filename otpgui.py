from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import requests
import json
import serial
import keyboard
import time

BASE_URL = "http://medivend.ethical.in/API/"

def nine():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "9")
    else:
        result.insert("end", "9")


def eight():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "8")
    else:
        result.insert("end", "8")


def seven():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "7")
    else:
        result.insert("end", "7")


def six():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "6")
    else:
        result.insert("end", "6")


def five():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "5")
    else:
        result.insert("end", "5")


def four():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "4")
    else:
        result.insert("end", "4")


def three():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "3")
    else:
        result.insert("end", "3")


def two():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "2")
    else:
        result.insert("end", "2")


def one():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "1")
    else:
        result.insert("end", "1")


def zero():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "0")
    else:
        result.insert("end", "0")


def clear():
    result.delete(0, "end")


def back():
    result.delete(1)
    # root.bind('<BackSpace>',button_clear)


def otp_verification():
    data = {"otp": result.get(),"machineid":"8517A76F-6C4C-4044-B19C-B5B73D7B0349"}
    headers={'Content-Type': 'application/json'}
    response_info = requests.post(url = BASE_URL+'GetDataByOTP',headers=headers, data = json.dumps(data))
    label_response= ttk.Label(mainframe,text=response_info.json(),wraplength=500,bootstyle="light")
    label_response.place(relx=0.35,rely=0.30)
    ser = serial.Serial(port='COM1', baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

    while TRUE:
        ser.write(response_info.json().encode('Ascii'))
        receive = ser.readline()
        print(receive.decode('Ascii'))
        time.sleep(1)
        if keyboard.is_pressed('q'):
            print("Quit Application")
            break
    



root = ttk.Window(themename='superhero')
root.geometry('1200x400')
style = ttk.Style()

root.title("HealthCare Management System")
mainframe = ttk.Frame(root, width=800, height=370, relief=RIDGE, borderwidth=5)
mainframe.place(relx=0.5, rely=0.5, anchor='center')

frame = ttk.Frame(mainframe, width=790, height=70, relief=RIDGE, borderwidth=5)
frame.place(x=0, y=0)
frame.pack(side='top', fill='x')

l1 = ttk.Label(frame, text="HealthCare Management System",
               font=('roboto', 30, 'bold'), bootstyle="light")
l1.place(relx=.5, rely=.5, anchor=CENTER)

frame1 = ttk.LabelFrame(mainframe, text="OTP Enter Here", width=650,
                        height=230, relief=RIDGE, borderwidth=7, style="TLabelframe")
# style.configure('TLabelframe', font=('roboto',10,'bold'))
frame1.pack(side='top', fill='x')

innerframe1 = ttk.Frame(frame1, width=200, height=320,
                        relief=RIDGE, borderwidth=3)
innerframe1.place(relx=0, rely=0)


# frame3= Frame(frame1,width=200,height=320,relief=RIDGE,borderwidth=5,bg='#248aa2')
# frame3.place(x=450,y=70)

innerframe2 = Frame(innerframe1, width=190, height=310, relief=RIDGE, borderwidth=3,
                    bg='#248aa2', highlightbackground="white", highlightcolor="white", highlightthickness=2)
innerframe2.place(x=0, y=0)


result = Entry(innerframe2, width=28, relief=SUNKEN, borderwidth=3)
result.place(x=2, y=0)

nine = Button(innerframe2, text="9", padx=15, relief=RAISED, borderwidth=2, font=(
    'verdana', 10, 'bold'), bg='#248aa2', command=nine, fg="white")
nine.place(x=0, y=30)
eight = Button(innerframe2, text="8", padx=15, relief=RAISED, borderwidth=2, font=(
    'verdana', 10, 'bold'), bg='#248aa2', command=eight, fg="white")
eight.place(x=48, y=30)
seven = Button(innerframe2, text="7", padx=15, relief=RAISED, borderwidth=2, font=(
    'verdana', 10, 'bold'), bg='#248aa2', command=seven, fg="white")
seven.place(x=96, y=30)


six = Button(innerframe2, text="6", padx=15, relief=RAISED, borderwidth=2, font=(
    'verdana', 10, 'bold'), bg='#248aa2', command=six, fg="white")
six.place(x=0, y=56)
five = Button(innerframe2, text="5", padx=15, relief=RAISED, borderwidth=2, font=(
    'verdana', 10, 'bold'), bg='#248aa2', command=five, fg="white")
five.place(x=48, y=56)
four = Button(innerframe2, text="4", padx=15, relief=RAISED, borderwidth=2, font=(
    'verdana', 10, 'bold'), bg='#248aa2', command=four, fg="white")
four.place(x=96, y=56)


three = Button(innerframe2, text="3", padx=15, relief=RAISED, borderwidth=2, font=(
    'verdana', 10, 'bold'), bg='#248aa2', command=three, fg="white")
three.place(x=0, y=82)
two = Button(innerframe2, text="2", padx=15, relief=RAISED, borderwidth=2, font=(
    'verdana', 10, 'bold'), bg='#248aa2', command=two, fg="white")
two.place(x=48, y=82)
one = Button(innerframe2, text="1", padx=15, relief=RAISED, borderwidth=2, font=(
    'verdana', 10, 'bold'), bg='#248aa2', command=one, fg="white")
one.place(x=96, y=82)


zero = Button(innerframe2, text="0", padx=15, relief=RAISED, borderwidth=2, font=(
    'verdana', 10, 'bold'), bg='#248aa2', command=zero, fg="white")
zero.place(x=0, y=108)
clear = Button(innerframe2, text="C", padx=15, relief=RAISED, borderwidth=2, font=(
    'verdana', 10, 'bold'), bg='#248aa2', command=clear, fg="white")
clear.place(x=48, y=108)
back = Button(innerframe2, text="<-", padx=15, relief=RAISED, borderwidth=2,
              font=('verdana', 10, 'bold'), bg='#248aa2', command=back, fg="white")
back.place(x=96, y=108)
submit = ttk.Button(innerframe2, text="Submit",command=otp_verification, style="success.TButton")
style.configure('TButton', font=('Roboto', 10, 'bold'))
submit.place(x=48, y=140)


root.mainloop()