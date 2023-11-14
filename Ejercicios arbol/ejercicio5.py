"""5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
los villanos, luego resolver las siguiente tareas:
I. determinar cuántos nodos tiene cada árbol;
II. realizar un barrido ordenado alfabéticamente de cada árbol."""

from arbol_binario import BinaryTree, NodeTree

    
lista_marvel =[
    {"nombre": "Loki", "heroe": False},
    {"nombre": "Thanos", "heroe": False},
    {"nombre": "Ultron", "heroe": False},
    {"nombre": "Iron Man", "heroe": True},
    {"nombre": "Captain America", "heroe": True},
    {"nombre": "Thor", "heroe": True},
    {"nombre": "Hulk", "heroe": True},
    {"nombre": "Black Widow", "heroe": True},
    {"nombre": "Hawkeye", "heroe": True},
    {"nombre": "Spider-Man", "heroe": True},
    {"nombre": "Doctor Strange", "heroe": True},
]
arbolHeroes = BinaryTree()
arbolVillanos = BinaryTree()
arbol = BinaryTree()

for heroe in lista_marvel:
    nombre = heroe['nombre']
    
    arbol.insert_node(nombre,heroe)
    if heroe.get("heroe"): 
        arbolHeroes.insert_node (nombre, heroe)
    else:
        arbolVillanos.insert_node (nombre,heroe)
#b. listar los villanos ordenados alfabéticamente;
def imprimirVillano (node: NodeTree): 
    if node.other_values is False:
        print (node.value)
arbol.inorden(imprimirVillano)

#c. mostrar todos los superhéroes que empiezan con C;
superheroes_con_c = [heroe['nombre'] for heroe in lista_marvel if heroe['heroe'] and heroe['nombre'].startswith("C")]
print('Superheroes que empiezan con C')
for heroe in superheroes_con_c: 
    print(heroe)

#d determinar cuántos superhéroes hay el árbol;
def cantidadHeroes(node: NodeTree, value):
    if node.other_values is value:
        return 1
    else:
        return 0
total = arbol.count(True,cantidadHeroes)
print ('Cantidad de superhéroes que hay en el árbol', (total))

#e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
def modificarDr():
    value = input ('Ingerse el nombre que quiere modificar ')
    pos = arbol.search(value)
    print(pos)
    if pos:
        es_heroe = pos.other_values
        arbol.delete_node(value)

        nuevo_nombre = input ('Ingere el nuevo nombre')
        arbol.insert_node(nuevo_nombre, es_heroe)

        arbol.inorden()
    else:
        print('El nombre ingresado no fue encontrado')
#modificarDr()

#f. listar los superhéroes ordenados de manera descendente;
print('Heroes ordenados de forma descendente')
def imprimirHeroe(node: NodeTree):
    print(node.other_values)
arbolHeroes.postorden(imprimirHeroe)

#g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas: I. determinar cuántos nodos tiene cada árbol; II. realizar un barrido ordenado alfabéticamente de cada árbol.

def countHeroes(node: NodeTree, value):
    if value in node.value:
        return 1
    else:
        return 0

print(arbolHeroes.count('', countHeroes))

def countVillanos(node: NodeTree, value):
    if value in node.value:
        return 1
    else:
        return 0

print(arbolVillanos.count('', countVillanos))