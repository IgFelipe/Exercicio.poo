class Pagamento:
    def processar_pagamento(self):
        pass   

class PagamentoCartaoCredito(Pagamento):
    def __init__(self, numero_cartao):
        self.numero_cartao = numero_cartao

    def processar_pagamento(self):
        print(f"Pagamento com cartão de crédito: {self.numero_cartao}")

class PagamentoBoleto(Pagamento):
    def __init__(self, codigo_boleto):
        self.codigo_boleto = codigo_boleto

    def processar_pagamento(self):
        print(f"Pagamento com boleto: {self.codigo_boleto}")

class PagamentoPix(Pagamento):
    def __init__(self, chave_pix):
        self.chave_pix = chave_pix

    def processar_pagamento(self):
        print(f"Pagamento via Pix: {self.chave_pix}")

def processar(pagamento):
    pagamento.processar_pagamento()

pagamento_cartao = PagamentoCartaoCredito("1234-5678-9012-3456")
pagamento_boleto = PagamentoBoleto("BOLETO123456")
pagamento_pix = PagamentoPix("chave.pix@exemplo.com")

processar(pagamento_cartao)
processar(pagamento_boleto)
processar(pagamento_pix)
