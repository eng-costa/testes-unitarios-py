# 1) Importar a classe "Calculadora"
from calculadora import Calculadora

# 2) Importar o pacote de testes unitários chamdo "unittest"
import unittest

# 3) Criando a classe de testes unitários
class TestCalculadora(unittest.TestCase):
    # 4)Criando o objeto que herdará a classe "Calculadora"

    # OBS: é necessário usar o método chamado "setUp()"
    def setUp(self):
        self.calc = Calculadora()
    
    # Criar o método de teste do método "soma()"
    def test_soma(self):
        self.assertEqual(self.calc.soma(2,3), 5, "Deve somar dois números")
    
    # Criar o método de teste do método "subtracao()"
    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(5,3), 2, "Deve subtrair dois números")

    # Criar o método de teste do método "multiplicacao()"
    def test_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(10,2), 20, "Deve multiplicar dois números")

    # Criar o método de teste do método "divisao()"
    def test_divisao(self):
        self.assertEqual(self.calc.divisao(10,2), 5, "Deve dividir dois números")
    
    # EXTRA:Criar o método de teste para uma divisao por zero
    def test_divisao_por_zero(self):
        self.assertEqual(self.calc.divisao(1,0), "Divisao invalida")

# Executar a classe de testes unitários
if __name__ == '__main__':
    unittest.main()