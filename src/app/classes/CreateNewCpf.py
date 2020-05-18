from .ValidateCpfParams import ValidateCpfParams
from random import randrange


class CreateNewCpf:
    def __init__(self, listOfParams):
        self._type = ValidateCpfParams(listOfParams).validadeFull()
        self._cpf = self.createCpf()
        self.format(self._cpf, self._type)

    def createCpf(self):
        cpf = list(map(lambda digit: randrange(0, 9), range(0, 9)))

        cpf = self.calculateDigit(cpf)

        cpf = list(map(lambda a: str(a), cpf))

        return cpf

    def calculateDigit(self, cpf):
        multiplier = 10 if len(cpf) == 9 else 11

        if len(cpf) <= 10:
            calc = []
            for digit in cpf:
                calc.append(digit * multiplier)
                multiplier -= 1
            
            r = sum(calc) % 11

            cpf.append(0) if r == 1 or r == 0 else cpf.append(11 - r)

            return self.calculateDigit(cpf)
        else:
            return cpf

    def format(self, cpf, type):
        if type is True:
            cpf = ''.join(cpf)
            
            cpf = f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
            msg = 'CPF (formatado):'
            
            self.showCpf(msg, cpf)

        else:
            cpf = ''.join(cpf)

            msg = 'CPF (Somente números):'
            
            self.showCpf(msg, cpf)

    def showCpf(self, msg, cpf):
        print(msg, cpf)
