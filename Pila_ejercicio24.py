class Pila():
    """Stack class"""

    def __init__(self):
        self.__elements = []

    def __eq__(self, stack_aux):
        if isinstance(stack_aux, Pila):
            return self.__elements == stack_aux.__elements
        else:
            return False

    def push(self, value):
        self.__elements.append(value)

    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato

    def size(self):
        return len(self.__elements)

    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]
        
class PersonajeMCU():
    def __init__(self, name, movie_amount):
        self.__name = name
        self.__movie_amount = movie_amount

    def __str__(self):
        return f'Personaje: {self.__name}. Cantidad de peliculas: {self.__movie_amount}'
    
    def get_name(self):
        return self.__name
    
    def get_movie_amount(self):
        return self.__movie_amount
    
pilaPersonajes = Pila()
personajes = [
    PersonajeMCU("Iron Man", 10 ),
    PersonajeMCU("Captain America", 9 ),
    PersonajeMCU("Groot", 5 ),
    PersonajeMCU("Spider-Man", 8 ),
    PersonajeMCU("Hulk", 7 ),
    PersonajeMCU("Black Widow", 7 ),
    PersonajeMCU("Doctor Strange", 4 ),
    PersonajeMCU("Black Panther", 4 ),
    PersonajeMCU("Scarlet Witch", 5 ),
    PersonajeMCU("Rocket Raccoon", 5 ),
]

for personaje in personajes:
    pilaPersonajes.push(personaje)

posicion = 1

while pilaPersonajes.size() > 0:
    personaje = pilaPersonajes.pop()
    if (not personaje):
        continue
    if (personaje.get_name() == 'Rocket Raccoon' or personaje.get_name() == 'Groot'):
        print(f'{personaje.get_name()}, posicion {posicion}')

    if (personaje.get_movie_amount() > 5):
        print(f'El personaje {personaje.get_name()} participo en mas de 5 peliculas, participo en {personaje.get_movie_amount()}')

    if (personaje.get_name() == 'Black Widow'):
        print(f'El personaje Black Widow aparecio en {personaje.get_movie_amount()} peliculas')

    if (personaje.get_name()[0] == 'C' or personaje.get_name()[0] == 'D' or personaje.get_name()[0] == 'G'):
        print(f'El personaje {personaje.get_name()} empieza con {personaje.get_name()[0]}')

    posicion = posicion + 1