from Personal import Personal

class PersonalApoyo(Personal):
    __categoria = ""
    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__categoria = categoria

    def getCategoria(self):
        return self.__categoria

    def getSueldo(self) :
        sueldo = super().getSueldo()
        if 1 <= self.getCategoria() <= 10:
            sueldo += self.getSueldoBasico() * 0.1
        elif 11 <= self.getCategoria() <= 20:
            sueldo += self.getSueldoBasico() * 0.2
        elif 21 <= self.getCategoria() <= 22:
            sueldo += self.getSueldoBasico() * 0.3
        return sueldo


    def __str__(self):
        cadena = super().__str__()
        cadena += "Categoria: {0}\n".format(self.__categoria)
        return cadena

    def getTipo(self) -> str:
        return "Personal de apoyo
