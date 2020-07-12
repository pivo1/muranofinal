from tkinter import *

from tkinter import ttk

import tkinter

import sqlite3

import csv

import os

import pandas as pd

import numpy as np

#criação da janela
root = Tk()




class Funcs():

    #apaga os textos das caixas de entrada
    def limpar_entradas(self):
        self.dre_entry.delete(0,END)
        self.curso_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.genero_entry.delete(0,END)
        self.data_entry.delete(0,END)
        self.altura_entry.delete(0,END)
        self.peso_entry.delete(0,END)
        self.cra_entry.delete(0,END)
        self.creditos_entry.delete(0,END)
        self.renda_entry.delete(0,END)


    #funçao p/ conectar no bando de dados
    def conecta_bd(self):
        self.conn = sqlite3.connect("alunos.bd")
        self.cursor = self.conn.cursor(); print("conectou no bd")

    def desconecta_bd(self):
        self.conn.close()

    def montarTabelas(self):

        self.conecta_bd();

        #criar tabela

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                DRE INTEGER,
                CURSO CHAR(40) NOT NULL,
                NOME CHAR(40) NOT NULL,
                GENERO CHAR(40),
                DATA_DE_NASCIMENTO CHAR(15),
                ALTURA REAL(10),
                PESO REAL(10),
                CRA REAL(10),
                CREDITOS_OBTIDOS INTEGER(10),
                RENDA INTEGER(20)
            );
        """)
        self.conn.commit(); print('BD CRIADO!')
        self.desconecta_bd()


    #conecta ao bd pra adicionar os dados
    def add_alunos(self):
        self.dre = self.dre_entry.get()
        self.curso = self.curso_entry.get()
        self.nome = self.nome_entry.get()
        self.genero = self.genero_entry.get()
        self.data = self.data_entry.get()
        self.altura = self.altura_entry.get()
        self.peso = self.peso_entry.get()
        self.cra = self.cra_entry.get()
        self.creditos = self.creditos_entry.get()
        self.renda = self.renda_entry.get()

        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO alunos (DRE, CURSO, NOME, GENERO, DATA_DE_NASCIMENTO,ALTURA, PESO, CRA, CREDITOS_OBTIDOS, RENDA)
              VALUES( ? , ? , ? , ? , ? , ? , ? , ? , ? , ? )""", (self.dre, self.curso, self.nome, self.genero, self.data, self.altura, self.peso, self.cra, self.creditos, self.renda))
        self.conn.commit()
        self.desconecta_bd()
        self.limpar_entradas()
        self.select_lista()

    def select_lista(self):
        self.lista.delete(*self.lista.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT DRE, CURSO, NOME, GENERO, DATA_DE_NASCIMENTO,ALTURA, PESO, CRA, CREDITOS_OBTIDOS, RENDA FROM alunos
          ORDER BY NOME ASC; """)

        #colocar os valores na treeviw na ordem certa
        for i in lista:
            self.lista.insert("", END, values = i )
        self.desconecta_bd()


    def export_csv(self):
        self.conecta_bd()
        # Export data into CSV file
        print
        "Exporting data into CSV............"
        self.conecta_bd()
        self.cursor.execute("select * from alunos")
        with open("alunos.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow([i[0] for i in self.cursor.description])
            csv_writer.writerows(self.cursor)

        dirpath = os.getcwd() + "/alunos.csv"
        print("Data exported Successfully into {}".format(dirpath))

        self.desconecta_bd()

    def bd_csv(self):
        conn = sqlite3.connect('alunos.bd')
        df = pd.read_sql_query("select * from alunos;",conn)
        renda_media = df['RENDA'].mean()
        cra_medio = df['CRA'].mean()
        num_alunos = len(df)
        self.desconecta_bd()




#classe com os widgets
class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.botoes_cadastro()
        self.lista_frame2()
        self.montarTabelas()
        self.select_lista()
        self.export_csv()
        self.bd_csv()
        # precisa ter um loop pra janela ficar aberta
        root.mainloop()

    #função com as configs da tela
    def tela(self):
        #mudando título
        self.root.title("Universidade Murano")

        #mudando cor
        self.root.configure(background="#2d3436")

        #tamanho inicial da janela
        self.root.geometry("800x600")

        #limitando o tamnho mínimo da tela
        self.root.minsize(width=800, height=600)

    def tela2(self):
        self.root2 = Toplevel()
        self.root2.title("Dados Estatísticos")
        self.root2.geometry("500x500")
        self.root2.resizable(False , False)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()
        self.bd_csv()
        conn = sqlite3.connect('alunos.bd')
        df = pd.read_sql_query("select * from alunos;", conn)
        renda_media = df['RENDA'].mean()
        cra_medio = df['CRA'].mean()
        num_alunos = len(df)
        self.desconecta_bd()
        texto = "RENDA MEDIA: {} \n CRA MEDIO{} \n NÚMERO DE ALUNOS: {}".format(renda_media,cra_medio,num_alunos)
        w = Label(self.root2, text = texto).pack()


    def frames(self):

        #criando frame dos cadastros
        self.frame_cadastro = Frame(self.root, bd = 4, highlightthickness=3)

        #configurando os labels
        self.frame_cadastro.place(relx= 0.04 , rely= 0.05 ,relwidth = 0.5, relheight = 0.90)

        # criando frame de visualização
        self.frame_visu = Frame(self.root, bd=4, highlightthickness=3)

        # configurando os labels
        self.frame_visu.place(relx=0.55, rely=0.05, relwidth=0.43, relheight=0.90)



    #função p/ crição dos botões

    def botoes_cadastro(self):



        #criando botão limpar
        self.bt_limpar = Button(self.frame_cadastro, text = 'Limpar', command= self.limpar_entradas)
        self.bt_limpar.place(relx = 0.01 , rely =0.1, relwidth = 0.2, relheight = 0.1)

        # criando botão novo
        self.bt_novo = Button(self.frame_cadastro, text='Novo', command = self.add_alunos)
        self.bt_novo.place(relx=0.25, rely=0.1, relwidth=0.2, relheight=0.1)

        # criando EXPORT CSV
        self.bt_novo = Button(self.frame_cadastro, text='Export CSV', command = self.export_csv)
        self.bt_novo.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.1)

        # criando botão dados estatísticos

        self.bt_novo = Button(self.frame_cadastro, text='Dados Estatísticos', command=self.tela2)
        self.bt_novo.place(relx=0.75, rely=0.1, relwidth=0.26, relheight=0.1)





        #criação label DRE e input
        self.lb_dre = Label(self.frame_cadastro, text = 'DRE')
        self.lb_dre.place(relx = 0.03, rely = 0.3)

        self.dre_entry = Entry(self.frame_cadastro)
        self.dre_entry.place(relx = 0.3 , rely = 0.3)

        #criação label curso e input
        self.lb_curso = Label(self.frame_cadastro, text = 'Curso')
        self.lb_curso.place(relx = 0.03, rely = 0.35)

        self.curso_entry = Entry(self.frame_cadastro)
        self.curso_entry.place(relx = 0.3 , rely = 0.35)

        #criação label nome e input
        self.lb_nome = Label(self.frame_cadastro, text = 'Nome')
        self.lb_nome.place(relx = 0.03, rely = 0.4)

        self.nome_entry = Entry(self.frame_cadastro)
        self.nome_entry.place(relx = 0.3 , rely = 0.4)


        #criação label gênero e input
        self.lb_genero = Label(self.frame_cadastro, text = 'Gênero')
        self.lb_genero.place(relx = 0.03, rely = 0.45)

        self.genero_entry = Entry(self.frame_cadastro)
        self.genero_entry.place(relx = 0.3 , rely = 0.45)

        #criação label Data de nascimento e input
        self.lb_data = Label(self.frame_cadastro, text = 'Data')
        self.lb_data.place(relx = 0.03, rely = 0.5)

        self.data_entry = Entry(self.frame_cadastro)
        self.data_entry.place(relx = 0.3 , rely = 0.5)


        #criação label altura e input
        self.lb_altura = Label(self.frame_cadastro, text = 'Altura')
        self.lb_altura.place(relx = 0.03, rely = 0.55)

        self.altura_entry = Entry(self.frame_cadastro)
        self.altura_entry.place(relx = 0.3 , rely = 0.55)

        #criação label peso e input
        self.lb_peso = Label(self.frame_cadastro, text = 'Peso')
        self.lb_peso.place(relx = 0.03, rely = 0.6)

        self.peso_entry = Entry(self.frame_cadastro)
        self.peso_entry.place(relx = 0.3 , rely = 0.6)


        #criação label CRA e input
        self.lb_cra = Label(self.frame_cadastro, text = 'CRA')
        self.lb_cra.place(relx = 0.03, rely = 0.65)

        self.cra_entry = Entry(self.frame_cadastro)
        self.cra_entry.place(relx = 0.3 , rely = 0.65)


        #criação label créditos e input
        self.lb_creditos = Label(self.frame_cadastro, text = 'Créditos Obtidos')
        self.lb_creditos.place(relx = 0.03, rely = 0.7)

        self.creditos_entry = Entry(self.frame_cadastro)
        self.creditos_entry.place(relx = 0.3 , rely = 0.7)


        #criação label renda e input
        self.lb_renda = Label(self.frame_cadastro, text = 'Renda')
        self.lb_renda.place(relx = 0.03, rely = 0.75)

        self.renda_entry = Entry(self.frame_cadastro)
        self.renda_entry.place(relx = 0.3 , rely = 0.75)

    #treeview
    def lista_frame2(self):

        #criando a treeview
        self.lista = ttk.Treeview(self.frame_visu, height = 3, column=("col1", 'col2', 'col3', 'col4', 'col5', 'col6', 'col7','col8','col9', 'col10'))
        self.lista.heading("#0", text = '')
        self.lista.heading("#1", text='DRE')
        self.lista.heading("#2", text='Curso')
        self.lista.heading("#3", text='Nome')
        self.lista.heading("#4", text='Gênero')
        self.lista.heading("#5", text='Data de Nascimento')
        self.lista.heading("#6", text='Altura')
        self.lista.heading("#7", text='Peso')
        self.lista.heading("#8", text='CRA')
        self.lista.heading("#9", text='Créditos Obtidos')
        self.lista.heading("#10", text='Renda')

        self.lista.column("#0", width=1)
        self.lista.column("#1", width=50)
        self.lista.column("#2", width=50)
        self.lista.column("#3", width=50)
        self.lista.column("#4", width=50)
        self.lista.column("#5", width=80)
        self.lista.column("#6", width=50)
        self.lista.column("#7", width=50)
        self.lista.column("#8", width=50)
        self.lista.column("#9", width=80)
        self.lista.column("#10", width=50)

        self.lista.place(relx = 0.05, rely = 0.1, relwidth = 0.95, relheight = 0.85 )


        #criando barra de rolagem

        self.scroollista = Scrollbar(self.frame_visu, orient='vertical')
        self.lista.configure(yscroll=self.scroollista.set)
        self.scroollista.place(relx = 0.97, rely = 0.1, relwidth = 0.03, relheight =0.85)















Application()









