
import numpy as np

vector1 = np.array([0,10,20,30,40,50,60,70,80,90])
vector2 = np.array([9,8,7,6,5,4,3,2,1,0])

matriz1 = np.array([[1,2,3],[4,5,6],[7,8,9]]) # De dos dimensiones.
matriz2 = np.array([[9,8,7],[6,5,4],[3,2,1]])

print('Vectores')
print(vector1)
print(vector2)
print(vector1.shape) # Saber la dimencion

# Iteracion  en arreglos vector y matriz. 
print('Recorre usando el indice del vector')
for i in range(0,9):  # Esto haciamos anates 
    print(i,'',vector1[i])

# Recorre directamente por el dato(for nuevo)
print('Recorre por el dato que existe dentro del vector')
for dato in vector1:  # Recorrer por el contenido de la informacion
    print(dato)

# Funciones agregadas mayor y menor.
print(vector1)
print(vector2)
print('Mayor: {} en indice'.format(vector1.max()))
print('Menor: {} en indice {}'.format(vector1.min(),vector1.argmin()))
print('Suma:',vector1+vector2)
print('Resta:',vector1 - vector2)
print('Multiplicacion:',vector1*vector2)
print('Division:',vector1 / vector2)



print('Matrizes')
print(matriz1)
print('')
print(matriz2)
print(matriz1.shape)

print('Recorre la matriz usando indices para fila y columna')
for f in range(0,3): # Usabamos antes
    for c in range(0,3):
        print(matriz1[f][c])
print('Recorre la matriz directamente por el dato')
# Iteracion en matrizes(Nuevo)
for fila in matriz1:
    for datos in fila:
        print(datos)

print('Suma de Matrizes:\n',matriz1+matriz2)
print('Resta de Matrizes:\n',matriz1-matriz2)
print('Multiplicacion de Matrizes:\n',matriz1*matriz2) # Esta no es correcta.
print('Multiplicacion real: \n',np.dot(matriz1,matriz2))




