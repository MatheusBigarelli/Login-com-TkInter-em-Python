from tkinter import *

class GerenciadorDeMensagens:
    tamanhoMinimo = 150
    def __init__(self):
        pass

    def exibir_mensagem(self, titulo, mensagem):
        self.criar_janela_de_mensagem(titulo, len(mensagem))
        self.exibir_conteudo(mensagem)

    def criar_janela_de_mensagem(self, titulo, tamanhoHorizontal):
        self.janela = Tk()
        self.caixaDeMensagem = Label(self.janela)
        # self.janela.geometry("300x200+400+150")

        if 10 * tamanhoHorizontal > GerenciadorDeMensagens.tamanhoMinimo:
            self.tamanhoHorizontal = str(10 * tamanhoHorizontal)
        else:
            self.tamanhoHorizontal = str(GerenciadorDeMensagens.tamanhoMinimo)
        self.janela.geometry(self.tamanhoHorizontal + "x200+400+150")
        self.janela.title(titulo)
        self.caixaDeMensagem.place(x=50, y=80)

    def exibir_conteudo(self, mensagem):
        self.caixaDeMensagem["text"] = mensagem
        self.janela.mainloop()
