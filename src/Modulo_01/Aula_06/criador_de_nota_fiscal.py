from datetime import date
from nota_fiscal import NotaFiscal, Item

class CriadorDeNotaFiscal(object):

    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__itens = None
        self.__detalhes = None

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self
    
    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self
    
    def com_itens(self, itens):
        self.__itens = itens
        return self
    
    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self
    
    def constroi(self):
        if self.__razao_social is None:
            raise Exception("Razao social deve ser preenchida")
        if self.__cnpj is None:
            raise Exception("CNPJ deve ser preenchida")
        if self.__itens is None:
            raise Exception("Itens deve ser preenchida")
        if self.__data_de_emissao is None:
            self.__data_de_emissao = date.today()
        if self.__detalhes is None:
            self.__detalhes = ''

        return NotaFiscal(razao_social=self.__razao_social, 
                          cnpj=self.__cnpj, itens=self.__itens,
                          data_de_emissao=self.__data_de_emissao, detalhes=self.__detalhes)

if __name__ == "__main__":
    
    itens=[Item('ITEM A',100), Item('ITEM B',200)]

    nota_fiscal_com_builder = CriadorDeNotaFiscal().com_razao_social('FHSA Limitada')\
    .com_cnpj('012345678901234').com_itens(itens).com_data_de_emissao(date.today())  \
    .com_detalhes('').constroi()

    print(nota_fiscal_com_builder)


