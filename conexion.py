# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 06:30:43 2021

@author: arimo
"""

  
import sqlite3
#Import database
database = "juegocarros.db"
class DB:
    def ejecutar_consulta(self,consulta,parametros = ()):
        with sqlite3.connect(database) as conn:
            self.cursor = conn.cursor()
            
            result = self.cursor.execute(consulta,parametros)
            conn.commit()
            return result

    def crear_tabla(self):
        sql= """
        CREATE TABLE IF NOT EXISTS ganadores(
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            puntos INTEGER NOT NULL,
            puntos1 INTEGER NOT NULL,
            puntos2 INTEGER NOT NULL,
            puntos3 INTEGER NOT NULL
        )"""
        self.ejecutar_consulta(sql)

       