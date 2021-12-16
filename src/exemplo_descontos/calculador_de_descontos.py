from exemplo_descontos.orcamento import Orcamento, Item

class CalculadoraDescontos(object):

    def calcula(self, orcamento):

        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        elif orcamento.valor > 500:
            return orcamento.valor * 0.07

if __name__ == "__main__":
    orcamento = Orcamento()
    orcamento.adiciona_item(Item("Item - 01", 100))
    orcamento.adiciona_item(Item("Item - 01", 50))
    orcamento.adiciona_item(Item("Item - 01", 400))

    print(orcamento.valor)

    calculador = CalculadoraDescontos()
    desconto_calculado = calculador.calcula(orcamento)

    print(f"{desconto_calculado:.2f}")