import simpy
from Nodo import *
from Canales.CanalBroadcast import *

TICK = 1

class NodoGenerador(Nodo):
    '''Implementa la interfaz de Nodo para el algoritmo de flooding.'''
    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida):
        '''Inicializamos el nodo.'''
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.padre = None
        if(id_nodo == 0):
            self.padre = id_nodo
        self.hijos = vecinos

    def genera_arbol(self, env):
        yield env.timeout(1)

