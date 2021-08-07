import sqlite3

def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)

        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
    
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()


def insertar_productos(conexion,sql):
    cursor = conexion.cursor()
    cursor.executescript(sql)
    conexion.commit()
    
def actualizar_usuario(conexion, ganador):
    sql = 'UPDATE ganadores SET puntos = ?, puntos1 = ? ,puntos2 = ?, puntos3 = ? WHERE nombre = ?;'

    cursor = conexion.cursor()
    cursor.execute(sql, (ganador[1], ganador[2] ,ganador[3],ganador[4] ,ganador[0]))


conexion = crear_conexion('juegocarros2.db')

sql ="""
CREATE TABLE ganadores(
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    puntos TEXT NOT NULL,
    puntos1 INTEGER NOT NULL,
    puntos2 INTEGER NOT NULL,
    puntos3 INTEGER NOT NULL
)"""

insert="""
INSERT INTO ganadores(nombre,puntos,puntos1,puntos2,puntos3) VALUES ('yhomi', 1, 1, 0,0);
"""

ganador=['yhomi',1,0,0,1]
#crear_tabla(conexion, sql)

#insertar_productos(conexion,insert)


actualizar_usuario(conexion,ganador)
if conexion:
    conexion.close()