from tkinter import *
from functools import partial

class Janela:

    def __init__(self, master):
        self.master = master
        self.criar_janela_principal_e_componentes()
        self.definir_layout()

    def criar_janela_principal_e_componentes(self):
        self.dividir_janela_principal_em_frames()
        self.criar_componentes_da_janela()

    def definir_layout(self):
        # self.__labelIdentificacaoDePrograma.grid(row=0, column=0, columnspan=2)
        # self.__labelCampoDeId.grid(row=1, column=0)
        # self.entradaDeId.grid(row=1, column=1)
        # self.__labelCampoDeSenha.grid(row=2, column=0)
        # self.entradaDeSenha.grid(row=2, column=1)
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

    def dividir_janela_principal_em_frames(self):
        self.criar_painel()
        self.dividir_painel()

        self.criar_areas_de_label_e_entrada()

        self.criar_frames_dos_identificadores()

        self.dividir_area_de_entrada()

    def criar_componentes_da_janela(self):
        self.criar_identificadores()

        self.criar_campos_de_entrada()

        self.criar_botao()


    def criar_painel(self):
        self.__painel = Tk()
        self.__painel.title("Login")
        self.__dimensoesDaTela = StringVar(self.__painel)
        self.__dimensoesDaTela.set("400x300+400+150")

    def dividir_painel(self):
        self.__ladoEsquerdoDoPainel = Frame(self.__painel)
        self.__ladoDireitoDoPainel = Frame(self.__painel)

    def criar_areas_de_label_e_entrada(self):
        self.__areaDeLabels = Frame(self.__ladoDireitoDoPainel)
        self.__areaDeEntrada = Frame(self.__ladoDireitoDoPainel, background="yellow")

    def criar_frames_dos_identificadores(self):
        self.__frameDeIdentificacaoDePrograma = Frame(self.__areaDeLabels, background="red")
        self.__frameDeLabelsIdentificadores = Frame(self.__areaDeLabels, background="purple")

    def dividir_area_de_entrada(self):
        self.__areaDeEntradaBranca = Frame(self.__areaDeEntrada)
        self.__areaEfetivaDeEntrada = Frame(self.__areaDeEntrada)

    def criar_identificadores(self):
        self.__labelIdentificacaoDePrograma = Label(self.__frameDeIdentificacaoDePrograma,
        text="Serviço de Login Bigarelli", background="red")
        self.__labelCampoDeId = Label(self.__frameDeLabelsIdentificadores, text="ID", background='blue')
        self.__labelCampoDeSenha = Label(self.__frameDeLabelsIdentificadores, text="Senha", background='pink')

    def criar_campos_de_entrada(self):
        self.entradaDeId = Entry(self.__areaEfetivaDeEntrada)
        self.entradaDeSenha = Entry(self.__areaEfetivaDeEntrada, show="*")
        self.id = ''
        self.senha = ''

    def criar_botao(self):
        self.botaoLogin = Button(self.__areaEfetivaDeEntrada, text="Login", command=self.master.efetuar_login)
        self.botaoLogin = Button(self.__areaEfetivaDeEntrada, text="Login", command=self.preparar_login)



    def preparar_login(self):
        self.id = self.entradaDeId.get()
        self.senha = self.entradaDeSenha.get()
        self.master.efetuar_login(self.id, self.senha)

    def mainloop(self):
        self.__painel.mainloop()
