from random import randint, choices

##############################################
#               MENÚES & TEXTO               #
##############################################

MENU_INICIO = 1
MENU_CONFIGURACION = 2
JUGAR = 3
MENU_JUEGO_TERMINADO = 4

COMENZAR = 1
FINALIZAR = 2

SANDOKAN = 1
ARMADA = 2

FILA = 0
COLUMNA = 1

mensaje_bienvenida = "\n<------------------------------------------------------\
                      \nBienvenido al juego del Sandokán contra la Armada Británica\
                      \n------------------------------------------------------> by Nickuchi, Inc."
menu_inicio = "\n\n~|~|~|~ Menú Inicio ~|~|~|~\
              \n\nElija entre las siguientes opciones:\
              \n\n1) Comenzar a jugar\
              \n2) Salir\n\n"
mensaje_agua = "\n~ ~~ ~~ ~~~ ~ ~ ~ ~ ~~ ~ ~~\
                \n ~ ~ ~ A ~ G ~ U ~ A ~ ~ ~ \
                \n~ ~~ ~~ ~~~ ~ ~ ~ ~ ~ ~~ ~ ~\n\n"
resp = ''

##############################################
#                    JUEGO                   #
##############################################

DIMENSION_TABLERO_MIN = 10
DIMENSION_TABLERO_MAX = 24
HORIZONTAL = 0
VERTICAL = 1

tablero = []
dimension_tablero = DIMENSION_TABLERO_MIN
abecedario =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
porcentaje_exito_partida_especial = 30
lista_booleana = [True, False]

##############################################
#                   NAVES                    #
##############################################

CANTIDAD_BARCOS = 5

# Barcos de Sandokan y sus amigos
FUERTE = 0
DEPOSITO = 1
CAMPAMENTO = 2
DEFENSA_NORTE = 3
DEFENSA_SUR = 4

DIM_DEFENSA_SUR = 1
DIM_DEPOSITO = 2
DIM_DEFENSA_NORTE = 2
DIM_CAMPAMENTO = 3
DIM_FUERTE = 6

barcos_horizontales_sandokan = [DIM_FUERTE,DIM_DEPOSITO]
barcos_verticales_sandokan = [DIM_CAMPAMENTO,DIM_DEFENSA_NORTE,DIM_DEFENSA_SUR]
barcos_sandokan = [[], []]

# Barcos Armada británica
GALEON = 0
GALERA = 1
CRUCERO_PESADO = 2
CANIONERO = 3
BARCAZA = 4

DIM_BARCAZA = 1
DIM_GALERA = 2
DIM_CANIONERO = 2
DIM_GALEON = 3
DIM_CRUCERO_PESADO = 6

barcos_horizontales_armada = [DIM_GALEON,DIM_GALERA]
barcos_verticales_armada = [DIM_CRUCERO_PESADO,DIM_CANIONERO,DIM_BARCAZA]
barcos_armada = [[], []]

##############################################
#                 JUGADORES                  #
##############################################

NOMBRE = 0
PERSONAJE = 1
TABLERO = 2
BARCOS = 3
POSICIONES_BARCOS = 4
BARCOS_DISPONIBLES = 5
BARCOS_ROBADOS = 6
GANADOR = 7

barcos_jugador_1 = []
barcos_jugador_2 = []

##############################################
#                   BACK                     #
##############################################

def validar_data(mensaje_usuario, type_=None, min_=None, max_=None, list_=None):
  if min_ is not None and max_ is not None and max_ < min_:
    raise ValueError("Backend Error: Wrong parameter values\n")
  while True:
    usr_input = input(mensaje_usuario)
    if type_ is not None:
      try:
        data = type_(usr_input)
      except ValueError:
        print("Tipo de dato erróneo.\n")
        continue
    if list_ is not None:
      try:
        idx = list_.index(usr_input)
      except ValueError:
        print("Valor fuera de rango. Por favor, ingresarlo nuevamente.\n")
        continue
      if list_[1] < 1 or list_[1] > dimension_tablero:
        print("Valor fuera de rango. Por favor, ingresarlo nuevamente.\n")
    if max_ is not None and min_ is not None and (data < min_ or data > max_):
      print("Valor fuera de rango. Por favor, ingresar un número del {0} al {1}".format(min_, max_))
    else:
      return data

def traducir_numero_fila(numero):
  return abecedario[numero]

def ubicar_barcos_horizontales(tablero, jugador):
  indice_maximo = len(jugador[BARCOS][HORIZONTAL])
  for barco, indice_barco in zip(jugador[BARCOS][HORIZONTAL], range(indice_maximo)):
    fila, columna = [], []
    fila, columna = ubicar_barco(tablero, fila, columna, barco, HORIZONTAL)
    for x,y in zip(fila, columna):
      jugador[POSICIONES_BARCOS][indice_barco].append(x+str(y))

def ubicar_barcos_verticales(tablero, jugador):
  indice_minimo = len(jugador[BARCOS][HORIZONTAL])
  indice_maximo = len(jugador[BARCOS][HORIZONTAL] + jugador[BARCOS][VERTICAL])
  for barco, indice_barco in zip(jugador[BARCOS][VERTICAL], range(indice_minimo, indice_maximo)):
    fila, columna = [], []
    fila, columna = ubicar_barco(tablero, fila, columna, barco, VERTICAL)
    for x,y in zip(fila, columna):
      jugador[POSICIONES_BARCOS][indice_barco].append(x+str(y))

def ubicar_barco(tablero, fila, columna, dimension_barco, orientacion):
  w = h = 0
  if orientacion == HORIZONTAL: 
    w = dimension_barco 
  else:
    h = dimension_barco
  copia = tablero.copy()
  while True:
    x = randint(0, dimension_tablero-1)
    y = randint(0, dimension_tablero-1)
    condicion = (x+h) > dimension_tablero-1 or (y+w) > dimension_tablero-1 or copia[x+h][y+w] == '0'
    if not condicion:
      break
    tablero = copia.copy()
  for aux in range(dimension_barco):
    if orientacion == HORIZONTAL: 
      w = aux 
    else:
      h = aux
    tablero[x+h][y+w] = '0'
    fila.append(traducir_numero_fila(x+h))
    columna.append(y+w+1)
  return fila, columna

def ubicar_barcos(jugador):
  ubicar_barcos_horizontales(jugador[TABLERO], jugador)
  ubicar_barcos_verticales(jugador[TABLERO], jugador)

def generar_tablero(tablero, dimension_tablero):
  for i in range(dimension_tablero):
    fila = []
    for j in range(dimension_tablero):
      fila.append('~')
    tablero.append(fila)
  return tablero

def configurar_partida(jugador_1, jugador_2, tablero, dimension_tablero):
  print('\n\n¿Listos para jugar?')
  jugador_1[NOMBRE] = validar_data("\nNombre Jugador 1: ", str)
  jugador_2[NOMBRE] = validar_data("\nNombre Jugador 2: ", str)
  print('\n\n¡Elegí tu jugador!\n')
  jugador_1[PERSONAJE] = validar_data("1) Sandokan y sus amigos\n2) Armada británica\n\n", int, 1, 2)
  jugador_2[PERSONAJE] = ARMADA if jugador_1[PERSONAJE] == SANDOKAN else SANDOKAN
  dimension_tablero = validar_data("\n\nIngresá el tamaño del tablero (entre 10 y 24): ", int, 10, 24)
  porcentaje_exito_partida_especial = validar_data("\n\nPorcentaje de probabilidad de ganar un defensa del oponente en una Partida Especial: ", int, 0, 100)
  tablero = generar_tablero(tablero, dimension_tablero)
  return jugador_1, jugador_2, tablero, dimension_tablero

def setear_jugadores(jugador, barcos, contador_barcos):
  jugador[TABLERO] = tablero.copy()
  jugador[BARCOS] = barcos
  jugador[BARCOS_DISPONIBLES] = contador_barcos
  jugador[POSICIONES_BARCOS] = [[] for i in range(CANTIDAD_BARCOS)]
  ubicar_barcos(jugador)
  jugador[BARCOS_ROBADOS] = [[] for i in range(BARCOS_ROBADOS)]
  jugador[GANADOR] = False

##############################################
#                   FRONT                    #
##############################################

def imprimir_tablero(tablero, dimension_tablero):
  for columna in range(dimension_tablero):
      print('\t' if columna == 0 else '', columna + 1, end='\t')
  print()
  for fila in range(dimension_tablero):
    print(' ', abecedario[fila], end= '\t')
    print('\t'.join(tablero[fila]), end='\n')

def imprimir_barco_atacado(jugador, indice_barco, orientacion, robando_barco_ = False):
  if jugador[PERSONAJE] == SANDOKAN:
    if orientacion == HORIZONTAL:
      if indice_barco == FUERTE:
        barco_str = "Fuerte"
      elif indice_barco == DEPOSITO:
        barco_str = "Depósito"
    else:
      if indice_barco == CAMPAMENTO:
        barco_str = "Campamento"
      elif indice_barco == DEFENSA_NORTE:
        barco_str = "Defensa Norte"
      elif indice_barco == DEFENSA_SUR:
        barco_str = "Defensa Sur"
  else:
    if orientacion == HORIZONTAL:
      if indice_barco == GALEON:
        barco_str = "Galeón"
      elif indice_barco == GALERA:
        barco_str = "Galera"
    else:
      if indice_barco == CRUCERO_PESADO:
        barco_str = "Crucero Pesado"
      elif indice_barco == CANIONERO:
        barco_str = "Camionero"
      elif indice_barco == BARCAZA:
        barco_str = "Barcaza"
  adjetivo_femenino = "a" if barco_str == "Defensa Norte" or barco_str == "Defensa Sur" or barco_str == "Galera" or barco_str == "Barcaza" else ""
  if not robando_barco_:
    if jugador[BARCOS_DISPONIBLES][indice_barco] == 0:
      print("¡Hundiste un{0} {1}!".format(adjetivo_femenino, barco_str))
    elif not robando_barco_:
      print("¡Le pegaste a un{0} {1}!".format(adjetivo_femenino, barco_str))
  else:
    print("¡Te robaste un{0} {1}!".format(adjetivo_femenino, barco_str))

def orientacion_barco(barcos, indice):
  if indice >= 0:
    if indice < len(barcos[HORIZONTAL]):
      return HORIZONTAL
    elif indice > len(barcos[HORIZONTAL]) and indice < len(barcos[VERTICAL]):
      return VERTICAL
  else:
    return -1

def buscar_coordenada_barco(oponente, campo, coordenada, fila, columna):
  coordenada_encontrada = False
  for indice_barco in range(len(oponente[campo])):
    if not coordenada_encontrada:
      for i in range(len(oponente[campo][indice_barco])):
        if oponente[campo][indice_barco][i] == coordenada:
          oponente[BARCOS_DISPONIBLES][indice_barco]-=1
          orientacion = orientacion_barco(oponente[BARCOS], indice_barco)
          if orientacion != -1:
            imprimir_barco_atacado(oponente, indice_barco, orientacion)
            oponente[TABLERO][fila][columna] = 'X'
            coordenada_encontrada = True
            break
          else:
            print("No se encontró el barco")
    else:
      break
  return coordenada_encontrada

def atacar(oponente, coordenada, repetida):
  fila = abecedario.index(coordenada[FILA])
  columna = int(coordenada[COLUMNA])-1
  repetida = False
  if oponente[TABLERO][fila][columna] == '0':
    barco_encontrado = buscar_coordenada_barco(oponente, POSICIONES_BARCOS, coordenada, fila, columna)
    if not barco_encontrado:
      barco_encontrado = buscar_coordenada_barco(oponente, BARCOS_ROBADOS, coordenada, fila, columna)
  elif oponente[TABLERO][fila][columna] == 'x' or oponente[TABLERO][fila][columna] == 'X':
    repetida = True
    print('\n\n¡Ya atacaste esa coordenada!\n')
  else:
    oponente[TABLERO][fila][columna] = 'x'
    print(mensaje_agua)
  return all(barco_disponible == 0 for barco_disponible in oponente[BARCOS_DISPONIBLES]), repetida

def dimension_barco(personaje, barco):
  if personaje == SANDOKAN:
    if barco == FUERTE:
      return DIM_FUERTE 
    elif barco == DEPOSITO:
      return DIM_DEPOSITO 
    if barco == CAMPAMENTO:
      return DIM_CAMPAMENTO 
    elif barco == DEFENSA_NORTE:
      return DIM_DEFENSA_NORTE 
    elif barco == DEFENSA_SUR:
      return DIM_DEFENSA_SUR
  else:
    if barco == GALEON:
      return DIM_GALEON 
    elif barco == GALERA:
      return DIM_GALERA 
    if barco == CRUCERO_PESADO:
      return DIM_CRUCERO_PESADO
    elif barco == CANIONERO:
      return DIM_CANIONERO 
    elif barco == BARCAZA:
      return DIM_BARCAZA 

def indices_barcos_disponibles(personaje, barcos_jugador):
  barcos_disponibles = [dimension_tablero]*len(barcos_jugador)
  for barco, indice in zip(barcos_jugador, range(len(barcos_jugador))):
    if barco != 0:
      dim_barco = 0
      dim_barco = dimension_barco(personaje, indice)
      barcos_disponibles[indice] = dim_barco
  return barcos_disponibles

def robar_defensa(atacante, oponente):
  barcos_disponibles = [0]*BARCOS_DISPONIBLES
  barcos_disponibles = indices_barcos_disponibles(oponente[PERSONAJE], oponente[BARCOS_DISPONIBLES])
  dimension_barco_min = min(barcos_disponibles)
  indice = barcos_disponibles.index(dimension_barco_min)
  orientacion = orientacion_barco(oponente[BARCOS], indice)
  fila, columna = [], []
  fila, columna = ubicar_barco(atacante[TABLERO], fila, columna, dimension_barco_min, orientacion)
  for x,y in zip(fila, columna):
    atacante[BARCOS_ROBADOS][indice].append(x+str(y))
  imprimir_barco_atacado(oponente, indice, orientacion, True) 
  oponente[BARCOS_DISPONIBLES][indice] = 0
  return all(barco_disponible == 0 for barco_disponible in oponente[BARCOS_DISPONIBLES])

def setear_barcos():
  for barco in barcos_horizontales_sandokan:
    barcos_sandokan[HORIZONTAL].append(barco)
  for barco in barcos_verticales_sandokan:
    barcos_sandokan[VERTICAL].append(barco)
  for barco in barcos_horizontales_armada:
    barcos_armada[HORIZONTAL].append(barco)
  for barco in barcos_verticales_armada:
    barcos_armada[VERTICAL].append(barco)

def jugar(jugador_1, jugador_2):
  setear_barcos()
  generar_tablero(tablero, dimension_tablero)
  contador_barcos_sandokan = barcos_horizontales_sandokan + barcos_verticales_sandokan
  contador_barcos_armada = barcos_horizontales_armada + barcos_verticales_armada
  if jugador_1[PERSONAJE] == SANDOKAN:
    setear_jugadores(jugador_1, barcos_sandokan, contador_barcos_sandokan)
    setear_jugadores(jugador_2, barcos_armada, contador_barcos_armada)
  else:
    setear_jugadores(jugador_1, barcos_armada, contador_barcos_armada)
    setear_jugadores(jugador_2, barcos_sandokan, contador_barcos_sandokan)
  turno = 0
  while True:
    turno += 1
    coordenada_repetida = True
    partida_especial = choices(lista_booleana, weights=(porcentaje_exito_partida_especial, 100-porcentaje_exito_partida_especial), k=1)[0]
    print("\nPartida especial: ", partida_especial)
    if turno % 2 == 1:
      if jugador_1[PERSONAJE] == SANDOKAN:
        print("\n\n¡Turno para Sandokan y sus amigos!\n")
      else:
        print("\n\n¡Turno de las fuerzas británicas!\n")
      while coordenada_repetida:
        coordenada_de_ataque = validar_data("\n\nIngrese coordenada a atacar: ", str, abecedario)
        jugador_1[GANADOR], coordenada_repetida = atacar(jugador_2, coordenada_de_ataque, coordenada_repetida)
      if partida_especial:
        jugador_1[GANADOR] = robar_defensa(jugador_1, jugador_2)
    else:
      if jugador_2[PERSONAJE] == SANDOKAN:
        print("\n\n¡Turno para Sandokan y sus amigos!\n")
      else:
        print("\n\n¡Turno de las fuerzas británicas!\n")
      while coordenada_repetida:
        coordenada_de_ataque = validar_data("\n\nIngrese coordenada a atacar: ", str, abecedario)
        jugador_2[GANADOR], coordenada_repetida = atacar(jugador_1, coordenada_de_ataque, coordenada_repetida)
      if partida_especial:
        jugador_1[GANADOR] = robar_defensa(jugador_2, jugador_1)
    if jugador_1[GANADOR] or jugador_2[GANADOR]:
      break
  resp = menu(MENU_JUEGO_TERMINADO, jugador_1, jugador_2)
  return resp

def menu(tipo, jugador_1_ = None, jugador_2_ = None):
  if tipo == MENU_INICIO:
    print(mensaje_bienvenida)
    return validar_data(menu_inicio, int, 1, 2)
  elif tipo == MENU_JUEGO_TERMINADO:
    winner = jugador_1_[NOMBRE] if jugador_1_[GANADOR] else jugador_2_[NOMBRE]
    print('\n\n¡GANÓ {0}!'.format(winner))
    return FINALIZAR

##############################################
#                MAIN PROGRAM                #
##############################################

def main():
  resp = menu(MENU_INICIO)
  while True:
    if resp == COMENZAR:
      dimension_tablero = DIMENSION_TABLERO_MIN
      tablero = []
      jugador_1 = ['', 0, [[]*dimension_tablero], [[]*CANTIDAD_BARCOS], []*CANTIDAD_BARCOS, []*CANTIDAD_BARCOS, [], False]
      jugador_2 = ['', 0, [[]*dimension_tablero], [[]*CANTIDAD_BARCOS], []*CANTIDAD_BARCOS, []*CANTIDAD_BARCOS, [], False]
      jugador_1, jugador_2, tablero, dimension_tablero = configurar_partida(jugador_1, jugador_2, tablero, dimension_tablero)
      resp = jugar(jugador_1, jugador_2)
      continue
    if resp == FINALIZAR:
      quit()

if __name__ == "__main__":
  main()