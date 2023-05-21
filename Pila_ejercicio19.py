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
        
class Pelicula():
    def __init__(self, title, film_studio, year):
        self.__title = title
        self.__film_studio = film_studio
        self.__year = year
    
    def get_title(self):
        return self.__title

    def get_film_studio(self):
        return self.__film_studio

    def get_year(self):
        return self.__year
    
    def __str__(self):
        return f'{self.__title} - {self.__film_studio} - {self.__year}'
    
pilaPeliculas = Pila()
pelis = [
    Pelicula("Titanic", "20th Century Fox", 1997),
    Pelicula("Black Panther", "Marvel Studios", 2018),
    Pelicula("Avengers: Endgame", "Marvel Studios", 2019),
    Pelicula("El Señor de los Anillos: El retorno del rey", "New Line Cinema", 2003),
    Pelicula("La La Land", "Summit Entertainment", 2016),
    Pelicula("Guardianes de la Galaxia", "Marvel Studios", 2014),
    Pelicula("Avatar", "20th Century Fox", 2009),
    Pelicula("Harry Potter y la piedra filosofal", "Warner Bros. Pictures", 2001),
    Pelicula("El caballero oscuro", "Warner Bros. Pictures", 2008),
    Pelicula("Bohemian Rhapsody", "20th Century Fox", 2018),
    Pelicula("Forrest Gump", "Paramount Pictures", 1994),
    Pelicula("El Rey León", "Walt Disney Pictures", 1994),
    Pelicula("Pulp Fiction", "Miramax Films", 1994),
    Pelicula("Captain America: Civil War", "Marvel Studios", 2016),
    Pelicula("El gran Gatsby", "Warner Bros. Pictures", 2013),
    Pelicula("Toy Story", "Pixar Animation Studios", 1995),
    Pelicula("Avengers: Infinity War", "Marvel Studios", 2018),
    Pelicula("El silencio de los corderos", "Orion Pictures", 1991),
    Pelicula("Doctor Strange", "Marvel Studios", 2016),
    Pelicula("Interstellar", "Paramount Pictures", 2014),
]

for peli in pelis:
    pilaPeliculas.push(peli)

contador_peliculas_de_2018 = 0

while pilaPeliculas.size() > 0:
    peli = pilaPeliculas.pop()
    if (not peli):
        continue
    if (peli.get_year() == 2014):
        print(f'La pelicula {peli.get_title()} se estreno en 2014')
    if (peli.get_year() == 2018):
        contador_peliculas_de_2018 = contador_peliculas_de_2018 + 1
    if (peli.get_year() == 2016 and peli.get_film_studio() == 'Marvel Studios'):
        print(f'Pelicula de Marvel Studios estrenada en 2016: {peli.get_title()}')
    

print(f'Se estrenaron {contador_peliculas_de_2018} peliculas en 2018')