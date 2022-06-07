#usar o IMC e o Fº
from tkinter import *

root=Tk()
#criando a janela
root.title('Windows Execute')
root.geometry('400x200+100+500')
root.minsize(width=500, height=250)
root.maxsize(width=1200, height=600)
root.config(bg=('#810F5F'))

f1=Frame(root, bg='Grey')
f2=Frame(root, bg='Dark Grey')
#calculos, IMC
def calcular():
    label3['text'] = float(entry2.get()) / (float(entry1.get())*float(entry1.get()))
    a1 = float(entry2.get()) / (float(entry1.get()) * float(entry1.get()))
    if a1 < 18.5:
        label4['text'] = 'MAGREZA'
    if a1 >= 18.5 and a1 <= 24.9:
        label4['text'] = 'PESO IDEAL'
    if a1 > 24.9 and a1 <= 29.9:
        label4['text'] = 'SOBREPESO'
    if a1 > 29.9 and a1 <= 39.9:
        label4['text'] = 'OBESIDADE'
    if a1 > 39.9:
        label['text'] = 'OBESIDADE GRAVE'

#Calculos, F
def calcularm():
    if entryp.get().isnumeric():
        labelc['text'] = float(entryp.get())*1.8+32



#IMC
label1 = Label(f1, text='Altura:',font='Arial 16', background='grey', foreground='black')
entry1 = Entry(f1,font='Arial 13')

label2 = Label(f1, text='Peso:',font='Arial 16',background='grey', foreground='black')
entry2 = Entry(f1,font='Arial 13')

btn3=Button(f1,text='IMC', font='Arial 10', command=calcular, background='light blue')
label3 = Label(f1, text='',font='Arial 16',background='grey', foreground='yellow')
label4 = Label(f1, text='',font='Arial 16',background='grey', foreground='yellow')

#F
labelp = Label(f2, text='C°:',font='Arial 16', background='dark Grey', foreground='black')
entryp = Entry(f2,font='Arial 13')

btnc=Button(f2,text='Converte F°', font='Arial 10', command=calcularm, background='light blue')
labelc = Label(f2, text='F°',font='Arial 16',background='Dark Grey', foreground='black')

#organizar
#f1
f1.grid(row=0,column=0)
label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
label2.grid(row=1,column=0)
entry2.grid(row=1,column=1)
btn3.grid(row=2,column=1)
label3.grid(row=3,column=1)
label4.grid(row=4,column=1)

#f2
f2.grid(row=0,column=2)
labelp.grid(row=0,column=0)
entryp.grid(row=0,column=1)
btnc.grid(row=1,column=1)
labelc.grid(row=2,column=1)

root.mainloop()