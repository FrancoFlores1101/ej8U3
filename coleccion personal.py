from DocenteInvestigador import DocenteInvestigador
from Investigador import Investigador
from Personal import Personal
from zope.interface import implementer
from IColeccion import IColeccion
from Nodo import Nodo

class ColeccionPersonal:
    __comienzo = None
    __actual = None
    __tope = 0


    def __init__(self) :
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0

    def insertarElemento(self, unaPersona, pos):
        if not isinstance(pos, int) or pos < 0:
            raise IndexError("Indice invalido")
        unNodo = Nodo(unaPersona)
        if pos == 0:
            unNodo.setSiguiente(self.__comienzo)
            self.__comienzo = unNodo
            self.__actual = self.__comienzo
        else:
            i = 1
            aux = self.__comienzo
            while i < pos and aux.getSiguiente() != None:
                i += 1
                aux = aux.getSiguiente()
            if i == pos:
                unNodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(unNodo)
            else:
                raise IndexError("Indice fuera de rango")
        self.__tope += 1

    def agregarElemento(self, unaPersona: Personal):
        unNodo = Nodo(unaPersona)
        if self.__comienzo == None:
            self.__comienzo = unNodo
            self.__actual = self.__comienzo
        else:
            aux = self.__comienzo
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(unNodo)

        self.__tope += 1

    def mostrarElemento(self, pos: int):
        if pos < 0 or self.__comienzo == None:
            raise IndexError("Indice invalido")
        else:
            i = 0
            aux = self.__comienzo
            while i < pos and aux.getSiguiente() != None:
                aux = aux.getSiguiente()
                i += 1
            if i == pos:
                unaPersona = aux.getPersona()
                print(unaPersona)
            else:
                raise IndexError("Indice fuera de rango")
        if self.__actual == None:
            self.__actual = self.__comienzo
            raise StopIteration
        else:
            unaPersona = self.__actual.getPersona()
            self.__actual = self.__actual.getSiguiente()
            return unaPersona
    def ordenarPersonal(self, metodoComparacion):
        if self.__comienzo != None:
            k = None
            cota = None
            while k != self.__comienzo:
                k = self.__comienzo
                unNodo = self.__comienzo
                while unNodo.getSiguiente() != cota:
                    if metodoComparacion(unNodo.getSiguiente().getPersona()) < metodoComparacion(unNodo.getPersona()):
                        unaPersona = unNodo.getPersona()
                        unNodo.setPersona(unNodo.getSiguiente().getPersona())
                        unNodo.getSiguiente().setPersona(unaPersona)
                        k = unNodo
                    unNodo = unNodo.getSiguiente()
                cota = k.getSiguiente()
    def getListadoAgentesInvestigadores(self, nombreCarrera):
        self.ordenarPersonal(lambda unaPersona: unaPersona.getNombre())
        cadena = "{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}\n".format("Cuil", "Apellido", "Nombre", "Categoria incentivos", "Importe extra")
        for unaPersona in self:
            if isinstance(unaPersona, DocenteInvestigador) and unaPersona.getCarrera().lower() == nombreCarrera.lower():
                cadena += "{0:<20}{1:<20}{2:<20}{3:<20}{4:<20.2f}\n".format(unaPersona.getCuil(), unaPersona.getApellido(), unaPersona.getNombre(), unaPersona.getCategoriaIncentivos(), unaPersona.getImporteExtra())
        return cadena
    def contarDocentesInvestigadores(self, nombreAreaInvestigacion) :
        contadorDocentesInvestigadores = 0
        contadorInvestigadores = 0
        for unaPersona in self:
            if isinstance(unaPersona, DocenteInvestigador) and unaPersona.getAreaInvestigacion().lower() == nombreAreaInvestigacion.lower():
                contadorDocentesInvestigadores += 1
            elif isinstance(unaPersona, Investigador) and unaPersona.getAreaInvestigacion().lower() == nombreAreaInvestigacion.lower():
                contadorInvestigadores += 1
        return (contadorDocentesInvestigadores, contadorInvestigadores)
    def getListadoPersonal(self):
        self.ordenarPersonal(lambda unaPersona: unaPersona.getApellido())
        cadena = "{0:<20}{1:<20}{2:<25}{3:<20}\n".format("Nombre", "Apellido", "Tipo de agente", "Sueldo")
        for unaPersona in self:
            cadena += "{0:<20}{1:<20}{2:<25}{3:<20}\n".format(unaPersona.getNombre(), unaPersona.getApellido(), unaPersona.getTipo(), unaPersona.getSueldo())
        return cadena
    def getListadoDocentesInvestigadores(self, categoria):
        cadena = "{0:<23}{1:<23}{2:>20}\n".format("Nombre", "Apellido", "Importe extra")
        total = 0
        for unaPersona in self:
            if isinstance(unaPersona, DocenteInvestigador) and unaPersona.getCategoriaIncentivos().lower() == categoria.lower():
                cadena += "{0:<23}{1:<23}{2:20.2f}\n".format(unaPersona.getNombre(), unaPersona.getApellido(), unaPersona.getImporteExtra())
                total += unaPersona.getImporteExtra()
        cadena += "{0:46}{1:20.2f}\n".format("Importe total en concepto de incentivos: ".upper(), total)
        return cadena
