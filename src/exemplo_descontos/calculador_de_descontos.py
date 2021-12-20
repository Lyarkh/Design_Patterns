from orcamento import Orcamento, Item
from descontos import DescontoPorCincoItens, DescontPorMaisDeQuinhentosReais, SemDesconto

class CalculadoraDescontos(object):

    def calcula(self, orcamento):
        desconto = DescontoPorCincoItens(DescontPorMaisDeQuinhentosReais(SemDesconto)).calcula(orcamento)
        return desconto
        
if __name__ == "__main__":
    orcamento = Orcamento()
    orcamento.adiciona_item(Item("Item - 01", 100))
    orcamento.adiciona_item(Item("Item - 01", 50))
    orcamento.adiciona_item(Item("Item - 01", 400))

    calculador = CalculadoraDescontos()
    desconto_calculado = calculador.calcula(orcamento)

    print(f"{desconto_calculado:.2f}")