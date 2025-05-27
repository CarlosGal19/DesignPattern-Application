"""
    Pequeño videojuego de rol con el patrón Visitor y abstract factory.
    Este juego permite crear personajes de tipo Guerrero y Mago, equiparles armas
    y encantamientos, y mostrar su información.
"""

# Importamos las clases necesarias para nuestro juego
from Fabricas import FabricaPersonajes
from EquiparArma import EquiparArma
from EquiparEncantamiento import EquiparEncantamiento

def main():
    # Creamos las fábricas
    fabrica_guerreros = FabricaPersonajes.create_fabrica("Guerrero")
    fabrica_magos = FabricaPersonajes.create_fabrica("Mago")

    # Creamos instancias de nuestros personajes
    g1 = fabrica_guerreros.crear_personaje()
    g2 = fabrica_guerreros.crear_personaje()
    m1 = fabrica_magos.crear_personaje("Fuego")
    m2 = fabrica_magos.crear_personaje("Hielo")

    # Configuramos los niveles mágicos de los magos
    m1.set_nivel_magico(3)  # Mago de fuego con nivel bajo
    m2.set_nivel_magico(7)  # Mago de hielo con nivel alto

    # Creamos la lista de personajes
    personajes = []
    personajes.extend([g1, g2, m1, m2])

    # Creamos y aplicamos el visitante para equipar armas
    ea = EquiparArma()
    ea.visitar_personajes(personajes)

    ee = EquiparEncantamiento()
    ee.visitar_personajes(personajes)

    mostrar_info(personajes)

def mostrar_info(personajes):
    """
    Función que muestra la información de cada personaje.
    Para todos los personajes muestra su arma.
    Para los magos además muestra su encantamiento y nivel mágico.
    """
    for personaje in personajes:
        print("\nInformación del personaje:")
        # Mostramos el arma que tiene equipada (todos los personajes tienen arma)
        print(f'Arma: {personaje.get_arma()}')

        # Verificamos si el personaje tiene atributos de mago
        if hasattr(personaje, 'get_encantamiento'):
            print(f'Tipo: Mago de {personaje.get_tipo()}')
            print(f'Encantamiento: {personaje.get_encantamiento()}')
            print(f'Nivel Magico: {personaje.get_nivel_magico()}')
        else:
            print('Tipo: Guerrero')

if __name__ == '__main__':
    main()
