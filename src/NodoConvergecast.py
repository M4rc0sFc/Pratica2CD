import simpy
import time
from Nodo import *
from Canales.CanalBroadcast import *

# La unidad de tiempo
TICK = 1

class NodoConvergecast(Nodo):
    ''' Implementa la interfaz de Nodo para el algoritmo de Broadcast.'''
    def __init__(self, id_nodo, vecinos, canal_entrada: CanalBroadcast, canal_salida: CanalBroadcast, mensaje=None):
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.valset = set()
        

    def broadcast(self, env):
        ''' Algoritmo de Broadcast. Desde el nodo distinguido (0)
            vamos a enviar un mensaje a todos los demás nodos.'''

        self.valset.add(self.id_nodo)

        if self.vecinos == None:
            self.canal_salida.envia(self.padre, self.valset)
            
        while True:
            self.mensaje = yield self.canal_entrada.get()
            self.canal_salida.envia(self.mensaje, self.vecinos)