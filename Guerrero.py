# Clase concreta que representa un personaje tipo Guerrero
from Visitable import Visitable

class Guerrero(Visitable):
    """
    Clase que representa a un Guerrero en el juego.
    Implementa la interfaz Visitable para poder recibir visitantes.
    """
    def __init__(self):
        """Inicializa un guerrero sin arma"""
        self.__arma = ''

    def get_arma(self):
        """Retorna el arma actual del guerrero"""
        return self.__arma

    def set_arma(self, arma):
        """Establece el arma del guerrero"""
        self.__arma = arma

    def aceptar(self, visitante):
        """
        Implementación del método aceptar de la interfaz Visitable.
        Llama al método específico del visitante para guerreros.
        """
        visitante.visitar_guerrero(self)
