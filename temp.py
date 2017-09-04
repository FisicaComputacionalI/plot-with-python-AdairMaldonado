"""
Created on Mon Sep  4 02:09:10 2017

@author: Braian
"""
#Python usa librerias como matplotlib con objetos predeterminados como pyplot que tienen propiedades que permiten enviar las instrucciones a la maquina de una forma resumida. Matplotlib es una libreria para crear graficas en 2 dimensiones. 
import matplotlib.pyplot as plt
X = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
Y = [8,10,11,12,14,17,0,18,18,19,19,19,20,20,20,20,20,20,20,20,20,20]
plt.scatter(X, Y, s=60, c='red', marker='.')
plt.xlim(0,25)
plt.ylim(0,25)
plt.title('Numero de primos y hermanos por año de vida')
plt.ylabel('Numero de primos y hermanos por año')
plt.xlabel('Numero de años')
#Con esta isntruccion guardamos la imagen con el formato que queramos.
plt.savefig('temp.png')
#Con esta instruccion mostramos la figura. 
plt.show()
