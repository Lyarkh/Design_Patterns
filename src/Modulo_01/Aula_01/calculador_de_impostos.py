from orcamento import Orcamento, Item
from impostos import ISS, ICMS

class CalculadoraImpostos(object):

	def realiza_calculo(self, orcamento, imposto):
		imposto_calculado = imposto.calcula(orcamento)

		print(imposto_calculado)

if __name__ == '__main__':
	calculador = CalculadoraImpostos()
	orcamento = Orcamento()
	
	orcamento.adiciona_item(Item('ITEM 1', 50))
	orcamento.adiciona_item(Item('ITEM 2', 200))
	orcamento.adiciona_item(Item('ITEM 3', 250))

	calculador.realiza_calculo(orcamento, ISS())
	calculador.realiza_calculo(orcamento, ICMS())

