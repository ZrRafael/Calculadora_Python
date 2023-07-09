# importanto tkinter
from tkinter import *
from tkinter import ttk

#cores

cor1 = "#454444"    #preta
cor2 = "#163d1b"     #verde
cor3 = "#fafafa"     #branco  
cor4 = "#e00000"     #vermelho
cor5 = "#e00000"     #azul



janela =Tk()
janela.title("Zr Calculando 😎")
janela.geometry("235x310")
janela.config(bg=cor1)


#frames

frame_tela = Frame(janela, width=235, height=50,bg=cor1)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268,bg=cor3)
frame_corpo.grid(row=1, column=0)


#variavel valores
#label

todos_valores = ''

#função

def entre_valores (event):
    
    global todos_valores
    
    todos_valores = todos_valores + str(event)
    
    
    #passando
    valor_texto.set(todos_valores)
    
    #função calcular
    
def calcular():
        resultado = eval(todos_valores)
        print(resultado)
        
        
        valor_texto.set(str(resultado))
    
    #limpar
def limpar_tela():
        global  todos_valores
        todos_valores=''
        valor_texto.set('')
    
    

#label
valor_texto = StringVar()

app_label =Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e",justify=RIGHT,fg=cor3,font=('ivy 18'), bg=cor1)
app_label.place(x=0,y=0)


# botões

b_1 = Button(frame_corpo,command=limpar_tela, text="C", width=11, height=2,bg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo,command=lambda: entre_valores('%'), text="%", width=5, height=2,bg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, command=lambda: entre_valores('/'),text="/", width=5, height=2,bg=cor2, fg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, command=lambda: entre_valores('7'),text="7", width=5, height=2,bg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command=lambda: entre_valores('8'),text="8", width=5, height=2,bg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, command=lambda: entre_valores('9'),text="9", width=5, height=2,bg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, command=lambda: entre_valores('*'),text="*", width=5, height=2,bg=cor2, fg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(frame_corpo, command=lambda: entre_valores('4'),text="4", width=5, height=2,bg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command=lambda: entre_valores('5'),text="5", width=5, height=2,bg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, command=lambda: entre_valores('6'),text="6", width=5, height=2,bg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, command=lambda: entre_valores('-'),text="-", width=5, height=2,bg=cor2, fg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo, command=lambda: entre_valores('1'),text="1", width=5, height=2,bg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command=lambda: entre_valores('2'),text="2", width=5, height=2,bg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_corpo, command=lambda: entre_valores('3'),text="3", width=5, height=2,bg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, command=lambda: entre_valores('+'),text="+", width=5, height=2,bg=cor2, fg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo, command=lambda: entre_valores('0'),text="0", width=11, height=2,bg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, command=lambda: entre_valores('.'),text=".", width=5, height=2,bg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_corpo, command=calcular,  text="=", width=5, height=2,bg=cor2, fg=cor3,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


    
   
    
    
    

janela.mainloop()