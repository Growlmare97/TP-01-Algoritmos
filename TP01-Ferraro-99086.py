from random import randint, choices

##############################################
#               MENÚES & TEXTO               #
##############################################

MENU_INICIO = 1
MENU_CONFIGURACION = 2

COMENZAR = 1
FINALIZAR = 2

SANDOKAN = 1
ARMADA = 2

FILA = 0
COLUMNA = 1

mensaje_bienvenida = "\n<------------------------------------------------------\
                      \nBienvenido al juego del Sandokán contra la Armada Británica\
                      \n------------------------------------------------------> by Nickuchi, Inc."

##############################################
#                    JUEGO                   #
##############################################

tablero = []
abecedario =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
porcentaje_exito_partida_especial = 30

##############################################
#                 JUGADORES                  #
##############################################

# Índices correspondientes para acceder en la 
# lista que guarda la data de cada jugador
NOMBRE = 0
PERSONAJE = 1
TABLERO = 2
POSICIONES_BARCOS = 3
BARCOS_DISPONIBLES = 4
BARCOS_DERRIBADOS = 5
GANADOR = 6

jugador_1 = []
jugador_2 = []

##############################################
#                   NAVES                    #
##############################################

CANTIDAD_BARCOS = 5

# Barcos de Sandokan y sus amigos
FUERTE = 6
DEPOSITO = 2
CAMPAMENTO = 3
DEFENSA_NORTE = 2
DEFENSA_SUR = 1

barcos_horizontales_sandokan = [FUERTE,DEPOSITO]
barcos_verticales_sandokan = [CAMPAMENTO,DEFENSA_NORTE,DEFENSA_SUR]
barcos_sandokan = []

# Barcos Armada británica
GALEON = 3
GALERA = 2
CRUCERO_PESADO = 6
CANIONERO = 2
BARCAZA = 1

barcos_horizontales_armada = [GALEON,GALERA]
barcos_verticales_armada = [CRUCERO_PESADO,CANIONERO,BARCAZA]
barcos_armada = []

##############################################
#                   BACK                     #
##############################################

def validar_data(mensaje_usuario, type_=None, min_=None, max_=None, list_=None):
  if min_ is not None and max_ is not None and max_ < min_:
    raise ValueError("Backend Error: Wrong parameter values")
  while True:
    usr_input = input(mensaje_usuario)
    if type_ is not None:
      try:
        data = type_(usr_input)
      except ValueError:
        print("Tipo de dato erróneo.")
        continue
    if list_ is not None:
      try:
      idx = list_.index(usr_input)
      except ValueError:
        print("Valor fuera de rango. Por favor, ingresarlo nuevamente.")
        continue
      if list_[1] < 1 or list_[1] > dimension_tablero:
        print("Valor fuera de rango. Por favor, ingresarlo nuevamente.")
    if max_ is not None and min_ is not None and (data < min_ or data > max_):
      print("Valor fuera de rango. Por favor, ingresar un número del {0} al {1}".format(min_, max_))
    else:
      return data

def traducir_numero_fila(numero):
  return abecedario[numero]

def ubicar_naves_horizontales(tablero, jugador):
  coordenadas_naves_horizontales = []
  for dimension_nave, nave in naves_horizontales, range(naves_horizontales.len):
    fila = []
    columna = []
    x = randint(0, dimension_tablero-1)
    y = randint(0, dimension_tablero-1)
    copia = tablero
    for i in range(dimension_nave):
      while (y+dimension_nave) > dimension_tablero or copia[x][y+i] == "O":
        copia = tablero
        x = randint(0, dimension_tablero-1)
        y = randint(0, dimension_tablero-1)
      copia[x][y+i] = "O"
      fila.append(x+1)
      columna.append(y+i)
      coordenadas_naves_horizontales.append(traducir_numero_fila(fila)+str(columna))
  jugador[POSICIONES_BARCOS][nave].append(coordenadas_naves_horizontales)

def ubicar_naves_verticales(tablero, jugador):
  coordenadas_naves_verticales = []
  for establecimiento_vertical,nave in naves_verticales, range(naves_horizontales.len, naves_horizontales.len + naves_verticales.len):
    fila = []
    columna = []
    x = randint(0, dimension_tablero-1)
    y = randint(0, dimension_tablero-1)
    copia = tablero
    for i in range(establecimiento_vertical):
      while (x+establecimiento_vertical) > dimension_tablero or copia[x+i][y]=="O":
        copia = tablero
        x = randint(0, dimension_tablero-1)
        y = randint(0, dimension_tablero-1)
      copia[x+i][y] = "O"
      fila.append(x+i+1)
      columna.append(y)
    coordenadas_naves_verticales.append(traducir_numero_fila(fila)+str(columna))
  jugador[POSICIONES_BARCOS][nave].append(coordenadas_naves_verticales)

def ubicar_naves(jugador):
  ubicar_naves_horizontales(jugador[TABLERO], jugador)
  ubicar_naves_verticales(jugador[TABLERO], jugador)

def generar_tablero(tablero, dimension_tablero):
  for i in range(dimension_tablero):
      fila = []
      for j in range(dimension_tablero):
        fila.append('*')
      tablero.append(fila)
  return tablero

def configuracion_partida(jugador_1, jugador_2, dimension_tablero)
  jugador_1,jugador_2,dimension_tablero,porcentaje_exito_partida_especial = menu(MENU_CONFIGURACION)

def setear_data(jugador, barcos)
  jugador[TABLERO] = tablero
  jugador[POSICIONES_BARCOS] = [[]]*CANTIDAD_BARCOS
  ubicar_naves(jugador[TABLERO])
  jugador[BARCOS_DISPONIBLES] = barcos
  jugador[GANADOR] = False

##############################################
#                   FRONT                    #
##############################################

def imprimir_tablero(tablero,dimension_tablero):
  for j in range(dimension_tablero):
    print(" ",lista_abecedario[j], end= "")
  for fila in range(dimension_tablero):
    print(f"\n{fila + 1}", end ="  ")
    for i in range(dimension_tablero):
      print(tablero[fila][i], end="  ")

def imprimir_barco_atacado(jugador, barco):
  if jugador[PERSONAJE] == SANDOKAN:
    if barco == FUERTE:
      barco = "Fuerte"
    elif barco == DEPOSITO:
      barco = "Depósito"
    elif barco == CAMPAMENTO:
      barco = "Campamento"
    elif barco == DEFENSA_NORTE:
      barco = "Defensa Norte"
    elif barco == DEFENSA_SUR:
      barco = "Defensa Sur"
  else:
    if barco == GALEON:
      barco = "Galeón"
    elif barco == GALERA:
      barco = "Galera"
    elif barco == CRUCERO_PESADO:
      barco = "Crucero Pesado"
    elif barco == CANIONERO:
      barco = "Camionero"
    elif barco == BARCAZA:
      barco = "Barcaza"
  adjetivo_femenino = "a" if barco == "Defensa Norte" or barco == "Defensa Sur" or barco == "Galera" or barco == "Barcaza" else ""
  if jugador[BARCOS_DISPONIBLES][nave] == 0:
    print("¡Hundiste un{0} {1}!".format(adjetivo_femenino, barco))
    jugador[BARCOS_DERRIBADOS]+=1
  else:
    print("¡Le pegaste a un{0} {1}!".format(adjetivo_femenino, barco))

def atacar(jugador, coordenada):
  fila = coordenada[FILA]
  columna = coordenada[COLUMNA]
  if jugador[TABLERO][fila][columna] == '0':
    for nave in range(jugador[POSICIONES_BARCOS].len):
      if nave[fila][columna] == coordenada:
        jugador[BARCOS_DISPONIBLES][nave]-=1
        imprimir_barco_atacado(jugador, nave)
  else:
    print("~ ~ ~ A ~ G ~ U ~ A ~ ~ ~")
  return all(barco_disponible == 0 for barco_disponible in jugador[BARCOS_DISPONIBLES])

def jugar(jugador_1, jugador_2):
  turno = 0
  do
  turno += 1
  if jugador[PERSONAJE] == SANDOKAN:
    print("¡Turno para Sandokan y sus amigos!")
  else:
    print("¡Turno de las fuerzas británicas!")
  coordenada_de_ataque = validar_data("Ingrese coordenada a atacar: ", str, abecedario)
  if turno % 2 == 1:
    jugador_1[GANADOR] = atacar(jugador_2, coordenada_de_ataque)
  else:
    jugador_2[GANADOR] = atacar(jugador_1, coordenada_de_ataque)
  while(not jugador_1[GANADOR] and not jugador_2[GANADOR])

def menu(tipo):
  if tipo == MENU_INICIO:
    print(mensaje_bienvenida)
    return validar_data("\n\n~ Menú Inicio ~\nElija entre las siguientes opciones:\n1) Comenzar a jugar\n2) Salir\n\n", int, 1, 2)
  elif tipo == MENU_CONFIGURACION:
    print('\n\n¿Listos para jugar?\n')
    jugador_1[NOMBRE] = validar_data("\nNombre Jugador 1: ", str)
    jugador_2[NOMBRE] = validar_data("\nNombre Jugador 2: ", str)
    print('\n\n¡Elegí tu jugador!\n')
    jugador_1[PERSONAJE] = validar_data("1) Sandokan y sus amigos\n2) Armada británica", int, 1, 2)
    jugador_2[PERSONAJE] = SANDOKAN if jugador_1[PERSONAJE] == ARMADA else ARMADA
    dimension_tablero = validar_data("\n\nIngresá el tamaño del tablero (entre 10 y 24): ", int, 10, 24)
    porcentaje_exito_partida_especial = print("\n\nYa casi está todo listo...\nFalta elegir el porcentaje de probabilidad de ganar un defensa en una Partida Especial: ", int, 0, 100)
    return jugador_1,jugador_2,dimension_tablero,porcentaje_exito_partida_especial
  elif tipo == JUGAR:
    barcos_sandokan.append(barcos_horizontales_sandokan + barcos_verticales_sandokan)
    barcos_armada.append(barcos_horizontales_armada + barcos_verticales_armada)
    generar_tablero(tablero, dimension_tablero)
    if jugador_1[PERSONAJE] == SANDOKAN:
      setear_data(jugador_1, barcos_sandokan)
      setear_data(jugador_2, barcos_armada)
    else:
      setear_data(jugador_1)
      setear_data(jugador_2)
    jugar(jugador_1, jugador_2)

##############################################
#                MAIN PROGRAM                #
##############################################

def main():
  do
    resp = menu(MENU_INICIO)
    if resp == COMENZAR:
      configuracion_partida(jugador_1, jugador_2, dimension_tablero)
      jugar(jugador_1, jugador_2)
  while(resp != FINALIZAR)

if __name__ == "__main__":
  main()