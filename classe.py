class conta_banco:
    def __init__(self,titular, numero_conta) -> None:
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = 0

        print("\nConta criada com sucesso!")
        print("=========================")
        print(f"Titular da conta: {self.titular}")
        print(f"Número da conta: {self.numero_conta}")
        print(f"saldo inicial: {self.saldo}\n")
    
    def creditar(self, dinheiro_creditado):

            print("\n=======DADOS DA CONTA========")
            print(f"titular: {self.titular}")
            print(f"numero da conta: {self.numero_conta}")
            print(f"saldo anterior: {self.saldo}")
            print("=============================")

            self.saldo += dinheiro_creditado
            print(f"dinheiro creditado na conta com sucesso!")
            print(f"novo saldo: {self.saldo}\n")
    
    def debitar(self, dinheiro_debitado):
        if(dinheiro_debitado <= self.saldo):
            
            print("\n=======DADOS DA CONTA========")
            print(f"titular: {self.titular}")
            print(f"numero da conta: {self.numero_conta}")
            print(f"saldo anterior: {self.saldo}")
            print("=============================")
            self.saldo -= dinheiro_debitado
            print("Dinheiro debitado com sucesso!")
            print(f"novo saldo: {self.saldo}\n")
        else:
            print("\nSaldo Insuficiente!\n")
            print(f"Saldo disponível: {self.saldo}")
            print(f"a tentativa de saque foi de: {dinheiro_debitado}")
    
    
                

conta1 = conta_banco("bruna", "457834758")
conta1.creditar(1000)
conta1.debitar(1001)

conta2 = conta_banco("neto", "734873249")
conta2.creditar(700)
conta2.debitar(600)

conta3 = conta_banco("samuel", "08878563")
conta3.creditar(20000)
conta3.debitar(1000)





