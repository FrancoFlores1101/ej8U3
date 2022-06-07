from personal import Personal

class Docente(Personal):
    __carrera = ""
    __cargo = ""
    __catedra = ""
    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
    def getCarrera(self):
        return self.__carrera
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra
    def getSueldo(self) :
        sueldo = super().getSueldo()
        if self.getCargo().lower() == "simple":
            sueldo += self.getSueldoBasico() * 0.1
        elif self.getCargo().lower() == "semiexclusivo":
            sueldo += self.getSueldoBasico() * 0.2
        elif self.getCargo().lower() == "exclusivo":
            sueldo += self.getSueldoBasico() * 0.5
        return sueldo
    def __str__(self):
        cadena = super().__str__()
        cadena += "Carrera: {0}\n".format(self.__carrera)
        cadena += "Cargo: {0}\n".format(self.__cargo)
        cadena += "Catedra: {0}\n".format(self.__catedra)
        return cadena
    def getTipo(self) -> str:
        return "Docente"
