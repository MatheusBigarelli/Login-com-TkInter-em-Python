import sqlite3

class ConexaoSql:
    def __init__(self):
        self.__pathDoBancoDeDados = r'C:\Users\mathe\sqlite\Servico de Login.db'
        self.conexaoAberta = False

    def conectar(self):
        try:
            self.conexao = sqlite3.connect(self.__pathDoBancoDeDados)
            self.conexaoAberta = True
        except:
            self.conexaoAberta = False

    def desconectar(self):
        try:
            self.conexao.close()
        except:
            pass
    def ler_banco_de_dados(self):
        self.__cursor = self.conexao.cursor()
        resultado = self.__cursor.execute("SELECT * FROM usuarios")
        return resultado


class ErroDeConexao(RuntimeError):
    def __init__(self, mensagem):
        self.mensagem = mensagem
