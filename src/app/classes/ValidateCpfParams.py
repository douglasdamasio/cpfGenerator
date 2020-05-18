
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
                return True
            else:
                print(
                    'Parametro de formatação opcional deve ser -f ou --format'
                )
                exit()
        else:
            return False

    def validadeFull(self):
        self.validateSize()
        self.validateParams()
        return self.validateType()
