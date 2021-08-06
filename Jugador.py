# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:47:47 2021

@author: arimo
"""


class Jugador():
    idJugador=0
    nombre=""
    puntos=0
    puntos1=0
    puntos2=0
    puntos3=0
    
    def __init__(self,nombre):
        self.nombre=nombre
    
    def agregarpuntoprimer(self):
        self.puntos=self.puntos+1
        self.puntos1==self.puntos1+1
    
    def agregarpuntosegundo(self):
        self.puntos+=1
        self.puntos2+=1
        
    def agregarpuntotercer(self):
        self.puntos+=1
        self.puntos3+=1
    
    