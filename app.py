from janela import Janela
from conexao_sql import *
from gerenciador_de_mensagens import GerenciadorDeMensagens

class Aplicativo:
    CAMPO_DE_LOGIN = 1
    CAMPO_DE_SENHA = 2
    def __init__(self):
        self.janelaPrincipal = Janela(self)

    def executar(self):
        self.janelaPrincipal.mainloop()

    def efetuar_login(self, id, senha):
        try:
            self.conexaoSql = ConexaoSql()
            self.conexaoSql.conectar()

            if not self.conexaoSql.conexaoAberta:
                raise ErroDeConexao("Não foi possível se conectar à base de dados.")

            self.gerenciador_de_mensagens = GerenciadorDeMensagens()

            self.respostaDeQuery = self.conexaoSql.ler_banco_de_dados()

            for linha in self.respostaDeQuery:
                if id != linha[Aplicativo.CAMPO_DE_LOGIN]:
                    self.gerenciador_de_mensagens.exibir_mensagem("Erro de Login", "Login inválido.")
                else:
                    if senha != linha[Aplicativo.CAMPO_DE_SENHA]:
                        self.gerenciador_de_mensagens.exibir_mensagem("Erro de Login", "Senha inválida.")
                    else:
                        self.gerenciador_de_mensagens.exibir_mensagem("Login", "Login realizado com sucesso.")
        except ErroDeConexao as erro:
            self.gerenciador_de_mensagens.exibir_mensagem("Erro de conexão", erro.mensagem)
        finally:
            if self.conexaoSql:
                self.conexaoSql.desconectar()
