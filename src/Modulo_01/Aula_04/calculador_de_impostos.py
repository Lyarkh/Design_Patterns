from orcamento import Orcamento, Item
from impostos import ISS, ICMS, ICPP, IKCV 

class CalculadoraImpostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)

        print (imposto_calculado)

if __name__ == "__main__":
    orcamento = Orcamento()
    calculador = CalculadoraImpostos()

    orcamento.adiciona_item(Item("Item 01", 50))
    orcamento.adiciona_item(Item("Item 01", 200))
    orcamento.adiciona_item(Item("Item 01", 250))

    print("---- ISS e ICMS ----")
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print("\n---- ISS c/ ICMS ----")
    calculador.realiza_calculo(orcamento, ISS(ICMS()))
    
    print("\n---- ICPP e IKCV ----")
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())

    print("\n---- ICPP c/ IKCV ----")
    calculador.realiza_calculo(orcamento, ICPP(IKCV()))

    
