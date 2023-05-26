class Cola():

    def __init__(self):
        self.__elementos = []

    def arrive(self, value):
        self.__elementos.append(value)

    def atention(self):
        if self.size() > 0:
            return self.__elementos.pop(0)

    def size(self):
        return len(self.__elementos)

    def on_front(self):
        if self.size() > 0:
            return self.__elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux


class PersonajesMCU():
    def __init__(self, namepj, namesup, gender):
        self.__namepj = namepj
        self.__namesup = namesup
        self.__gender = gender

    def get_namepj(self):
        return self.__namepj

    def get_namesup(self):
        return self.__namesup

    def get_gender(self):
        return self.__gender

    def __str__(self):
        return f'{self.__namepj} - {self.__namesup} - {self.__gender}'


colaPersonajesMCU = Cola()
personajes = [
    PersonajesMCU("Bruce Banner", "Hulk", "M"),
    PersonajesMCU("Carol Danvers", "Capitana Marvel", "F"),
    PersonajesMCU("Clint Barton", "Hawkeye", "M"),
    PersonajesMCU("Peter Parker", "Spider-Man", "M"),
    PersonajesMCU("T'Challa", "Black Panther", "M"),
    PersonajesMCU("Stephen Strange", "Doctor Strange", "M"),
    PersonajesMCU("Peter Quill", "Star-Lord", "M"),
    PersonajesMCU("Gamora", "Gamora", "F"),
    PersonajesMCU("Scott Lang", "Ant-Man", "M"),
    PersonajesMCU("Tony Stark", "Iron Man", "M"),
]
for pj in personajes:
    colaPersonajesMCU.arrive(pj)

contador_pjconS = 0

while colaPersonajesMCU.size() > 0:
    pj = colaPersonajesMCU.atention()
    if (not pj):
        continue

    if (pj.get_namesup() == "Capitana Marvel"):
        print(
            f'El nombre del personaje de la superhéroe Capitana Marvel es {pj.get_namepj()}')

    if (pj.get_gender() == "F"):
        print(f'La superhéroe {pj.get_namesup()} es femenino')

    if (pj.get_gender() == "M"):
        print(f'El personaje {pj.get_namepj()} es masculino')

    if (pj.get_namepj() == "Scott Lang"):
        print(f'El nombre del superhéroe de Scott Lang es {pj.get_namesup()}')

    if (pj.get_namepj()[0] == "S" or pj.get_namesup()[0] == "S"):
        print(f'Este personaje o superhéroe empieza con S: {pj}')

    if (pj.get_namepj() == "Carol Danvers"):
        print(
            f'El nombre de la superhéroe Carol Danvers es {pj.get_namesup()}')
