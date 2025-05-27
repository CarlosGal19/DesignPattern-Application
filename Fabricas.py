from Guerrero import Guerrero
from Mago import MagoFuego, MagoHielo

class FabricaPersonajes:
    @staticmethod
    def create_fabrica(tipo_personaje: str):
        if tipo_personaje is None:
            raise ValueError("Tipo de personaje is required")
        if tipo_personaje == "Guerrero":
            return FabricaGuerreros()
        if tipo_personaje == "Mago":
            return FabricaMagos()
        raise ValueError("Invalid Tipo de personaje")

class FabricaGuerreros:
    @staticmethod
    def crear_personaje():
        return Guerrero()

class FabricaMagos:
    def crear_personaje(self, tipo_mago: str = "Fuego"):
        if tipo_mago == "Hielo":
            return MagoHielo()
        return MagoFuego()


