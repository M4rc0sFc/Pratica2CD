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
        
        if self.id_nodo == 0:  'De esta forma sabemos si el nodo es el padre'
            yield env.timeout(TICK) 'Realiza iteraciones, funciona como un metodo iterador por un limite de tiempo'
            self.canal_salida.envia([self.id_nodo, 'GO'], self.vecinos)
        
            while True:
                mensaje = yield self.canal_entrada.get() 'Asignamos a mensaje un arreglo de tamaño 2 dado por el canal de entrada (?)'
                id_recibido = mensaje[0]   'En la primera entrada del arreglo se almacena el id de recibido'
                tipo_mensaje = mensaje[1]   'En la segunda entrada del arreglo mensaje se almacena el tipo de mensaje que se recibe'
                if tipo_mensaje == 'GO':    'Se espera recibir el mensaje GO'
                    if self.padre == None:    'Si el Nodo generador no tiene padre'
                            self.padre = id_recibido     'Se le asigna el id_recibido, el id de mensaje[0]'
                            self.mensajes_esperados == 1 'Estamos esperando recibir el mensaje 1'
                    if self.mensajes_esperados == 0:       'Si no recibimos ningún mensaje'
                            yield env.timeout(TICK)
                            self.canal_salida.envia([self.id_nodo, 'BACK'], [self.padre])
                            
                    else:                                                                   'Si recibimos algún mensaje entonces lo volvemos a enviar'
                        yield env.timeout(TICK)
                        self.canal_salida.envia([self.nodo, 'GO'], list(set(self.vecinos), set([self.padre])))
                elif:
                     yield env.timeout(TICK)
                     self canal_salida.envia([None, 'BACK'],[id_recibido])
                else:
                    tipo_mensaje = 'BACK'
                    self.mensajes_esperados = 1
                if id_recibido is not None: 
                     self.hijos.append(id_recibido)

