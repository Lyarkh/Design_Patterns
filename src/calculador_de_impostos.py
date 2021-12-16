from orcamento import Orcamento
from impostos import calcula_ISS, calcula_ICMS 

class CalculadoraImpostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto = imposto.upper()

        if imposto == "ISS":
            imposto_calculado = calcula_ISS(orcamento)
        if imposto == "ICMS":
            imposto_calculado = calcula_ICMS(orcamento)

        print (imposto_calculado)

if __name__ == "__main__":
    calculador = CalculadoraImpostos()
    orcamento = Orcamento(500)

    calculador.realiza_calculo(orcamento, "iss")
    calculador.realiza_calculo(orcamento, "icms")
