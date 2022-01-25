import tkinter as tk
from tkinter.ttk import *

program=tk.Tk()
program.title("Voltage Drop")
program.geometry("350x300+500+200")
program.resizable(False,False)

phase=tk.Label(program,text="Phase Number               :",fg="black", font="arial 8 bold")
phase.place(x=10,y=28)
cable_type=tk.Label(program,text="Cable Type                     :",fg="black", font="arial 8 bold")
cable_type.place(x=10,y=59)

phase=tk.IntVar()
phase.set(1)

cable=tk.IntVar()
cable.set(1)

radio1=tk.Radiobutton(program,text="1 Phase",variable=phase,value=1,activebackground="red")
radio1.place(x=145,y=27)

radio2=tk.Radiobutton(program,text="3 Phase",variable=phase,value=2,activebackground="red")
radio2.place(x=225,y=27)

radio3=tk.Radiobutton(program,text="Cu",variable=cable,value=1,activebackground="red")
radio3.place(x=145,y=58)

radio4=tk.Radiobutton(program,text="Al",variable=cable,value=2,activebackground="red")
radio4.place(x=225,y=58)

sectionbox=[1.5,2.5,4,6,10,16,25,35,50,70,95,120,150]

x=tk.StringVar()

section = tk.Label(program, text="Cable Section   (mm2)  :", fg="black", font="arial 8 bold")
section.place(x=10, y=90)

box=Combobox(program,values=sectionbox,height=6,width=4,textvariable=x)
box.place(x=150, y=90)

distance = tk.Label(program, text="Distance               (m)     :", fg="black", font="arial 8 bold")
distance.place(x=10, y=120)
distance_entry = tk.Entry(program,width=6, bg="black", fg="white")
distance_entry.place(x=150, y=120)

voltage= tk.Label(program, text="Voltage                 (V)     :", fg="black", font="arial 8 bold")
voltage.place(x=10, y=150)
voltage_entry = tk.Entry(program,width=6, bg="black", fg="white")
voltage_entry.place(x=150, y=150)

power= tk.Label(program, text="Power                   (W)    :", fg="black", font="arial 8 bold")
power.place(x=10, y=180)
power_entry = tk.Entry(program,width=6, bg="black", fg="white")
power_entry.place(x=150, y=180)

voltage_drop = tk.Label(program, text="Voltage Drop  %e  =", fg="black", font="arial 8 bold")
voltage_drop.place(x=10,y=260)

def calculation():

    if (phase.get()==1):
        f = 200
    elif (phase.get()==2):
        f = 100
    else:
     pass

    if(cable.get()==1):
        k = 56
    elif (cable.get()==2):
        k = 35
    else:
     pass

    l = int(distance_entry.get())
    n = int(power_entry.get())
    u = int(voltage_entry.get())
    s = float(box.get())
    percent_e = (f * l * n) / (k * s * u ** 2)
    percent_e=round(percent_e,3)
    print("Voltage Drop %e =", percent_e)
    percent_e_label = tk.Label(program, text=percent_e, font="arial 8 italic")
    percent_e_label.place(x=120, y=260)


calculate=tk.Button(program,text="Calculate",bg="black",fg="white",command=calculation)
calculate.place(x=160,y=220)

program.mainloop()