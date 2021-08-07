# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 19:02:40 2021

@author: arimo
"""
from random import randint
#clase conductor
class Conductor:
    nombre=""
    
    #constructor inicializado con nombre
    def __init__(self,nombre):
        self.nombre=nombre
#clase carro
class Carro():
    conductor=None
    
    def __init__(self,conductor):
        self.conductor=conductor

class Carril():
    carro=None
    posicion=0
    terminocarril=False
    
    def __init__(self,posicion,carro):
        self.posicion=posicion
        self.carro=carro
    def avanzar(self,avance):
        self.posicion=self.posicion-avance
        if(self.posicion<=0):
            self.terminocarril=True
        
        
    
        
class Pista():
    limite=0
    limitemetros=0
    listaCarriles=[]
    
    def __init__(self,limite,listaCarriles):
        self.limite=limite
        self.limitemetros=limite*1000
        self.listaCarriles=listaCarriles
        
    def agregarCarril(self,carril):
        self.listaCarriles.append(carril)
        
class Jugador():
    idJugador=0
    nombre=""
    puntos=0
    puntos1=0
    puntos2=0
    puntos3=0
    
    def __init__(self,nombre,puntos,puntos1,puntos2,puntos3):
        self.nombre=nombre
        self.puntos=puntos
        self.puntos1=puntos1
        self.puntos2=puntos2
        self.puntos3=puntos3
    
    def arreglo(self):
        a=[self.nombre,self.puntos,self.puntos1,self.puntos2,self.puntos3]
        return a
        
class Podio():
    primerlugar=""
    segundolugar=""
    tercerlugar=""
    completado=False
    
    def __init__(self):
        pass
        
    def asignarprimerlugar(self,nombre):
        self.primerlugar=nombre
    def asignarsegundolugar(self,nombre):
        self.segundolugar=nombre
    def asignartercerlugar(self,nombre):
        self.tercerlugar=nombre
        self.completado=True
        
    def imprimirresultados(self):
        print("....RESULTADOS....")
        print("primer puesto: "+self.primerlugar)
        print("segundo puesto: "+self.segundolugar)
        print("tercer puesto: "+self.tercerlugar)
        print(":::::::::::::::::::::::::::")
    
        

class Juego():

    limitepista=0
    limitepistametros=0
    nrojugadores=0
    pista=None
    ListaJugadores=[]
    ListaCarriles=[]
    Podio=Podio();
    contadoraux=0
    
    
    
    def __init__(self):
        print("Bienvenido al juego de carros")
        
    def datos(self):
        self.limitepista=int(input("Ingrese Limite o tamaño de la pista en Kilometros:"))
        self.limitepistametros=self.limitepista*1000
        self.nrojugadores=int(input("Ingrese numero de jugadores minimo son 3:"))
        
    def llenadocarriles(self):
        ListaConductores=[]
        for j in range(1,self.nrojugadores+1):
            nombrejugador=input("Ingrese nombre de jugador "+str(j)+":")
            conductor=Conductor(nombrejugador)
            carril=Carril(self.limitepistametros,conductor)
            ListaConductores.append(conductor)
            self.ListaCarriles.append(carril)
            
    def inicializandopista(self):
        self.pista=Pista(self.limitepista,self.ListaCarriles)
    def avancerandom(self):
        return 100*randint(1,6)
    def mostrarrecorrido(self,avance):
        n=self.limitepistametros/100
        print("Empieza otra ronda:")
        for i in range(0,len(avance)):
            avanzo=avance[i]/100
            j=self.ListaCarriles[i].carro.nombre
            print("Jugador "+j+" avanzo "+str(avance[i])+" de "+str(self.limitepistametros)+"(m)")
            print("*"*int(avanzo))
            print("_"*int(n))
            
            if(avanzo>=n and self.pista.listaCarriles[i].terminocarril==True):
                self.asignarpuesto(self.pista.listaCarriles[i])
        
    def asignarpuesto(self,carril):
        if(self.Podio.primerlugar!=carril.carro.nombre and self.Podio.segundolugar!=carril.carro.nombre and self.Podio.tercerlugar!=carril.carro.nombre):
            print(carril.carro.nombre)
            self.contadoraux+=1
            if(self.contadoraux==1):
                self.Podio.asignarprimerlugar(carril.carro.nombre)
            elif(self.contadoraux==2):
                self.Podio.asignarsegundolugar(carril.carro.nombre)
            elif(self.contadoraux==3):
                self.Podio.asignartercerlugar(carril.carro.nombre)
            else:
                print("ya hay ganadores")
    
    def competencia(self):
        avancejugadores=[0]*self.nrojugadores
        while(self.Podio.completado==False):
            for i in range(0,len(self.pista.listaCarriles)):
                if(self.pista.listaCarriles[i].terminocarril==False):
                    print("llega a ti")
                    avance=self.avancerandom()
                    avancejugadores[i]=avancejugadores[i]+avance
                    self.pista.listaCarriles[i].avanzar(avance)
            self.mostrarrecorrido(avancejugadores)
            
    def agregarlistajugadores(self):
        jugador1=Jugador(self.Podio.primerlugar,1,1,0,0)
        self.ListaJugadores.append(jugador1)
        jugador2=Jugador(self.Podio.segundolugar,1,0,1,0)
        self.ListaJugadores.append(jugador2)
        jugador3=Jugador(self.Podio.tercerlugar,1,0,0,1)
        self.ListaJugadores.append(jugador3)
        
        

    
    def empieza(self):
        self.datos()
        self.llenadocarriles()
        self.inicializandopista()
        self.competencia()
        self.Podio.imprimirresultados()
        self.agregarlistajugadores()
        


#juego1=Juego()
#juego1.empieza()




    