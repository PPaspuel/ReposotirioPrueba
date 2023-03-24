
# Listas
dias= ['lunes','martes','miercoles','jueves','viernes',6,7] # En una lista si se pueden mezclara los tipos de datos en un vector no.
numeros = [10,20,30,40,50]

# Recorrer lista, imprime una valor deseado.
print(dias[2])
# Asignar un nuevo valor a la lista.
#numeros[0] = 111 # Reemplaza este valor en cero.
#print(numeros)
# Longitud de la lista.
print(len(numeros))
print(len(dias))
# Eliminar datos de lista.
del dias[5]
del dias[5] # Borro el numero 6.
dias.append('sabado')  # Agrega datos al final de la lista.
dias.append('domingo')
print(dias)
print(len(dias)) # Reduce en una pocicon el tamano de la lista.

# Usamos insertar.
print(len(numeros)) # Longitus de lista al principio
numeros.insert(1,15) # Primero es la ubicacion luego valor.
numeros.insert(3,25)
numeros.insert(5,35)
numeros.insert(7,45)
del numeros[4]
print(numeros)
print(len(numeros)) # Longitud de lista ala final.

# Rodajas en listas.
numeros2 = numeros[2:6] # Empieze primero y despues termine
print(numeros2)
print(dias)
diasFeriado = dias[1::4] # Estas son sublistas, aplicamos salto al final.
print(diasFeriado)

# Preguntar si esta dentro o fuera de la lista un elemento.
print('viernes' in dias) # si esta dentro in.
print('viernes' not in dias) # si esta fuera not in.

if ('viernes' in dias): # Dentro de if.
    print('Friday')

# Tuplas.
vocales = ('a','e','i','o','u')
print(vocales)

# Diccionarios.
numerosTelefono = {'Juan': '100','Maria':'200','Marco':'300','Ana':'400','Luis':'500'} #El primero es la clave y el segundo el valor.
print(numerosTelefono)
print(len(numerosTelefono))
# Metodo keys().
print('Numeros de telefono recorrido por clave')
for clave in numerosTelefono.keys(): # El keys recorre clave por clave.
    print(clave,'->',numerosTelefono[clave]) # Imprime la clave y el valor
# Siempre que tenemos datos variados usamos diccionarios.

# Borrar la clave con del, coloca la clave.
del numerosTelefono['Marco']
print(numerosTelefono)

print('Diccionario jugadores por clave')
jugadores= {22:'Alexander dominguez',15:'Angel Mena',8:'Maraco Caicedo',10:'Damian Diaz'}
for k in jugadores.keys():
    print(k,'->',jugadores[k])

# Otra forma de trabajara con diccionarios es usando el metodo  items().
print('Diccionario jugadores recorrido por items')
for tupla in numerosTelefono.items():
    print(tupla)

print('Diccionario jugadores por items')
for k in jugadores.items():
    print(k)

# Borrar el ultimo elemnto de la lista.
jugadores.popitem()
print(jugadores)





