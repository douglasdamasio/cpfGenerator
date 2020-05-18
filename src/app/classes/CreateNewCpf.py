from .ValidateCpfParams import ValidateCpfParams
from random import randrange


class CreateNewCpf:
    def __init__(self, listOfParams):
        self._params, self._type = ValidateCpfParams(listOfParams).\
            validadeFull()
        self.createCpf(self._params, self._type)

    def createCpf(self, listOfParams, typeFormat):
        if typeFormat is True:
            cpfFormat = []

            for n in range(0, 11):
                n = randrange(0, 9)
                cpfFormat.append(str(n))

            cpfFormat = ''.join(cpfFormat)

            cpf = f'{cpfFormat[0:3]}.{cpfFormat[3:6]}.{cpfFormat[6:9]}-{cpfFormat[9:]}'

            msg = 'CPF (Formatado):'

            self.showCpf(msg, cpf)

        elif typeFormat is False:
            cpfNotFormat = []
            for n in range(0, 11):
                n = randrange(0, 9)
                cpfNotFormat.append(str(n))

            cpf = ''.join(cpfNotFormat)

            msg = 'CPF (Somente números):'

            self.showCpf(msg, cpf)

    def showCpf(self, msg, cpf):
        print(msg, cpf)
