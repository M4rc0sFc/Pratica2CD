import simpy
from Canales.Canal import Canal

class CanalBroadcast(Canal):
    '''
    Clase que modela un canal, permite enviar mensajes one-to-many.
    '''
    def __init__(self, env, capacidad=simpy.core.Infinity):

    def envia(self, mensaje, vecinos):
        '''
        Envia un mensaje a los canales de salida de los vecinos.
        '''
    def crea_canal_de_entrada(self):
        '''
        Creamos un canal de entrada
        '''
