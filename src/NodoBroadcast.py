import simpy
import time
from Nodo import *
from Canales.CanalBroadcast import *

# La unidad de tiempo
TICK = 1

class NodoBroadcast(Nodo):
    ''' Implementa la interfaz de Nodo para el algoritmo de Broadcast.'''
    def __init__(self, id_nodo, vecinos, canal_entrada: CanalBroadcast, canal_salida: CanalBroadcast, mensaje=None):
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.mensaje = mensaje
        

    def broadcast(self, env):
        ''' Algoritmo de Broadcast. Desde el nodo distinguido (0)
            vamos a enviar un mensaje a todos los demás nodos.'''

        if self.id_nodo == 0:
            yield env.timeout(tick)
            self.canal_salida.envia(self.mensaje, self.vecinos)
            
        self.canal_salida.envia(self.mensaje, self.vecinos)
        yield env.timeout(TICK)
