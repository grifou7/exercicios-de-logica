import base64

class Criptografia:

    def __init__(self, mensagem_original="", mensagem_criptografa=""):
        self.mensagem_original = mensagem_original
        self.mensagem_criptografa = mensagem_criptografa
    def criptografar_mensagem(self):
        mensagem_bytes = self.mensagem_original.encode("ascii")
        base64_bytes = base64.b64encode(mensagem_bytes)
        base64_mensagem = base64_bytes.decode("ascii")
        self.mensagem_criptografa = base64_mensagem
        print(f"Frase criptografada:  {base64_mensagem}")

    def descriptografarMensagem(self):
        Dbase64_bytes = self.mensagemCriptografada.encode("ascii")
        msg_decrito_bytes = base64.b64decode(Dbase64_bytes)
        self.mensagemdescriptografada = msg_decrito_bytes.decode("ascii")
        print(f"Mensagem descriptografada: {self.mensagemdescriptografada}")

if __name__ == '__main__':
    primeira_mensagem = Criptografia("Estudar python com professor")
    primeira_mensagem.criptografar_mensagem()
    primeira_mensagem.descriptografarMensagem