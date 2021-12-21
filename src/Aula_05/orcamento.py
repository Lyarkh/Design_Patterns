from abc import ABCMeta, abstractmethod

class EstadoDeUmOrcamento(metaclass=ABCMeta):

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprovado(self, orcamento):
        pass

    @abstractmethod
    def reprovado(self, orcamento):
        pass

    @abstractmethod
    def finalizado(self, orcamento):
        pass

class EmAprovacao(EstadoDeUmOrcamento):
    
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprovado(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprovado(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finalizado(self, orcamento):
        raise Exception("Um orçamento em aprovação não pode ir para finalizado.")

class Aprovado(EstadoDeUmOrcamento):

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
    
    def aprovado(self, orcamento):
        raise Exception("Orçamento já está aprovado!")

    def reprovado(self, orcamento):
        raise Exception("Orçamentos aprovados não podem ser reprovados.")

    def finalizado(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Reprovado(EstadoDeUmOrcamento):

    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orçamentos reprovados não recebem desconto extra!")
    
    def aprovado(self, orcamento):
        raise Exception("Orçamentos reprovados não podem ser aprovados.")

    def reprovado(self, orcamento):
        raise Exception("Orçamento já está reprovado!")

    def finalizado(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Finalizado(EstadoDeUmOrcamento):

    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orçamentos finalizados não recebem desconto extra!")
    
    def aprovado(self, orcamento):
        raise Exception("Orçamento já finalizado e não pode ser aprovado.")

    def reprovado(self, orcamento):
        raise Exception("Orçamento já finalizado e não pode ser reprovado.")

    def finalizado(self, orcamento):
        raise Exception("Orçamento já finalizado!")

class Orcamento(object):

    def __init__(self):
        self.__itens = []
        self.estado_atual = EmAprovacao()
        self.__desconto_extra = 0
    
    def aprovado(self):
        self.estado_atual.aprovado(orcamento)

    def reprovado(self):
        self.estado_atual.reprovado(orcamento)

    def finalizado(self):
        self.estado_atual.finalizado(orcamento)

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor

        return total - self.__desconto_extra
    
    def obter_itens(self):
        return tuple(self.__itens)
    
    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

class Item(object):
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property  
    def valor(self):
        return self.__valor
        
    @property  
    def nome(self):
        return self.__nome
    
if __name__ == "__main__":
    orcamento = Orcamento()

    orcamento.adiciona_item(Item("Item 01", 100))
    orcamento.adiciona_item(Item("Item 01", 50))
    orcamento.adiciona_item(Item("Item 01", 400))
    
    print(orcamento.valor)
    orcamento.reprovado()
    orcamento.reprovado()
    
    orcamento.aplica_desconto_extra()

    print(orcamento.valor)
    



