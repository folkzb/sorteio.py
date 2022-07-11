import random
from tkinter import *
import pandas as pd

analistas_lista = pd.read_excel("analista_pontos.xlsx", header=0)
analistas_lista.head()
analists_list = list(analistas_lista.analistas)
points_list = list(analistas_lista.pontos)

def sorteio_brabo():
    users = analists_list
    ganhador = (random.choices(users,weights=points_list))
    texto_ganhador = f"""O sorteado foi {ganhador}"""
    texto_ganhador = texto_ganhador.replace("[","").replace("'","").replace("]","")
    texto_sorteado ["text"] = texto_ganhador

janela = Tk()
janela.title('Sorteio V1')
janela.geometry("420x250")

bg = PhotoImage (file = "imagem.gif")
label1 = Label( janela, image = bg) 
label1.place(x = 0, y = 0)

texto_orientacao = Label(janela, text='Clique no botão para sortear o ganhador!')
texto_orientacao.place(x=103,y=16)

botao = Button(janela, text='Sortear', command=sorteio_brabo)
botao.place(x=190,y=80)

texto_sorteado = Label(janela, text="")
texto_sorteado.place (x=146,y=140)

creditos = Label(janela, text='Created by Bruno Fernandes', background="#A4BAFC", foreground="#000000")
creditos.place (x=196,y=200)

janela.mainloop()