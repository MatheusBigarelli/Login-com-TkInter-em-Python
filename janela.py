from tkinter import *
from functools import partial

class Janela:
    '''
    # Componentes.
    __painel
    __labelIdentificacaoDePrograma
    __labelCampoDeId
    __labelCampoDeSenha
    entradaDeId
    entradaDeSenha
    '''
    def __init__(self, master):
        self.master = master
        self.criar_componentes()
        self.criar_layout()

    def criar_componentes(self):
        self.__painel = Tk()
        self.__painel.title("Login")

        self.__dimensoesDaTela = StringVar(self.__painel)
        self.__dimensoesDaTela.set("400x300+400+150")

        self.__ladoEsquerdoDoPainel = Frame(self.__painel)
        self.__ladoDireitoDoPainel = Frame(self.__painel)

        self.__areaDeLabels = Frame(self.__ladoDireitoDoPainel)
        self.__areaDeEntrada = Frame(self.__ladoDireitoDoPainel, background="yellow")

        self.__frameDeIdentificacaoDePrograma = Frame(self.__areaDeLabels, background="red")
        self.__frameDeLabelsIdentificadores = Frame(self.__areaDeLabels, background="purple")

        self.__areaDeEntradaBranca = Frame(self.__areaDeEntrada)
        self.__areaEfetivaDeEntrada = Frame(self.__areaDeEntrada)



        self.__labelIdentificacaoDePrograma = Label(self.__frameDeIdentificacaoDePrograma, text="Serviço de Login Bigarelli", background="red")

        self.__labelCampoDeId = Label(self.__frameDeLabelsIdentificadores, text="ID", background='blue')
        self.__labelCampoDeSenha = Label(self.__frameDeLabelsIdentificadores, text="Senha", background='pink')
        self.entradaDeId = Entry(self.__areaEfetivaDeEntrada)
        self.entradaDeSenha = Entry(self.__areaEfetivaDeEntrada, show="*")

        self.botaoLogin = Button(self.__areaEfetivaDeEntrada, text="Login", command=self.master.efetuar_login)
        self.id = ''
        self.senha = ''
        self.botaoLogin = Button(self.__areaEfetivaDeEntrada, text="Login", command=self.preparar_login)

    def criar_layout(self):
        self.__labelIdentificacaoDePrograma.grid(row=0, column=0, columnspan=2)
        self.__labelCampoDeId.grid(row=1, column=0)
        self.entradaDeId.grid(row=1, column=1)
        self.__labelCampoDeSenha.grid(row=2, column=0)
        self.entradaDeSenha.grid(row=2, column=1)
        self.__painel.geometry(self.__dimensoesDaTela.get())
        
        self.__ladoEsquerdoDoPainel.pack(side=LEFT, expand=True)
        self.__ladoDireitoDoPainel.pack(side=RIGHT, expand=True)

        self.__areaDeLabels.pack(side=LEFT, expand=True)
        self.__areaDeEntrada.pack(side=RIGHT, expand=True)

        self.__frameDeIdentificacaoDePrograma.pack(side=TOP, expand=True, fill=BOTH)
        self.__frameDeLabelsIdentificadores.pack(side=BOTTOM, expand=True)

        self.__labelIdentificacaoDePrograma.pack(expand=True, side=TOP)

        self.__labelCampoDeId.pack(expand=False, side=TOP)
        self.__labelCampoDeSenha.pack(expand=True, side=TOP)

        self.__areaDeEntradaBranca.pack(expand=True, side=TOP)
        self.__areaEfetivaDeEntrada.pack(expand=True, side=TOP)

        self.entradaDeId.pack(expand=False, side=TOP)
        self.entradaDeSenha.pack(expand=False, side=TOP)

        self.botaoLogin.pack(expand=False)


    def preparar_login(self):
        self.id = self.entradaDeId.get()
        self.senha = self.entradaDeSenha.get()
        self.master.efetuar_login(self.id, self.senha)

    def mainloop(self):
        self.__painel.mainloop()
