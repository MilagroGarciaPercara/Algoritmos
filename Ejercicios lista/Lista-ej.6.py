"""Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:
a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic."""

from Lista import Lista
heroesLista = Lista()

class Heroe():
    def __init__(self, nombre, anio, casa_comic, biografia):
        self.nombre = nombre
        self.anio = anio
        self.casa_comic = casa_comic
        self.biografia = biografia

    def get_nombre(self):
        return self.nombre

    def get_casa(self):
        return self.casa_comic

    def get_anio(self):
        return self.anio
    
    def get_biografia(self):
        return self.biografia

    def __str__(
        self): return f'{self.nombre}-{self.anio}-{self.casa_comic}-{self.biografia}'
    
listaSuperheroes = Lista()

superheroes = [
{"nombre": "Linterna Verde", "anio_aparicion": 1940, "casa_comic": "DC", "biografia": "Linterna Verde es el nombre de varios superhéroes de DC Comics. Cada uno posee un anillo de poder que le otorga habilidades sobrehumanas."},
{"nombre": "Wolverine", "anio_aparicion": 1974, "casa_comic": "Marvel", "biografia": "Wolverine es un mutante de Marvel Comics conocido por sus habilidades regenerativas, garras retráctiles y su participación en los X-Men."},
{"nombre": "Dr Strange", "anio_aparicion": 1963, "casa_comic": "Marvel", "biografia": "Doctor Strange es un hechicero y el Hechicero Supremo del Universo Marvel. Utiliza la magia para proteger la realidad de amenazas místicas."},
{"nombre": "Capitana Marvel", "anio_aparicion": 1967, "casa_comic": "Marvel", "biografia": "Capitana Marvel es el nombre de varios personajes de Marvel Comics, siendo Carol Danvers la más conocida. Tiene poderes cósmicos y es miembro de los Vengadores."},
{"nombre": "Mujer Maravilla", "anio_aparicion": 1941, "casa_comic": "DC", "biografia": "Mujer Maravilla es una princesa guerrera de las Amazonas en DC Comics. Es una de las principales superheroínas y miembro de la Liga de la Justicia."},
{"nombre": "Flash", "anio_aparicion": 1940, "casa_comic": "DC", "biografia": "Flash es el nombre de varios superhéroes de DC Comics con velocidad sobrehumana. Barry Allen es uno de los más conocidos y miembro de la Liga de la Justicia."},
{"nombre": "Star Lord", "anio_aparicion": 1976, "casa_comic": "Marvel", "biografia": "Star-Lord, también conocido como Peter Quill, es un personaje de Marvel Comics y líder de los Guardianes de la Galaxia. Es conocido por su habilidad con las armas y su astucia."},
]
    
for data in superheroes:
    heroe = Heroe(data["nombre"], data['anio_aparicion'], data["casa_comic"], data["biografia"])
    heroesLista.insert(heroe, "nombre")

#a. eliminar el nodo que contiene la información de Linterna Verde;
heroesLista.delete("Linterna Verde", "nombre")

#b. mostrar el año de aparición de Wolverine;





#c. cambiar la casa de Dr. Strange a Marvel;

#d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;


#e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;


#f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;


#g. mostrar toda la información de Flash y Star-Lord;


#h. listar los superhéroes que comienzan con la letra B, M y S;


#i. determinar cuántos superhéroes hay de cada casa de comic.