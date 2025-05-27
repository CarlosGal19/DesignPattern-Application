# Visitante concreto que equipa encantamientos a los magos
from Visitante import Visitante

class EquiparEncantamiento(Visitante):
    """
    Implementación concreta de un visitante que equipa encantamientos
    solo a los magos, basándose en su nivel mágico
    """
    def visitar_mago(self, mago):
        """Equipa un encantamiento según el nivel mágico del mago"""
        if mago.get_tipo() == 'Fuego':
            mago.set_encantamiento('Bola de fuego')  # Encantamiento básico
        else:
            mago.set_encantamiento('Rayo de hielo')  # Encantamiento avanzado

    def visitar_guerrero(self, guerrero):
        """Los guerreros no reciben encantamientos"""
        pass

    def visitar_personajes(self, personajes):
        """Visita cada personaje para equipar encantamientos si corresponde"""
        for personaje in personajes:
            personaje.aceptar(self)
