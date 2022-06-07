from abc import ABC
import abc
class Personal(ABC):
    __cuil = ""
    __apellido = ""
    __nombre = ""
    __sueldoBasico = 0
    __antiguedad = 0

    def __init__(self,cuil, apellido, nombre, sueldoBasico, antiguedad):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoBasico = sueldoBasico
        self.__antiguedad = antiguedad


    def getCuil(self):
        return self.__cuil

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getSueldoBasico(self):
        return self.__sueldoBasico

    def getAntiguedad(self) -> int:
        return self.__antiguedad

    @abc.abstractmethod
    def getSueldo(self):
        sueldo = self.getSueldoBasico() + self.getSueldoBasico() * 0.01 * self.getAntiguedad()
        return sueldo



    @abc.abstractmethod
    def __str__(self):
        cadena = "Tipo de agente: {0}\n".format(self.getTipo())
        cadena += "Cuil: {0}\n".format(self.getCuil())
        cadena += "Apellido: {0}\n".format(self.getApellido())
        cadena += "Nombre {0}\n".format(self.getNombre())
        cadena += "Sueldo basico: {0:.2f}\n".format(self.getSueldoBasico())
        cadena += "Antiguedad: {0}\n".format(self.getAntiguedad())
        return cadena

