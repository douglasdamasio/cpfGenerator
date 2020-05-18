from classes.CreateNewCpf import CreateNewCpf
from sys import argv


def runApp():
    listOfParams = []
    for param in argv:
        listOfParams.append(param)

    CreateNewCpf(listOfParams)


if __name__ == "__main__":
    runApp()
