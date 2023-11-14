"""Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de nacimiento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos
tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
siguientes consignas:
a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
b. realizar un barrido inorden del árbol por nombre y ranking;
c. realizar un barrido por nivel de los árboles por ranking y especie;
d. mostrar toda la información de Yoda y Luke Skywalker;
e. mostrar todos los Jedi con ranking “Jedi Master”;
f. listar todos los Jedi que utilizaron sabe de luz color verde;
g. listar todos los Jedi cuyos maestros están en el archivo;
h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre."""

from arbol_binario import BinaryTree, NodeTree, get_value_from_file
arbolnombre = BinaryTree ()
arbolespecie = BinaryTree ()
arbolranking= BinaryTree () 

archivo = 'jedis.txt'
filas = open(archivo).readlines()

for index, linea in enumerate(filas):
    datos = linea.split(";")

    jedi = {
        "nombre": datos[0],
        "ranking": datos[1],
        "especie": datos[2],
        "maestro": datos[3],
        "color_sable": datos[4],
        "anio": datos[6],
    }
#a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
    arbolnombre.insert_node(jedi.get("nombre"), jedi)
    arbolespecie.insert_node(jedi.get("especie"), jedi)
    arbolranking.insert_node(jedi.get("ranking"), jedi)
#b realizar un barrido inorden del árbol por nombre y ranking;
#arbolnombre.inorden()
#arbolranking.inorden()

#c. realizar un barrido por nivel de los árboles por ranking y especie;
#arbolespecie.inorden()
#arbolranking.inorden()

#d mostrar toda la información de Yoda y Luke Skywalker;

print('Nombres buscados')
print(arbolnombre.search('yoda').other_values)
print(arbolnombre.search('luke skywalker').other_values)

#e. mostrar todos los Jedi con ranking “Jedi Master”;
print('Jedis con ranking "Jedi Master"')
print(arbolranking.search('jedi master').other_values)

#f. listar todos los Jedi que utilizaron sabe de luz color verde;

print('Jedis que utilizaron sablede luz color verde')
def jedis_sableverde(node: NodeTree):
    if node.other_values.get('color_sable') == "green":
        print(node.other_values.get('nombre')) 

arbolnombre.inorden(jedis_sableverde)

#h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;

print('Jedis de especie "Togruta" o "Cerean" ')
def jedis_especie(node: NodeTree):
    if node.other_values.get('especie') == "togruta" or node.other_values.get('especie') == "cerean":
        print(node.other_values.get('nombre')) 

arbolnombre.inorden(jedis_especie)

#i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.
print('Jedis que comienzan con la letra A o contienn un -')
def jedis_buscados(node: NodeTree):
    nombre: str = node.other_values.get('nombre')
    if nombre.lower().startswith("a") or nombre.find("-") != -1:
        print(node.other_values.get('nombre')) 

arbolnombre.inorden(jedis_buscados)
