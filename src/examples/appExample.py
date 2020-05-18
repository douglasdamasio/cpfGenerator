import sys
from random import randrange


class ValidateCpfParams:
    def __init__(self, listOfParams):
        self._lt = listOfParams

    def validateSize(self):
        if len(self._lt) > 3:
            print('Você só pode passar 2 argumentos no máximo')
            exit()

        if len(self._lt) < 2:
            print('Você deve passar no minimo 1 argumento')
            exit()

        if len(self._lt) >= 2:
            return True

    def validateParams(self):
        if len(self._lt) == 3 and self._lt[1] == '-cpf':
            return True

        elif len(self._lt) < 3:
            if self._lt[1] == '-cpf':
                return False

            else:
                print('Parametros principal inválido')
                exit()

    def validateType(self):
        if self.validateParams() is True:
            if self._lt[-1] == '-f' or self._lt[-1] == '--format':
                return self._lt, True
            else:
                print(
                    'Parametro de formatação opcional deve ser -f ou --format'
                )
                exit()
        else:
            return self._lt, False

    def validadeFull(self):
        self.validateSize()
        self.validateParams()
        return self.validateType()


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


def main():
    listOfParams = []
    for param in sys.argv:
        listOfParams.append(param)

    CreateNewCpf(listOfParams)


main()
