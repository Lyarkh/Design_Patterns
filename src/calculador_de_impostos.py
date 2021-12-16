from orcamento import Orcamento

class CalculadoraImpostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto = imposto.upper()

        if imposto == "ISS":
            imposto_calculado = orcamento.valor * 0.1
        if imposto == "ICMS":
            imposto_calculado = orcamento.valor * 0.06

        print (imposto_calculado)

if __name__ == "__main__":
    calculador = CalculadoraImpostos()
    orcamento = Orcamento(500)

    calculador.realiza_calculo(orcamento, "iss")
    calculador.realiza_calculo(orcamento, "icms")
