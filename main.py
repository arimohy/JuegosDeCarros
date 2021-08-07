from Clases import * 
import conexion as con

db=con.DB()    
    
def main():
    #base de datos
    db.crear_tabla()
    #juego
    juego1=Juego()
    juego1.empieza()
    lista=juego1.ListaJugadores
    for i in lista:
        print(i.arreglo())
        consulta="SELECT * FROM ganadores WHERE nombre = ?"
        result = db.ejecutar_consulta(consulta,i.arreglo()[0])
        recuperar=result.fetchall()
        if(recuperar==[]):
            print("esta vacio")
            #insertaremos nuevos registros
            qinsert="INSERT INTO ganadores(nombre,puntos,puntos1,puntos2,puntos3) VALUES (?, ?, ?, ?,?);"
            jugador=i.arreglo()
            parametros=(jugador[0],jugador[1],jugador[2],jugador[3],jugador[4])
            db.ejecutar_consulta(qinsert,parametros)
        else:
            #existe y se debe actualizar
            jugador=i.arreglo()
            nuevo=[]
            for n in range(1,5):
                nuevo.append(jugador[n]+recuperar[0][n+1])
            
            print(nuevo)
            qupdate='UPDATE ganadores SET puntos = ?, puntos1 = ? ,puntos2 = ?, puntos3 = ? WHERE nombre = ?;'
            #q="INSERT INTO ganadores(nombre,puntos,puntos1,puntos2,puntos3) VALUES ('yhomi', 1, 0, 0,1)"
            parametros=(nuevo[0],nuevo[1],nuevo[2],nuevo[3],jugador[0])
            db.ejecutar_consulta(qupdate,parametros)
            #db.ejecutar_consulta(q)
            #print(parametros)
 
print("#####################################################")
c=True
while(c):
    main()
    r=input("Desea segui jugando escriba si o no:")
    if(r=='no'):
        c=False


    
    