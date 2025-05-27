# Esta es la interfaz base para todos los objetos que pueden ser "visitados"
import abc

class Visitable(metaclass=abc.ABCMeta):
    """
    Clase abstracta que define el contrato para los objetos que pueden ser visitados.
    Cualquier clase que quiera ser visitable debe implementar el método aceptar.
    """
    @abc.abstractmethod
    def aceptar(self, visitante):
        """
        Método que acepta un visitante y le permite realizar operaciones sobre el objeto.
        Cada clase concreta implementará este método para llamar al método específico del visitante.
        """
        pass
