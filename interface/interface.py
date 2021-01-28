from tkinter import *
from tkinter import ttk
import random
from tkinter.filedialog import *
from tkinter import scrolledtext
import sys
from tkinter.messagebox import *
import sys, fileinput
N=8
texts=['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']

def function():
    pass


def randomi():
    a=['Кот', 'Собака', 'Клавиатура', 'Россия', 'Нигга']
    print(random.choice(a))

def vosemnadsat():
    b =['Кошка', 'Собака', 'Мышка', 'Эстония', 'Мексиканец']
    print(random.choice(b))

def open_():
    file=askopenfilename()
    f=open(file,'r',encoding='utf-8-sig')
    file=f.readlines()
    salvestamine
def save_():
    file=asksaveasfile(mode='w',defaultextension=(('.txt'),('.docx')),filetypes=(('Notepad','.txt'),('Word','.docx')))
    t=txt_box.get(0.0,END)
    file.write(t)
    file.close()
def exit():
    if askyesno('Exit','Yes/No'):
        showinfo('Exit','Message: Yes')
        root.destroy()
    else:
       showinfo('No')

root=Tk()
root.geometry("500x400")
root.title('Elemendid Tkinteris')
tabs=ttk.Notebook(root)
tabs_list=[]
#for i in range (N):
 #   t='tab'+str(i)
 #   t=Frame(tabs)
 #   tabs_list.append(t)
 #   tabs.add(t,text=texts[i-1])



tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tabs.add(tab1,text='one')
tabs.add(tab2,text='two')
tabs.add(tab3,text='three')
tabs.add(tab4,text='four')

M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label='Menu1',menu=m1)
m1.add_command(label='Com1',command=function)
m1.add_command(label='Com1',command=function)
m1.add_command(label='Com1',command=function)
m1.add_command(label='Com1',command=function)


m2=Menu(M,tearoff=0)
M.add_cascade(label='BG Colors',menu=m2)
m2.add_command(label='Yellow',command=lambda:root.config(bg='yellow'))
m2.add_command(label='Green',command=lambda:root.config(bg='green'))
m2.add_command(label='Blue',command=lambda:root.config(bg='blue'))
m2.add_command(label='Violette',command=lambda:root.config(bg='violet'))

m3=Menu(M,tearoff=0)
M.add_cascade(label='Only fun',menu=m3)
m3.add_command(label='random',command=randomi)
m3.add_command(label='18+',command=vosemnadsat)
m3.add_command(label='random',command=randomi)
m3.add_command(label='random',command=randomi)

btn_open=Button(tab1,text='Open',command=open_)
btn_save=Button(tab1,text='Save',command=save_)
btn_exit=Button(tab1,text='Exit',command=exit)
txt_box=scrolledtext.ScrolledText(tab1,width=40,height=5)
txt_box.grid(row=0,column=0,columnspan=3)
btn_open.grid(row=1,column=0)
btn_save.grid(row=1,column=1)
btn_exit.grid(row=1,column=2)

tabs.pack(fill='both')
root.mainloop() 