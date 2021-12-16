from src.exemplo_descontos.orcamento import Orcamento
from exemplo_impostos.impostos import ISS, ICMS 

class CalculadoraImpostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)

        print (imposto_calculado)

if __name__ == "__main__":
    calculador = CalculadoraImpostos()
    orcamento = Orcamento(500)

    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())
