from inspect import FrameInfo
import sys
import os
from playsound import playsound
from threading import *
import threading
from tkinter import *
from tkinter import messagebox
import datetime
import time
import winsound
from PIL import ImageTk, Image
import pygame
from pygame import mixer
import random

#riddles dictioray with question and answers.
riddle = {'Spaghetto is the singular form of the word spaghetti':'yes', 
          'Polar bears can only live in the Arctic region, not in the Antarctic' : 'no',
          'Emus can not fly.': 'yes',
          'The Mona Liza was stolen from the Louvre in 1911': 'yes',
	 'In the animation film “Finding Nemo,” the main protagonist is a pufferfish.' : 'no',
          'In a regular deck of cards, all kings have a mustache.' : 'no',
          'Michael Jackson and Nicolas Cage both married the same lady.' : 'yes',
          'The Philippines is an archipelagic country that has the most number of islands.' : 'no',
          'Mount Kilimanjaro is the highest mountain in the world?' : 'no',
          'A group of swans is known as a bevy? ' :'yes' ,
          'Glastonbury had been due to celebrate its 50th anniversary in June before the festival was cancelled?' : 'yes',
          ' Nepal is the only country in the world which does not have a rectangular flag?' : 'yes',
          ' First ODI (Cricket) in India was played in Ahemadabad.' : 'yes',
          'The Headquarters of the Southern Naval Command of the India Navy is located at Thiruvananthapuram.' : 'no'}

root = Tk()

pygame.init()
mixer.init()
mixer.music.load("alarm-clock.wav")


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
		alarm(window)

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
    
    question, answer = random.choice(list(riddle.items()))

    res=messagebox.askquestion("askquestion", question)
    if res.lower() == answer.lower():
        mixer.music.stop()
        #root.destroy()
        startProcess()      
    else:
        res2 = messagebox.showinfo('stop', 'Do you want to stop alarm?')
        if res2=='ok':
            on_closing()


def alarm(window):
    global hour,minute,second
    #window=Toplevel(root)
    window.geometry("350x300")
    window.title("ALARM CLOCK")
    Label(window,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red", relief=SUNKEN).pack(pady=10)
    Label(window,text="Set Time",font=("Helvetica 15 bold"), relief=SUNKEN).pack()
              
    frame = Frame(window)
    frame.pack()
    hour = StringVar(window)
    hours = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15','16', '17', '18', '19', '20', '21', '22', '23')
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

    begin=Button(window,text="Set Alarm",font=("Helvetica 15"),command=callAlarm)
    begin.pack(pady=20)
    #begin.bind("<Button-1>",callalarm)

def callAlarm():
    # Infinite Loop
    global hour,minute,second
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"        
    while(1):
        # Wait for one seconds
        time.sleep(1)
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
        
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            mixer.music.play(-1)
            res2 = messagebox.showinfo('stop', 'Do you want to stop alarm?')
            if res2=='ok':
                on_closing()
                break

def startProcess():   
    # Set geometry
    root.geometry("600x500")
    root.title("DIGITAL CLOCK")
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

    photo=ImageTk.PhotoImage(Image.open("alarmclock.png"))

    img_label=Label(root,image=photo)
    img_label.place(x=300, y=120)
    mainloop()
startProcess()
