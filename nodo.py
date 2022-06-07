from Personal import Personal

class Nodo:
    __persona = None
    __siguiente = None

    def __init__(self, unaPersona):
        self.__persona = unaPersona
        self.__siguiente = None
    def getPersona(self)
        return self.__persona
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    def getSiguiente(self):
        return self.__siguiente
    def setPersona(self, unaPersona):
        self.__persona = unaPersona
