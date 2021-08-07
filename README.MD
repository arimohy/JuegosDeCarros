# CHALLENGE - JUEGO DE CARROS POR CONSOLA
Por Yhomira Alexandra Yupayccana Lopa

## Use Case/Problem
Lo que se busca en este juego es crear unos carros y posicionarlo en una pista (cada
carro tiene un conductor), puede existir tantos carros como carriles, cada pista deberá
tener el mismo límite de distancia (kilómetros) para el recorrido del carro, los carros
avanzan de forma aleatoria aumentado su distancia por medio de metros (los kilómetros
de debe convertir a metros para que el avance sea en metros)
Cada avance debe existir un dado (de 1 a 6) que permite mover el carro y se debe
multiplicar por 100, donde si se tira el dado y sacas 5 entonces debería ser 5*100 = 500
metros de recorrido.
Al final debe existir un podio donde se clasifique primer, segundo y tercer ganador.

## Tecnologias
- Python
- Sqlite

## Para jugar el juego ejecutar el archivo "main.py"

- En el archivo Clases se encuentran las clases pista, juego, carril, carro, conductor,jugador, podio.
- Para la persistencia de datos se utilizo la base de datos sqllite que se crean automaticamente mientras juegan la base de datos se llama juegodecarros.db



