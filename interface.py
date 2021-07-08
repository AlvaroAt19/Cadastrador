#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Criador: Alvaro


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import cadastrador


root = Tk()
root.geometry('600x400')
root.title('Cadastrador')
root.resizable(False,False)

#Organizando frames
img = Image.open('Img/img.png') #abrindo a imagem
img = img.resize((200,200),Image.ANTIALIAS) #Alterando o tamanho
img = ImageTk.PhotoImage(img) #Convertendo para Tk

LFrame = Frame(root, width=200, height=400, bg='GOLD')
LFrame.pack(side=LEFT)

RFrame = Frame(root, width=400, height=400, bg='#856ff8')
RFrame.pack(side=RIGHT)

#Frame Esquerdo:
imgLabel = Label(LFrame,image=img, bg='GOLD')
imgLabel.place(x=0, y=100)

#Frame Direito:
#Cadastrar
def cadastro():
    """Cadastra novas pessoas no banco de dados"""
    CFrame = Frame(RFrame, width=600, height=600, bg='#856ff8')
    CFrame.pack()

    #Nome
    Nome_lbl = ttk.Label(CFrame, text='Nome:', width=40, background='#856ff8', foreground='white')
    Nome_lbl.place(x=0,y=50)
    Nome_entry = ttk.Entry(CFrame, width=40)
    Nome_entry.place(x=70, y=50)

    #Endereço
    Adress_lbl = ttk.Label(CFrame, text='Endereço:', width=40, background='#856ff8', foreground='white')
    Adress_lbl.place(x=0,y=100)
    Adress_entry = ttk.Entry(CFrame, width=40)
    Adress_entry.place(x=70, y=100)

    #Celular
    Cel_lbl = ttk.Label(CFrame, text='Telefone:', width=40, background='#856ff8', foreground='white')
    Cel_lbl.place(x=0,y=150)
    Cel_entry = ttk.Entry(CFrame, width=40)
    Cel_entry.place(x=70, y=150)

    #Data de aniversário
    Birth_lbl = ttk.Label(CFrame, text='Nascimento:', width=20, background='#856ff8', foreground='white')
    Birth_lbl.place(x=0,y=200)
    Birth_entry = ttk.Entry(CFrame, width=40)
    Birth_entry.place(x=75, y=200)


    #Graduação
    Grad_lbl = ttk.Label(CFrame, text='Graduação:', width=40, background='#856ff8', foreground='white')
    Grad_lbl.place(x=0,y=250)
    Grad_entry = ttk.Entry(CFrame, width=40)
    Grad_entry.place(x=70, y=250)


    def salvar():
        """Salva as informações no banco de dados"""

        #Garantindo que todas as informações foram preenchidas
        if Nome_entry.get()=="" or Adress_entry.get()=="" or Cel_entry.get()=="" or Birth_entry.get()=="" or Grad_entry.get()=="":
            messagebox.showwarning("ERRO","Preencha todos os campos")

        else:
            Nome = Nome_entry.get().lower()
            Adress = Adress_entry.get().lower()
            Cel = Cel_entry.get().lower()
            Birth = Birth_entry.get().lower()
            Grad = Grad_entry.get().lower()

            #Inserindo e fazendo commit
            cadastrador.cursor.execute('''
                INSERT INTO Pessoas(Nome, Endereco, Cel, Nasc, Grad) VALUES(?,?,?,?,?);
                ''', (Nome,Adress,Cel,Birth,Grad))
            cadastrador.conn.commit()

            Nome_entry.delete(0, 'end')
            Adress_entry.delete(0, 'end')
            Cel_entry.delete(0, 'end')
            Birth_entry.delete(0, 'end')
            Grad_entry.delete(0, 'end')

            messagebox.showinfo("Sucesso","Cadastrado com Sucesso")


    save = Button(CFrame, text = 'Salvar', width = 30, command=salvar)#Botão para ativar a função salvar
    save.place(x=100, y=330)

    Retornar = Button(CFrame, text = 'Retornar', width = 30, command=lambda:back(CFrame)) #Botão para retornar ao frame anterior
    Retornar.place(x=100, y=370)


Cadastro_btn = ttk.Button(RFrame, text = 'Cadastrar Informação', width = 40, command=cadastro)#Botão para ativar a função cadastro
Cadastro_btn.place(x=50, y=50)


#Editar
def editar():
    """Inicia a edição de informações por meio do ID"""

    EFrame = Frame(RFrame, width=600, height=600, bg='#856ff8')
    EFrame.pack()

    ID_lbl = ttk.Label(EFrame, text='ID:', width=40, background='#856ff8', foreground='white')
    ID_lbl.place(x=0,y=50)
    ID_entry = ttk.Entry(EFrame, width=40)
    ID_entry.place(x=70, y=50)


    def edit():
        """Abre a janela de edição com as informações"""
        cadastrador.cursor.execute('''
            SELECT * FROM Pessoas WHERE ID = ? ;
            ''',(ID_entry.get(),))
        Pessoa = cadastrador.cursor.fetchone()

        if Pessoa:

            EdFrame = Frame(EFrame, width=600, height=600, bg='#856ff8')
            EdFrame.pack()

            #Nome
            Nome = Pessoa[1]
            Nome_lbl = ttk.Label(EdFrame, text='Nome:', width=40, background='#856ff8', foreground='white')
            Nome_lbl.place(x=0,y=50)
            Nome_entry = ttk.Entry(EdFrame, width=40)
            Nome_entry.place(x=70, y=50)
            Nome_entry.insert(0,Nome)

            #Endereço
            Adress = Pessoa[2]
            Adress_lbl = ttk.Label(EdFrame, text='Endereço:', width=40, background='#856ff8', foreground='white')
            Adress_lbl.place(x=0,y=100)
            Adress_entry = ttk.Entry(EdFrame, width=40)
            Adress_entry.place(x=70, y=100)
            Adress_entry.insert(0,Adress)

            #Celular
            Cel = Pessoa[3]
            Cel_lbl = ttk.Label(EdFrame, text='Telefone:', width=40, background='#856ff8', foreground='white')
            Cel_lbl.place(x=0,y=150)
            Cel_entry = ttk.Entry(EdFrame, width=40)
            Cel_entry.place(x=70, y=150)
            Cel_entry.insert(0,Cel)

            #Data de aniversário
            Birth = Pessoa[4]
            Birth_lbl = ttk.Label(EdFrame, text='Nascimento:', width=20, background='#856ff8', foreground='white')
            Birth_lbl.place(x=0,y=200)
            Birth_entry = ttk.Entry(EdFrame, width=40)
            Birth_entry.place(x=75, y=200)
            Birth_entry.insert(0,Birth)

            #Graduação
            Grad = Pessoa[5]
            Grad_lbl = ttk.Label(EdFrame, text='Graduação:', width=40, background='#856ff8', foreground='white')
            Grad_lbl.place(x=0,y=250)
            Grad_entry = ttk.Entry(EdFrame, width=40)
            Grad_entry.place(x=70, y=250)
            Grad_entry.insert(0,Grad)


            def save_change():
                """Salva as edições feitas no banco de dados"""

                #Garantindo que todas as informações foram preenchidas
                if Nome_entry.get()=="" or Adress_entry.get()=="" or Cel_entry.get()=="" or Birth_entry.get()=="" or Grad_entry.get()=="":
                    messagebox.showwarning("ERRO","Preencha todos os campos")

                else:
                    Nome = Nome_entry.get().lower()
                    Adress = Adress_entry.get().lower()
                    Cel = Cel_entry.get().lower()
                    Birth = Birth_entry.get().lower()
                    Grad = Grad_entry.get().lower()

                    #Inserindo e fazendo commit
                    cadastrador.cursor.execute('''
                        UPDATE Pessoas
                        SET Nome = ?,
                        Endereco = ?,
                        Cel = ?,
                        Nasc = ?,
                        Grad = ?
                        WHERE ID = ?;
                        ''', (Nome,Adress,Cel,Birth,Grad, ID_entry.get()))

                    cadastrador.conn.commit()


                    messagebox.showinfo("Sucesso","Cadastrado alterado com Sucesso")

                    EdFrame.destroy()



            Save_Change_btn = Button(EdFrame, text = 'Salvar', width = 30, command=save_change)#Salva as alterações feitas
            Save_Change_btn.place(x=100, y=330)


        else:
            messagebox.showwarning("ERRO","Preencha um ID válido")

    Edit_btn = Button(EFrame, text='Editar', width=20, command=edit) #Inicia a função edit
    Edit_btn.place(x=20, y=100)

    Retornar = Button(EFrame, text = 'Retornar', width = 20, command=lambda:back(EFrame))#Retorna ao frame anterior
    Retornar.place(x=210, y=100)


Editar_btn = ttk.Button(RFrame, text = 'Editar Informação', width = 40, command=editar)#Inicia a funçaõ editar
Editar_btn.place(x=50, y=150)


#Excluir
def delete():
    """Iniciar a exclusão de uma pessoa no banco de dados por meio do ID"""

    DFrame = Frame(RFrame, width=600, height=600, bg='#856ff8')
    DFrame.pack()

    ID_lbl = ttk.Label(DFrame, text='ID:', width=40, background='#856ff8', foreground='white')
    ID_lbl.place(x=0,y=50)
    ID_entry = ttk.Entry(DFrame, width=40)
    ID_entry.place(x=70, y=50)


    def excluir():
        """Botão para completar a exclusão"""
        cadastrador.cursor.execute('''
            SELECT * FROM Pessoas WHERE ID = ? ;
            ''',(ID_entry.get(),))
        Pessoa = cadastrador.cursor.fetchone()

        if Pessoa:
            cadastrador.cursor.execute('''
                Delete FROM Pessoas WHERE ID = ? ;
                ''',(ID_entry.get(),))
            cadastrador.conn.commit()

            ID_entry.delete(0, 'end')

            messagebox.showinfo("Sucesso","Excluido com Sucesso")

        else:
            messagebox.showinfo("Atenção","Preencha um ID válido que deseja deletar")


    Excluir_btn = Button(DFrame, text='Excluir', width=20, command=excluir)#Inicia a função excluir
    Excluir_btn.place(x=20, y=100)

    Retornar = Button(DFrame, text = 'Retornar', width = 20, command=lambda:back(DFrame))#Retorna ao frame anterior
    Retornar.place(x=210, y=100)


Del_btn = ttk.Button(RFrame, text = 'Excluir Informação', width = 40, command=delete)#Inicia a função delete
Del_btn.place(x=50, y=250)


#Localizar
def search():
    """Procura pessoas por meio do Nome"""
    SFrame = Frame(RFrame, width=600, height=600, bg='#856ff8')
    SFrame.pack()

    Nome_lbl = ttk.Label(SFrame, text='Nome:', width=40, background='#856ff8', foreground='white')
    Nome_lbl.place(x=0,y=50)
    Nome_entry = ttk.Entry(SFrame, width=40)
    Nome_entry.place(x=70, y=50)


    def procurar():
        """Botão para ativar a procura"""
        PFrame = Frame(SFrame, width=600, height=600, bg='#856ff8')
        PFrame.place(x=0,y=150)

        Nome = Nome_entry.get().lower()

        cadastrador.cursor.execute('''
            SELECT * FROM Pessoas WHERE Nome REGEXP ? ;
            ''',(Nome,))
        Pessoas = cadastrador.cursor.fetchall()

        Info_lbl = ttk.Label(PFrame,text='Id    Nome    Endereço    Cel     Nasc    Grad', background='#856ff8', foreground='white')
        Info_lbl.place(x=0,y=10)

        y=50
        for i,pessoa in enumerate(Pessoas):
            i_lbl = ttk.Label(PFrame, text=str(pessoa),background='#856ff8', foreground='white')
            i_lbl.place(x=0,y=y)
            y+=30


    Procurar_btn = Button(SFrame, text='Procurar', width=20, command=procurar)#inifia a função procurar
    Procurar_btn.place(x=20, y=100)

    Retornar = Button(SFrame, text = 'Retornar', width = 20, command=lambda:back(SFrame))#retorna ao frame anterior
    Retornar.place(x=210, y=100)


Search_btn = ttk.Button(RFrame, text = 'Procurar Informação', width = 40, command=search)#inicia a função search
Search_btn.place(x=50, y=350)


#BackButton
def back(frame):
    """Deleta o frame atual retornando ao frame anterior"""
    frame.destroy()


root.mainloop()
