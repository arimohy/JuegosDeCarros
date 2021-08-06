# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 18:37:17 2021

@author: arimo
"""

class Pista():
    limite=0
    listaCarriles=[]
    
    def __init__(self,limite,listaCarriles):
        self.limite=limite
        self.listaCarriles=listaCarriles
        
    def agregarCarril(self,carril):
        self.listaCarriles.append(carril)
        
        
        