# Visitante concreto que equipa armas a los personajes
from Visitante import Visitante

class EquiparArma(Visitante):
    """
    Implementación concreta de un visitante que equipa armas específicas
    según el tipo de personaje
    """
    def visitar_mago(self, mago):
        """Equipa una daga al mago"""
        mago.set_arma('Daga')

    def visitar_guerrero(self, guerrero):
        """Equipa una espada al guerrero"""
        guerrero.set_arma('Espada')

    def visitar_personajes(self, personajes):
        """Visita cada personaje en la colección para equiparle su arma"""
        for personaje in personajes:
            personaje.aceptar(self)
