from zope.interface import Interface

class IDirector(Interface):

    def modificarBasico(self,, nuevoBasico):

        pass


    def modificarCargo(self,cuil, nuevoCargo):
        pass


    def modificarCategoria(self,cuil, nuevaCategoria):

        pass

    def modificarImporteExtra(self, cuil, nuevoImporteExtra:):

        pass
