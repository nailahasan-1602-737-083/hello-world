from inspect import FrameInfo
import sys
import vlc
from threading import *
import threading
from tkinter import *
from tkinter import messagebox
import datetime
import time
import winsound
from playsound import playsound
from PIL import ImageTk, Image
root = Tk()
# Set geometry
root.geometry("600x500")
root.title("DIGITAL CLOCK")

def tick(val):
	global clock
	window=Toplevel(root)
	window.geometry("300x130")
	clock=Label(window, font=('Helvetica', 30, "bold"), fg="light green", bg="black", bd=16, relief=SUNKEN)
	clock.place(x=18,y=30)
	if val=="btn_24":
		time24()
	elif val=="btn_12":
		time12()
	elif val=="btn_al":
		alarm()

def time24():
	global clock
	ts=time.strftime("%H:%M:%S")
	clock["text"]=ts
	clock.after(1000, time24)
    

def time12():
	global clock
	ts=time.strftime("%I:%M:%S:%p")
	clock["text"]=ts
	clock.after(1000, time12)
# Create Object

# Use Threading

def Threading():
    if(tick("btn_al")):
        t1=Thread(target=alarm)
        t1.start()
def Threading12():
    if(tick("btn_12")):
        t2=Thread(target=time12)
        t2.start()
def Threading24():
    if(tick("btn_24")):
        t3=Thread(target=time24)
        t3.start()


def on_closing():
    p = vlc.MediaPlayer("alarm-clock.wav")
    res=messagebox.askquestion("askquestion",'Spaghetto is the singular form of the word spaghetti.')
    if res == 'yes':
        res1=messagebox.askquestion('askquestion', 'Polar bears can only live in the Arctic region, not in the Antarctic. ')
        if res1=='yes':
            messagebox.showinfo('Response', 'you exit the alarm')
        
        else:
           
            p.play()
            on_closing()
    else:
        
        p.play()
        on_closing()



def alarm():
    global hour,minute,second
    window=Toplevel(root)
    window.geometry("350x300")
    window.title("ALARM CLOCK")
    Label(window,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red", relief=SUNKEN).pack(pady=10)
    Label(window,text="Set Time",font=("Helvetica 15 bold"), relief=SUNKEN).pack()
              
    frame = Frame(window)
    frame.pack()
    hour = StringVar(window)
    hours = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15','16', '17', '18', '19', '20', '21', '22', '23', '24' )
    hour.set(hours[0])
    hrs = OptionMenu(frame, hour, *hours)
    hrs.pack(side=LEFT)

    minute = StringVar(window)
    minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
        '08', '09', '10', '11', '12', '13', '14', '15',
        '16', '17', '18', '19', '20', '21', '22', '23',
        '24', '25', '26', '27', '28', '29', '30', '31',
        '32', '33', '34', '35', '36', '37', '38', '39',
        '40', '41', '42', '43', '44', '45', '46', '47',
        '48', '49', '50', '51', '52', '53', '54', '55',
        '56', '57', '58', '59', '60')
    minute.set(minutes[0])
    mins = OptionMenu(frame, minute, *minutes)
    mins.pack(side=LEFT)

    second = StringVar(window)
    seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
        '08', '09', '10', '11', '12', '13', '14', '15',
        '16', '17', '18', '19', '20', '21', '22', '23',
        '24', '25', '26', '27', '28', '29', '30', '31',
        '32', '33', '34', '35', '36', '37', '38', '39',
        '40', '41', '42', '43', '44', '45', '46', '47',
        '48', '49', '50', '51', '52', '53', '54', '55',
        '56', '57', '58', '59', '60')
    second.set(seconds[0])
    secs = OptionMenu(frame, second, *seconds)
    secs.pack(side=LEFT)

    begin=Button(window,text="Set Alarm",font=("Helvetica 15"),command=alarmset)
    begin.pack(pady=20)
    begin.bind("<Button-1>",alarmset)
    
    


def alarmset(event):
    # Infinite Loop
    global hour,minute,second
    while(1):
       
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        
        # Wait for one seconds
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
        
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
                # Playing sound
            p = vlc.MediaPlayer("alarm-clock.wav")
            p.play()
            res2 = messagebox.askquestion('askquestion', 'Do you want to stop alarm?')
            if res2=='yes':
                win = Toplevel(root)
                win.title("STOPPING ALARM")
                win.geometry("230x100")
                b1=Button(win,text="Yes",command=on_closing, width=10)
                b1.grid(row=1, column=1)
                mainloop()
	    else:
		pass

                # Add Labels, Frame, Button, Optionmenus

        
img1=PhotoImage(file="12.png")
img2=PhotoImage(file="24.png")
img3=PhotoImage(file="alarm.png")
text=Label(root,text="Which clock do you want to try?",font = ('Helvetica', 20 , "bold"), fg="dark red")
text.place(x=80, y=20)

btn1=Button(root, image=img1, borderwidth=0, command=Threading12)
btn1.place(anchor=SW,x=0, y=200)
btn2=Button(root, image=img2, borderwidth=0, command=Threading24)
btn2.place(anchor=SW,x=0, y=300)
btn3=Button(root, image=img3, borderwidth=0, command= Threading)
btn3.place(anchor=SW,x=0, y=400)

photo=ImageTk.PhotoImage(Image.open("clock.png"))

img_label=Label(root,image=photo)
img_label.place(x=230, y=150)
mainloop()
