import sys
import os
from pynput.mouse import Listener
from pynput.mouse import Button, Controller
mouse = Controller()
import time
import tkinter as tk
import tkinter
from tkinter import messagebox
from distutils.core import setup
import py2exe
import json
from json import dump

# speed2=0.0029 #bude v json

file = open('data_coockie_clicker.json')
data = json.load(file)
# data = json.loads(json_retezec)
# print(data['Rychlost'])

speed2 = data['Rychlost']
global a
a = 0
file.close()
main_window = tk.Tk()
main_window.title("Auto Clicker")
main_window.resizable(0,0)
main_window.geometry('400x180')
# main_window.configure(background="#B8FFFF")

main_window.option_add('*Font', 'Arial 14')

title = tk.Label(main_window, text=u"Auto clicker", height=2,anchor="w").grid(row=0,columnspan=3)

titleSpeed = tk.Label(main_window, text=u"Rychlost: ", width=15,anchor="e").grid(row=1,column=0)

entrySpeed = tk.Entry(main_window, width=10, justify="center")
entrySpeed.insert(0,speed2)
entrySpeed.grid(row=1,column=1)
def speed(speed2=entrySpeed.get):
    try:
        if(float(entrySpeed.get())>0.001):
            speed2 = float(entrySpeed.get())
            # print(speed2)
            return speed2
        else:
            messagebox.showerror("error","Musí být větší než 0.001")
    except:
        messagebox.showerror("error","Špatná hodnota")
# btnSpeed = tk.Button(main_window, text=u"nastav",
#                             command=speed, width=10).grid(row=1,column=2)



# if enteryCurrentX.get()!=mouse.position:
#     enteryCurrentX.delete(0,"end")
#     enteryCurrentX.insert(0,mouse.position)    
# entryCurrentY = tk.Entry(main_window, width=10).grid(row=2,column=2)

# def on_move(x, y):
#     enteryCurrentX.insert(0,'Pointer moved to {0}'.format(
#         (x)))

# with Listener(
#         on_move=on_move) as listener:
#     listener.join()

titleSetPosition = tk.Label(main_window, text="Nastav pozici: ", width=15,anchor="e").grid(row=2,column=0)
enterySetX = tk.Entry(main_window, width=10, justify="center")
enterySetX.grid(row=2,column=1)
enterySetY = tk.Entry(main_window, width=10, justify="center")
enterySetY.grid(row=2,column=2)
# btnSetPosition = tk.Button(main_window, text=u"nastav", command=position).grid(row=3,column=4)
titleSetPosition = tk.Label(main_window, text="Nastavená pozice: ", width=15,anchor="e").grid(row=3,column=0)
enteryX = tk.Entry(main_window, width=10, justify="center")
enteryX.grid(row=3,column=1)
enteryX.configure(state='normal')
enteryX.insert(0,data['NastavenaPoziceX'])
enteryX.configure(state='disabled')
enteryY = tk.Entry(main_window, width=10, justify="center")
enteryY.grid(row=3,column=2)
enteryY.configure(state='normal')
enteryY.insert(0,data['NastavenaPoziceY'])
enteryY.configure(state='disabled')
def clicker():
    try:
        file = open('data_coockie_clicker.json')
        data = json.load(file)
        # data['Rychlost'] = speed(speed2)
        # print(speed(speed2))
        # json.dump(data['Rychlost'],json_retezec)
        time.sleep(0.5)
        # mouse.position = (300, 540)
        if enterySetX.get() != "" and enterySetY.get()!= "":
            positionSetX = enterySetX.get()
            positionSetY = enterySetY.get()
            # print(positionSetX + positionSetY)
            data['NastavenaPoziceX'] = positionSetX
            data['NastavenaPoziceY'] = positionSetY
            mouse.position = (data['NastavenaPoziceX'],data['NastavenaPoziceY'])
            enteryX.configure(state='normal')
            enteryX.delete(0,"end")
            enteryX.insert(0,data['NastavenaPoziceX'])
            enteryX.configure(state='disabled')
            enteryY.configure(state='normal')
            enteryY.delete(0,"end")
            enteryY.insert(0,data['NastavenaPoziceY'])
            enteryY.configure(state='disabled')
            
        else:
            mouse.position = (data['NastavenaPoziceX'],data['NastavenaPoziceY'])
        file.close()
        #dump json
        with open("data_coockie_clicker.json", "w") as file:
            dump({'Rychlost':speed(speed2), 'NastavenaPoziceX':enteryX.get(), 'NastavenaPoziceY':enteryY.get()}, file, indent=3)
        file.close()
        file = open('data_coockie_clicker.json')
        data = json.load(file)
        while mouse.position == (int(data['NastavenaPoziceX']),int(data['NastavenaPoziceY'])): 
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(float(data['Rychlost']))
        # file.close()
    except:
        messagebox.showerror("error","Něco nefunguje správně")


btn=tk.Button(main_window, height=1, width=20, text="ZAPNI", 
                    command=clicker, background="red",anchor="c").grid(row=4,columnspan=3)
# btn.configure(font=("Arial", 12))
main_window.mainloop()


