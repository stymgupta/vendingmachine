from tkinter import *
from tkinter import messagebox
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import requests, json, serial, time, socket, threading


BASE_URL = "http://medivend.ethical.in/API/"
#ser = serial.Serial(port='/dev/ttyS0', baudrate=9600,bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)


def machineStatus():
    data2 = {"machineid": "746B5961-F805-4144-BE0F-3D94833022BB"}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url=BASE_URL+'UdpateStatusofMachine',headers=headers, data=json.dumps(data2))
    message = response.json()['returnMessage']
    print(message)


def everyminute():
    thread= threading.Timer(60.0, everyminute)
    thread.start()
    machineStatus()

    

    

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
    txt = result.get()
    newtxt = txt[:-1]
    result.delete(0, tk.END)
    result.insert(0, newtxt)

    
def statusUpdate():
    data1 = {"otp": result.get(), "machineid": "746B5961-F805-4144-BE0F-3D94833022BB", "dispendstatus": status}
    headers = {'Content-Type': 'application/json'}
    info=requests.post(url=BASE_URL+'StatusByOTP',headers=headers, data=json.dumps(data1))



def toggler(event):
    fullScreenState = True
    root.attributes("-fullscreen", fullScreenState)


def exit(event):
    fullScreenState = False
    root.attributes("-fullscreen", fullScreenState)



def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        state = "Online"
        everyminute()
    except OSError:
        state = "Offline"
    wifi.config(text=state)
    root.after(10000, is_connected)
##################################################################################################################################


byte0 = "A5"
byte4 = 0xFF

def otp_verification():
    global byte1, byte2, byte3, byte5, checksum, status  
    
    if len(result.get()) == 6:
        data = {"otp": result.get(), "machineid": "746B5961-F805-4144-BE0F-3D94833022BB"}
        headers = {'Content-Type': 'application/json'}
        response_info = requests.post(url=BASE_URL+'GetDataByOTP', headers=headers, data=json.dumps(data))
        response_detail = response_info.json()['dispendDetails']
        if response_info.json()['returnCode'] == 1:
            ser.write(bytes.fromhex(byte0+"01"+"00"+"00"+"01"))
            receive = ser.readline()
            if receive == b'\xa5\x81\x00\x00\x81':
                status = 8
            else:
                if receive == b'\xa5\x81\x01\x00\x82':
                    print("Sold Out")
                    status = 0
                elif receive == b'\xa5\x81\x02\x00\x83':
                    print("Motor Jam")
                    status = 1
                elif receive == b'\xa5\x81\x04\x00\x85':
                    print("No Motor")
                    status = 2
                elif receive == b'\xa5\x81\x08\x00\x89':
                    print("Invalid Selection")
                    status = 3
                elif receive == b'\xa5\x81\x10\x00\x91':
                    print("Health Safety Error")
                    status = 4
                else:
                    print(receive,"System Fault")
                    status = 5

            for i in range(len(response_detail)):
                matrix = response_detail[i]
                for j in range(matrix['qty']):
                    byte1, byte2, byte3 = "04", matrix['coil'][1], matrix['coil'][0]
                    sum2 = hex(int(byte1, 16)+int(byte2, 16)+int(byte3, 16))
                    checksum = (int(sum2, 16)) & (byte4)
                    ser.write(bytes.fromhex(byte0+byte1+byte2.zfill(2) + byte3.zfill(2)+"0x{:02x}".format(checksum)[2:]))
                    #time.sleep(1)                    
                    receive = ser.readline()
                    print(receive)
                    if receive == b'\xa5\x84\x00\x00\x84' or b'\xa5\x84\x80\x00\x04':
                        print("Vend in Progress")
                        status = 7
                    else:
                        if receive == b'\xa5\x84\x01\x00\x85':
                            message = "Sold Out"
                            print(message)
                            status = 0
                        elif receive == b'\xa5\x84\x02\x00\x86':
                            message = "Motor Jam"
                            print(message)
                            status = 1
                        elif receive == b'\xa5\x84\x04\x00\x88':
                            message = "No Motor"
                            print(message)
                            status = 2
                        elif receive == b'\xa5\x84\x08\x00\x92':
                            message = "Invalid Selection"
                            print(message)
                            status = 3
                        elif receive == b'\xa5\x84\x10\x00\x94':
                            message = "Health Safety Error"
                            print(message)
                            status = 4
                        else:
                            message = "Health Safety Error"
                            print(message)
                            status = 5
                        #statusUpdate()
                        tk.messagebox.showerror("error", message)

                    byte5 = "03"
                    sum2 = hex(int(byte5, 16)+int(byte2, 16)+int(byte3, 16))
                    checksum = (int(sum2, 16)) & (byte4)
                    time.sleep(1)
                    ser.write(bytes.fromhex(byte0+byte5+byte2.zfill(2) + byte3.zfill(2)+"0x{:02x}".format(checksum)[2:]))
                    time.sleep(1)
                    receive = ser.readline()
                    print(receive)
                    if receive==b'\xa5\x83\x00\x00\x83' or b'\xa5\x83\x80\x00\x03':
                        print("Vend in Progress")
                        status = 7
                    else:
                        if receive == b'\xa5\x83\x01\x00\x84':
                            message = "Sold Out"
                            print(message)
                            status = 0
                        elif receive == b'\xa5\x83\x02\x00\x85':
                            message = "Motor Jam"
                            print(message)
                            status = 1
                        elif receive == b'\xa5\x83\x04\x00\x87':
                            message = "No Motor"
                            print(message)
                            status = 2
                        elif receive == b'\xa5\x83\x08\x00\x91':
                            message = "Invalid Selection"
                            print(message)
                            status = 3
                        elif receive == b'\xa5\x83\x10\x00\x93':
                            message = "Health Safety Error"
                            print(message)
                            status = 4
                        else:
                            message = "Health Safety Error"
                            print(message)
                            status = 5
                        tk.messagebox.showerror("error", message)
                    time.sleep(3)
                    ser.write(bytes.fromhex(byte0+"02"+"00"+"00"+"02"))
                    #time.sleep(1)
                    receive = ser.readline()
                    print(receive)
                    responses = {
                    b'\xa5\x82\x00\x00\x02': {
                        'message': 'Vend Successful',
                        'status': 6,
                        'success_message': 'Vend Successful',
                    },
                    b'\xa5\x82@\x00\xc2': {
                        'message': 'Vend Successful',
                        'status': 6,
                        'success_message': 'Vend Successful',
                    },
                    b'\xa5\x82\x01\x00\x83': {
                        'message': 'Sold Out',
                        'status': 0,
                        'error_message': 'Sold Out',
                        'clear_result': True,
                    },
                    b'\xa5\x82\x02\x00\x84': {
                        'message': 'Motor Jam',
                        'status': 1,
                        'error_message': 'Motor Jam',
                        'clear_result': True,
                    },
                    b'\xa5\x82\x04\x00\x86': {
                        'message': 'No Motor',
                        'status': 2,
                        'error_message': 'No Motor',
                        'clear_result': True,
                    },
                    b'\xa5\x82\x80\x00\x02': {
                        'message': 'Sold Out',
                        'status': 0,
                        'error_message': 'Sold Out',
                        'clear_result': True,
                    },
                    b'\xa5\x82\x08\x00\x90': {
                        'message': 'Invalid Selection',
                        'status': 3,
                        'error_message': 'Invalid Selection',
                        'clear_result': True,
                    },
                    b'\xa5\x82\x10\x00\x92': {
                        'message': 'Health Safety Error',
                        'status': 4,
                        'error_message': 'Health Safety Error',
                        'clear_result': True,
                    },
                    # Default response
                    'default': {
                        'message': 'System Fault',
                        'status': 5,
                        'error_message': 'System Fault',
                        'clear_result': True,
                    }
                }

                # Process the received data
                    if receive in responses:
                            response = responses[receive]
                    else:
                            response = responses['default']

                # Display the message
                    print(response['message'])

                # Update the status
                    status = response['status']
                

                # Display the error message if applicable
                    if 'error_message' in response:
                       tk.messagebox.showerror("error", response['error_message'])
                       
                    
                # Clear the result if applicable
                    if 'clear_result' in response and response['clear_result']:
                        result.delete(0, "end")
                    if 'error_message' in response:
                        break
                if 'error_message' in response:
                    break
            statusUpdate()
            if 'success_message' in response:
                    tk.messagebox.showinfo("Success", "Vend Successful")
                    result.delete(0,"end")
                
        else:
            tk.messagebox.showerror("error", response_info.json()['returnMessage'])
            result.delete(0, "end")
    else:
        tk.messagebox.showerror("OTP Error", "OTP must be 6 digits.")
        result.delete(0, "end")
        

#################################################################################################################################


################################################################################################################################
root = ttk.Window(themename='yeti')
root.attributes('-fullscreen', True)
root.geometry('400x300')
root.configure()
style = ttk.Style()
root.bind("<F11>", toggler)
root.bind("<Escape>", exit)
wifi = ttk.Label(root, text="Checking...", bootstyle='default')
wifi.pack()

is_connected()
root.title("Alauna Health Care")

head = ttk.Frame(root, relief=RAISED, borderwidth=0)
head.pack(ipady=2,side=ttk.TOP)
ttk.Label(head, bootstyle="inverse-info", text="  Alauna Vending Machine  ", font=('verdana',20, 'bold')).pack(side=ttk.TOP)
innerframe1 = ttk.Frame(root, relief=RAISED, borderwidth=0)
innerframe1.pack(side=ttk.TOP)

innerframe2 = ttk.Frame(root, relief=RAISED, borderwidth=2)
innerframe2.pack(fill=ttk.BOTH, side=ttk.TOP)
#Change image path
logoimage = ttk.PhotoImage(file=r"C:\Users\satya\Downloads\vending\vendingmachine\logo.png").subsample(6,6)
root.tk.call('wm', 'iconphoto', root._w, logoimage)
ttk.Label(innerframe1, text='logo', image=logoimage).pack(side=ttk.LEFT)
ttk.Label(innerframe1, bootstyle="default", text="Alauna", font=('verdana', 20, 'bold'), foreground='#2E3092').pack(side=ttk.LEFT)
ttk.Label(innerframe1, bootstyle="default", text=" HealthCare", font=('verdana', 20), foreground='#2E3092').pack(side=ttk.LEFT)
innerbox = ttk.Frame(innerframe2, relief=RAISED, borderwidth=1)
innerbox.pack(fill=ttk.Y, side=ttk.TOP, expand=True)

result = ttk.Entry(innerbox, justify="center", font=('Ariel 40 bold'))
result.pack(ipadx=30, fill=ttk.BOTH, expand=True)

style.configure('MyButton.TButton', font='Verdana 30 bold')
pack_row = {"fill": ttk.BOTH, "side": ttk.TOP}
pack_button = {"ipadx":43,"ipady":10, "fill": ttk.BOTH, "side": ttk.LEFT}

row1 = ttk.Frame(innerbox, relief=RAISED, borderwidth=1)
row1.pack(**pack_row)

row2 = ttk.Frame(innerbox, relief=RAISED, borderwidth=1)
row2.pack(**pack_row)

row3 = ttk.Frame(innerbox, relief=RAISED, borderwidth=2)
row3.pack(**pack_row)

row4 = ttk.Frame(innerbox, relief=RAISED, borderwidth=2)
row4.pack(**pack_row)


one = ttk.Button(row1, text="1", bootstyle='outline',
                 command=one, style='MyButton.TButton')
one.pack(**pack_button)

two = ttk.Button(row1, text="2", bootstyle='outline',
                 command=two, style='MyButton.TButton')
two.pack(**pack_button)

three = ttk.Button(row1, text="3", bootstyle='outline',
                   command=three, style='MyButton.TButton')
three.pack(**pack_button)

four = ttk.Button(row2, text="4", bootstyle='outline',
                  command=four, style='MyButton.TButton')
four.pack(**pack_button)

five = ttk.Button(row2, text="5", bootstyle='outline',
                  command=five, style='MyButton.TButton')
five.pack(**pack_button)

six = ttk.Button(row2, text="6", bootstyle='outline',
                 command=six, style='MyButton.TButton')
six.pack(**pack_button)

seven = ttk.Button(row3, text="7", bootstyle='outline',
                   command=seven, style='MyButton.TButton')
seven.pack(**pack_button)

eight = ttk.Button(row3, text="8", bootstyle='outline',
                   command=eight, style='MyButton.TButton')
eight.pack(**pack_button)

nine = ttk.Button(row3, text="9", bootstyle='outline',
                  command=nine, style='MyButton.TButton')
nine.pack(**pack_button)

clear = ttk.Button(row4, text="C", bootstyle='outline',
                   command=clear, style='MyButton.TButton')
clear.pack(**pack_button)

zero = ttk.Button(row4, text="0", bootstyle='outline',
                  command=zero, style='MyButton.TButton')
zero.pack(**pack_button)

back = ttk.Button(row4, text="X", bootstyle='outline',
                  command=back, style='MyButton.TButton')
back.pack(**pack_button)

submit = ttk.Button(innerbox, text="Submit",
                    command=otp_verification, style="success.outline.TButton")
style.configure('TButton', font=('Roboto', 50, 'bold'))
submit.pack(side=ttk.TOP, fill=ttk.BOTH)

root.mainloop()

