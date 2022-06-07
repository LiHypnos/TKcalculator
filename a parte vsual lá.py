from tkinter import *

root=Tk()
#criando a janela
root.title('Windows Execute')
root.geometry('400x200+100+500')
root.minsize(width=650, height=300)
root.maxsize(width=1200, height=600)
root.config(bg=('dark grey'))
#configurando os frames
f1=Frame(root,background='Dark Grey')
f2=Frame(root,background='Dark Grey')
f3=Frame(root,background='Dark Grey')

#configurando os frames
#f1
lb1=Label(f1,text='Dados Pessoais', font= 'Arial 20',bg='Dark Grey')
lb2=Label(f1,text='Nome:',font='Arial 14',bg='Dark Grey')
ent1=Entry(f1,font='Arial 14',bg='Dark Grey')
lb3=Label(f1, text='Data Nasc:',font='Arial 14',bg='Dark Grey')
ent2=Entry(f1,font='Arial 14',bg='Dark Grey')
lb4=Label(f1, text='CPF:',font='Arial 14',bg='Dark Grey')
ent3=Entry(f1,font='Arial 14',bg='Dark Grey')
lb5=Label(f1, text='Telefone:',font='Arial 14',bg='Dark Grey')
ent4=Entry(f1,font='Arial 14',bg='Dark Grey')
#f2 -  rua,n, bairro, cidade,UF
lbl1=Label(f2,text='Endereço',font='Arial 20',bg='Dark Grey')
lbl2=Label(f2, text='Rua:', font='Arial 14',bg='Dark Grey')
en1=Entry(f2,font='Arial 14',bg='Dark Grey')
lbl3=Label(f2, text='Nº:', font='Arial 14',bg='Dark Grey')
en2=Entry(f2,font='Arial 14',bg='Dark Grey')
lbl4=Label(f2,text='Bairro:',font='Arial 14',bg='Dark Grey')
en3=Entry(f2,font='Arial 14',bg='Dark Grey')
lbl5=Label(f2,text='Cidade:',font='Arial 14',bg='Dark Grey')
en4=Entry(f2,font='Arial 14',bg='Dark Grey')
lbl6=Label(f2,text='UF:', font='Arial 14',bg='Dark Grey')
en5=Entry(f2,font='Arial 14',bg='Dark Grey')
#f3
btn=Button(f3, text='Salvar', font='Arial 11', background='light blue')
btn2=Button(f3, text='Imprimir', font='Arial 11', background='light blue')
#organizando
#f1
f1.grid(row=0,column=0)
lb1.grid(row=0)
lb2.grid(row=1)
ent1.grid(row=1,column=1)
lb3.grid(row=2)
ent2.grid(row=2,column=1)
lb4.grid(row=3)
ent3.grid(row=3,column=1)
lb5.grid(row=4)
ent4.grid(row=4,column=1)
#f2
f2.grid(row=1,column=0)
lbl1.grid(row=0)
lbl2.grid(row=1)
en1.grid(row=1,column=1)
lbl3.grid(row=1,column=2)
en2.grid(row=1,column=3)
lbl4.grid(row=2)
en3.grid(row=2,column=1)
lbl5.grid(row=2)
en4.grid(row=2,column=1)
lbl6.grid(row=2,column=2)
en5.grid(row=2,column=3)
#f3
f3.grid(row=2,column=0)
btn.grid(row=0,column=0)
btn2.grid(row=0,column=1)


root.mainloop()