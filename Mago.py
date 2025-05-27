# Clase concreta que representa un personaje tipo Mago
from Visitable import Visitable

class MagoHielo(Visitable):
    """
    Clase que representa a un Mago en el juego.
    Implementa la interfaz Visitable y tiene propiedades adicionales como encantamiento y nivel mágico.
    """
    def __init__(self):
        """Inicializa un mago con valores por defecto"""
        self.__arma = ''
        self.__encantamiento = ''
        self.__nivel_magico = 1
        self.__tipo = 'Hielo'

    def get_arma(self):
        """Retorna el arma actual del mago"""
        return self.__arma

    def set_arma(self, arma):
        """Establece el arma del mago"""
        self.__arma = arma

    def get_encantamiento(self):
        """Retorna el encantamiento actual del mago"""
        return self.__encantamiento

    def set_encantamiento(self, encantamiento):
        """Establece el encantamiento del mago"""
        self.__encantamiento = encantamiento

    def get_nivel_magico(self):
        """Retorna el nivel mágico actual del mago"""
        return self.__nivel_magico

    def set_nivel_magico(self, nivel_magico):
        """Establece el nivel mágico del mago"""
        self.__nivel_magico = nivel_magico

    def aceptar(self, visitante):
        """
        Implementación del método aceptar de la interfaz Visitable.
        Llama al método específico del visitante para magos.
        """
        visitante.visitar_mago(self)

    def get_tipo(self):
        """Retorna el arma actual del mago"""
        return self.__tipo

class MagoFuego(Visitable):
    """
    Clase que representa a un Mago en el juego.
    Implementa la interfaz Visitable y tiene propiedades adicionales como encantamiento y nivel mágico.
    """
    def __init__(self):
        """Inicializa un mago con valores por defecto"""
        self.__arma = ''
        self.__encantamiento = ''
        self.__nivel_magico = 1
        self.__tipo = 'Fuego'

    def get_arma(self):
        """Retorna el arma actual del mago"""
        return self.__arma

    def set_arma(self, arma):
        """Establece el arma del mago"""
        self.__arma = arma

    def get_encantamiento(self):
        """Retorna el encantamiento actual del mago"""
        return self.__encantamiento

    def set_encantamiento(self, encantamiento):
        """Establece el encantamiento del mago"""
        self.__encantamiento = encantamiento

    def get_nivel_magico(self):
        """Retorna el nivel mágico actual del mago"""
        return self.__nivel_magico

    def set_nivel_magico(self, nivel_magico):
        """Establece el nivel mágico del mago"""
        self.__nivel_magico = nivel_magico

    def aceptar(self, visitante):
        """
        Implementación del método aceptar de la interfaz Visitable.
        Llama al método específico del visitante para magos.
        """
        visitante.visitar_mago(self)

    def get_tipo(self):
        """Retorna el arma actual del mago"""
        return self.__tipo
