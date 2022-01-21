class Pessoa:
    def __init__(self,nome=None,idade=0,*filhos):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    matheus = Pessoa('Matheus',25)
    edmilson = Pessoa("Edmilson",60,matheus)
    for filhos in edmilson.filhos:
        print(filhos.nome)

