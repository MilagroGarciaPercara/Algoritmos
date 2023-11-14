class Pila():
    """Stack class"""

    def __init__(self):
        self.__elements = []

    """compara dos objetos de la clase y se fija si son iguales"""

    def __eq__(self, stack_aux):
        if isinstance(stack_aux, Pila):
            return self.__elements == stack_aux.__elements
        else:
            return False
    """agrega elementos a la pila"""

    def push(self, value):
        self.__elements.append(value)
    """si la pila no esta vacia, elimina y devuelve el último elemento de la pila"""

    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato
    """ devuelve el tamaño de la pila"""

    def size(self):
        return len(self.__elements)
    """si la cola no esta vacia, devuelve el ultimo elemento de la pila """

    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]
