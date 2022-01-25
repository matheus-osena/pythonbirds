from unittest import TestCase
from carro import Motor
from carro import Direcao
from carro import Carro

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0,motor.velocidade)
    def teste_direcao_inicial(self):
        direcao=Direcao()
        self.assertEqual("Norte",direcao.valor())
    def teste_aceleracao(self):
        motor =Motor()
        motor.acelerar()
        self.assertEqual(1,motor.velocidade)
    def teste_girar_a_direita(self):
        direcao =Direcao()
        direcao.girar_a_direita()
        self.assertEqual("Leste",direcao.valor())
    def teste_carro_aceleracao(self):
        carro = Carro()
        carro.acelerar()
        self.assertEqual(1,carro.calcular_velocidade())