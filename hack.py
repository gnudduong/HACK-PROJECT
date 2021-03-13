# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 23:07:04 2021

@author: slims
"""

from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox

root = tk.Tk()
root.title('NOHAZE')
root.geometry('395x850')



    
    
    
    
def infotab():
    for widget in root.winfo_children():
        widget.destroy()
    global bg
    global label1
    global title
    global title_label
    global info_img
    global info_label    
    bg = ImageTk.PhotoImage(Image.open("back2.png") )
  
    # Show image using label 
    label1 = Label( root, image = bg) 
    label1.place(x = 0, y = 0) 
    
    title=ImageTk.PhotoImage(Image.open('logo.png'))
    title_label=Label(root, image=title,bg='black')
    title_label.grid(row=0,column=0, columnspan=4,padx=5,pady=5)

    info_img=ImageTk.PhotoImage(Image.open('text.png'))
    info_label=Label(root, image=info_img, bg='#D8EDF3')
    info_label.grid(row=3,column=0, columnspan=4,padx=20,pady=400)
    
    back_but = Button(root,text='Back',command=main).grid(row=2,column=0)
        
    
def submissiontab():
    for widget in root.winfo_children():
        widget.destroy()
    global bg
    global label1
    global title
    global title_label
    global info_img
    global info_label    
    bg = ImageTk.PhotoImage(Image.open("back2.png") )
  
    # Show image using label 
    label1 = Label( root, image = bg) 
    label1.place(x = 0, y = 0) 
    
    title=ImageTk.PhotoImage(Image.open('logo.png'))
    title_label=Label(root, image=title,bg='black')
    title_label.grid(row=0,column=0, columnspan=4,padx=5,pady=5)
    
    user_title=Label(root,text='Your email here:',fg='black',bg='#D8EDF3',font='Helvetica', justify=LEFT)
    user_title.grid(row=1,column=0, pady=(500,0))
    
    user_submit=Entry(root)
    user_submit.grid(row=1,column=1,pady=(500,0))
    
    user_ob=Label(root,text='Your observations here:',fg='black',bg='#D8EDF3',font='Helvetica')
    user_ob.grid(row=2,column=0,padx=20)
    
    ob_submit=Entry(root)
    ob_submit.grid(row=2,column=1)
    
    
    def subsuccess():
        user_submit.delete(0,END)
        ob_submit.delete(0,END)
        suc = messagebox.showinfo('Thank you','Submission recieved')

        
        
        
    ob_sub = Button(root,text='Submit', command=subsuccess).grid(row=3, column=0)
    ob_back= Button(root,text='Back',command=main).grid(row=3,column=1)

def notitab():
    for widget in root.winfo_children():
        widget.destroy()
    global bg
    global label1
    global title
    global title_label
    global noti_img
    global noti_label    
    bg = ImageTk.PhotoImage(Image.open("back2.png") )
  
    # Show image using label 
    label1 = Label( root, image = bg) 
    label1.place(x = 0, y = 0) 
    
    title=ImageTk.PhotoImage(Image.open('logo.png'))
    title_label=Label(root, image=title,bg='black')
    title_label.grid(row=0,column=0, columnspan=4,padx=5,pady=5)
    
    
    
    noti_img=ImageTk.PhotoImage(Image.open('warning.png'))
    noti_label=Label(root, image=noti_img)
    noti_label.grid(row=3,column=0, columnspan=4,padx=35,pady=200)
    
    back_but = Button(root,text='Back',command=main).grid(row=2,column=0)
    
    
    
def searchtab():
    for widget in root.winfo_children():
        widget.destroy()
    global bg
    global label1
    global title
    global title_label
    global info_img
    global info_label    
    bg = ImageTk.PhotoImage(Image.open("back2.png") )
  
    # Show image using label 
    label1 = Label( root, image = bg) 
    label1.place(x = 0, y = 0) 
    
    title=ImageTk.PhotoImage(Image.open('logo.png'))
    title_label=Label(root, image=title,bg='black')
    title_label.grid(row=0,column=0, columnspan=4,padx=5,pady=5)

    pollution_label= Label(root,text='Choose pollutants:',fg='white',bg='black',font='Helvetica').grid(row=2,column=0,padx=35,pady=5)
    options=['     SO2     ' ,'     CO      ', '     NOx      ']
    click=StringVar()
    click.set('     SO2     ')
    drop = OptionMenu(root, click, *options)
    drop.grid(row=2, column=1,padx=0,pady=0)
    
    date_label= Label(root,text='Choose date:',fg='white',bg='black',font='Helvetica',anchor=W).grid(row=3,column=0,padx=25,pady=2)
    date_entry = Entry(root)
    date_entry.insert(0,'yyyy,mm,dd')
    date_entry.grid(row=3,column=1)
    
    location_label= Label(root,text='Choose location:',fg='white',bg='black',font='Helvetica',anchor=W).grid(row=4,column=0,padx=25,pady=2)
    location_entry = Entry(root)
    location_entry.insert(0,'your location')
    location_entry.grid(row=4,column=1)
    
    def opendata():
        global chart
        global chart_lab
        global chart1
        global chart1_lab
        global signal
        global signal_lab
        
        if click.get()=='     SO2     ':
            chart = ImageTk.PhotoImage(Image.open("SO2.png"))
            chart1 = ImageTk.PhotoImage(Image.open("niceso2.png"))
            signal = ImageTk.PhotoImage(Image.open("bad.png"))
        elif click.get()=='     CO      ':
            chart = ImageTk.PhotoImage(Image.open("CO.png"))
            chart1 = ImageTk.PhotoImage(Image.open("niceco.png"))
            signal = ImageTk.PhotoImage(Image.open("good.png"))
        elif click.get()=='     NOx      ':
            chart = ImageTk.PhotoImage(Image.open("NOx.png"))
            chart1 = ImageTk.PhotoImage(Image.open("nicenox.png"))
            signal = ImageTk.PhotoImage(Image.open("bad.png"))

        chart_lab = Label(root, image = chart)
        chart1_lab = Label(root, image = chart1, bg='#D8EDF3')
        signal_lab = Label(root, image = signal, bg='black')
        chart_lab.grid(row=6,column=0,columnspan=2, padx=20, pady=20)
        chart1_lab.grid(row=7,column=0,columnspan=2, padx=20, pady=0)
        signal_lab.grid(row=0,column=1,padx=5,pady=5)
    
    sub_butt= Button(root,text='Search', command=opendata)
    sub_butt.grid(row=5,column=0,columnspan=2,padx=10)
    
    ob_back= Button(root,text='Back',command=main).grid(row=5,column=1)
    # return
    
def main():
# Add image file
    for widget in root.winfo_children():
        widget.destroy()
    global bg
    global label1
    global title
    global title_label
    global info_img
    global info_label
    global quality
    global quality_label
    
    
    bg = ImageTk.PhotoImage(Image.open("back2.png") )
      
    # Show image using label 
    label1 = Label( root, image = bg) 
    label1.place(x = 0, y = 0) 
    
    title=ImageTk.PhotoImage(Image.open('logo.png'))
    title_label=Label(root, image=title,bg='black')
    title_label.grid(row=0,column=0,padx=5,pady=5, columnspan=4)   
    
    search_tab= Button(root, text='Search', command= searchtab,bg='#D8EDF3')
    search_tab.grid(row=1,column=0)
    
    info_tab= Button(root, text='Info', command = infotab,bg='#D8EDF3')
    info_tab.grid(row=1,column=1)
    
    submission_tab= Button(root, text='Submission', command = submissiontab,bg='#D8EDF3')
    submission_tab.grid(row=1,column=2)
    
    noti_tab= Button(root, text='Notification', command = notitab,bg='#D8EDF3')
    noti_tab.grid(row=1,column=3)
    
    quality=ImageTk.PhotoImage(Image.open('quality.png'))
    quality_label=Label(root, image=quality,bg='#D8EDF3')
    quality_label.grid(row=2,column=0,padx=20,pady=370, columnspan=4)
    
    
    
main()
root.mainloop()