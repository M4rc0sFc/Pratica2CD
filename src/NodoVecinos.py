import simpy
from Nodo import *
from Canales.CanalBroadcast import *

class NodoVecinos(Nodo):
    ''' Implementa la interfaz de Nodo para el algoritmo de conocer a los
        vecinos de tus vecinos.'''
    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida):
        '''Inicializamos el nodo.'''
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        print(type(canal_entrada))
        self.canal_salida = canal_salida

        self.identifiers = set()
        


    def conoceVecinos(self, env):
        ''' Algoritmo que hace que el nodo conozca a los vecinos de sus vecinos.
            Lo guarda en la variable identifiers.'''
        self.canal_salida.envia(self.vecinos, self.vecinos)
        while True:
            mensaje = yield self.canal_entrada.get()
            self.identifiers.update(mensaje)

