class Pessoa:
    def __init__(self,nome=None,idade=0):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p =Pessoa()
    print(Pessoa.cumprimentar(p))

