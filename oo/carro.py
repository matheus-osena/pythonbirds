class Direcao():
    direcoes=["Norte","Leste","Sul","Oeste"] # só como exemplo
    def __init__(self):
        self.direcoes = ["Norte","Leste","Sul","Oeste"]
        self.v = 0

    def girar_a_direita(self):
        if self.v < 3:
            self.v += 1
        elif self.v >=3:
            self.v = 0

    def girar_a_esquerda(self):
        if self.v > 0:
            self.v -= 1
        elif self.v <=0:
            self.v = 3


    def valor(self):
        return self.direcoes[self.v]
    """se eu chamar "direções[self.v]" ao invés de "self.direcoes[self.v]" o código não funciona, não entendi o pq.
    Pensei que funcionaria já que "direcoes" é um atributo de classe. Mas funcionou somente com o atributo de instância"""

class Motor():
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def freiar(self):
        if self.velocidade <=2:
            self.velocidade =0
        elif self.velocidade > 2:
            self.velocidade -= 2

    def valor(self):
        return self.velocidade


class Carro():
    def __init__(self):
        self.motor = Motor()
        self.direcao = Direcao()

    def acelerar(self):
        self.motor.acelerar()

    def freiar(self):
        self.motor.freiar()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def calcular_velocidade(self):
        print(f"{self.motor.valor()}")

    def calcular_direcao(self):
        print(self.direcao.valor())
