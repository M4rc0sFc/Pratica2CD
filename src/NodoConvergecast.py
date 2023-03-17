import simpy
import time
from Nodo import *
from NodoGenerador import *
from Canales.CanalBroadcast import *

# La unidad de tiempo
TICK = 1

class NodoConvergecast(NodoGenerador):
    ''' Implementa la interfaz de Nodo para el algoritmo de Broadcast.'''
    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida):
        '''Inicializamos el nodo.'''
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.padre = None
        self.mensaje = set()

    def convergecast(self, env):
        ##GENERADOR
        ##Primero se genera el arbol de la gráfica
        self.hijos = []
        if self.id_nodo == 0:
            self.padre = self.id_nodo
            self.mensajes_esperados = len(self.vecinos)
            yield env.timeout(TICK)
            self.canal_salida.envia([self.id_nodo, 'GO'], self.vecinos)
        else:
            self.padre = None
        
        while True and self.padre == None:
            mensaje = yield self.canal_entrada.get()
            id_recibido = mensaje[0]
            tipo_mensaje = mensaje[1]
            if tipo_mensaje == 'GO':
                if self.padre == None:
                    self.padre = id_recibido 
                    self.mensajes_esperados = len(self.vecinos) - 1
                    if self.mensajes_esperados == 0:      
                        yield env.timeout(TICK)
                        self.canal_salida.envia([self.id_nodo, 'BACK'], [self.padre])
                    else:
                        receptores = set(self.vecinos)
                        receptores.discard(id_recibido)
                        yield env.timeout(TICK)
                        self.canal_salida.envia([self.id_nodo, 'GO'], receptores)
                else:
                    yield env.timeout(TICK)
                    self.canal_salida.envia([None, 'BACK'],[id_recibido])

            elif tipo_mensaje == 'BACK':
                self.mensajes_esperados -= 1
                if id_recibido != None: 
                    self.hijos.append(id_recibido)
                if self.mensajes_esperados == 0:
                    if self.padre != self.id_nodo:
                        self.canal_salida.envia([self.id_nodo, 'BACK'],[self.padre])
        ##Convergecast
        ##Una vez que se ha generado el arbol (el nodo tiene un padre e hijos)
        ##Se ejecuta la parte del código correspondiente al algoritmo convergecast
        self.mensaje.add(self.id_nodo)
        if len(self.hijos)==0:
            yield env.timeout(TICK)
            self.canal_salida.envia([[self.id_nodo], 'CHILD'], [self.padre])

        while True:
            mensajeRecibido = yield self.canal_entrada.get()
            yield env.timeout(TICK)
            tipo_mensaje = mensajeRecibido[1]
            contenido_mensaje = mensajeRecibido[0]
            if tipo_mensaje == 'CHILD':
                self.mensaje.update(contenido_mensaje)
                self.canal_salida.envia([self.mensaje, 'CHILD'], [self.padre])
           
        
