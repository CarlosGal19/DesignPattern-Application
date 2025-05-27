# Esta es la interfaz base para todos los "visitantes" que pueden realizar operaciones
import abc

class Visitante(metaclass=abc.ABCMeta):
    """
    Clase abstracta que define el contrato para los visitantes.
    Cada visitante debe implementar métodos específicos para cada tipo de objeto visitable.
    """
    @abc.abstractmethod
    def visitar_mago(self, mago):
        """Método para realizar operaciones específicas en un mago"""
        pass

    @abc.abstractmethod
    def visitar_guerrero(self, guerrero):
        """Método para realizar operaciones específicas en un guerrero"""
        pass

    @abc.abstractmethod
    def visitar_personajes(self, personajes):
        """Método para visitar una colección de personajes"""
        pass
