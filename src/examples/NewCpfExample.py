from .ValidateCpfParams import ValidateCpfParams
from random import randrange


class CreateNewCpf:
    def __init__(self, listOfParams):
        self._params, self._type = ValidateCpfParams(listOfParams).\
            validadeFull()
        self.createCpf(self._params, self._type)

    def createCpf(self, listOfParams, typeFormat):
        randomNumbers = []
        calcJ = []
        calcK = []
        multiplierJ = 10
        multiplierK = 11

        for digit in range(0, 9):
            randomNumbers.append(randrange(0, 9))
        
        for digit in randomNumbers:
            calcJ.append(digit * multiplierJ)
            multiplierJ -= 1

        result = sum(calcJ) % 11

        if result == 1 or result == 0:
            randomNumbers.append(0)
        else:
            randomNumbers.append(11 - result)

        for digit in randomNumbers:
            calcK.append(digit * multiplierK)
            multiplierK -= 1
        
        result = sum(calcK) % 11

        if result == 1 or result == 0:
            randomNumbers.append(0)
        else:
            randomNumbers.append(11 - result)

        cpf = list(map(lambda a: str(a), randomNumbers))
        cpf = ''.join(cpf)

        print(cpf)

    def showCpf(self, msg, cpf):
        print(msg, cpf)
