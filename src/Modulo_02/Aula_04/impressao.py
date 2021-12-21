#Erro na hora de impressao -> Imprimindo "None"

class Impressora(object):

    def visita_soma(self, soma):
        print (f'( {soma.expressao_esquerda.aceita(self)}  + {soma.expressao_direita.aceita(self)} )')

    def visita_subtracao(self, subtracao):
        print(f'( {subtracao.expressao_esquerda.aceita(self)} - {subtracao.expressao_direita.aceita(self)} )')

    def visita_numero(self, numero):
        print(numero.avalia())