import simpy

class Canal():
    '''
    Interfaz que modela el comportamiento que cualquier canal debe tomar.
    '''
    def __init__(self, env: simpy.Environment, capacidad):
        '''Constructor de la clase. Se debe inicializar la lista de objetos Store al
        ser creado un canal.
        '''
         self.capacidad = capacidad
         self.almacen_objetos = []

    def envia(self, mensaje, vecinos):
        '''
        Envia un mensaje a los canales de entrada de los vecinos.
        '''
        for vecino in vecinos:
           vecino.canal_entrada = mensaje


    def crea_canal_de_entrada(self):
        '''
        Creamos un objeto Store en el un nodo recibirá los mensajes.
        '''
        almacen_mensajes = [] 
