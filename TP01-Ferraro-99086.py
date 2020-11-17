from random import randint, choices
import copy

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

mensaje_bienvenida = "\n\n\
                      \n█████████████████████████████████████████████████████████████████████████████\
                      \n█▄─▄─▀██▀▄─██─▄─▄─██▀▄─██▄─▄███▄─▄████▀▄─████▄─▀█▄─▄██▀▄─██▄─█─▄██▀▄─██▄─▄███\
                      \n██─▄─▀██─▀─████─████─▀─███─██▀██─██▀██─▀─█████─█▄▀─███─▀─███▄▀▄███─▀─███─██▀█\
                      \n▀▄▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▀▀▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀\
                      \n"
                      
menu_inicio = "\n\
              \n█▀ ▄█ ▀█   █▀▀ █▀█ █▀▄▀█ █▀▀ █▄░█ ▀█ ▄▀█ █▀█\
              \n█▄ ░█ ▄█   █▄▄ █▄█ █░▀░█ ██▄ █░▀█ █▄ █▀█ █▀▄\
              \n\
              \n█▀ ▀█ ▀█   █▀ ▄▀█ █░░ █ █▀█\
              \n█▄ █▄ ▄█   ▄█ █▀█ █▄▄ █ █▀▄\
              \n\
              \n:"

juego_finalizado = "\n\
                    \n░█▀▀█ ─█▀▀█ ░█▀▄▀█ ░█▀▀▀ 　 ░█▀▀▀█ ░█──░█ ░█▀▀▀ ░█▀▀█\
                    \n░█─▄▄ ░█▄▄█ ░█░█░█ ░█▀▀▀ 　 ░█──░█ ─░█░█─ ░█▀▀▀ ░█▄▄▀\
                    \n░█▄▄█ ░█─░█ ░█──░█ ░█▄▄▄ 　 ░█▄▄▄█ ──▀▄▀─ ░█▄▄▄ ░█─░█\
                    \n"

mensaje_agua = "\n~ ~~ ~~ ~~~ ~ ~ ~ ~ ~~ ~ ~~\
                \n ~ ~ ~ 𝗔 ~ 𝗚 ~ 𝗨 ~ 𝗔 ~ ~ ~\
                \n~ ~~ ~~ ~~~ ~ ~ ~ ~ ~ ~~ ~ ~\n\n"
resp = ''

##############################################
#                    JUEGO                   #
##############################################

DIMENSION_TABLERO_MIN = 10
DIMENSION_TABLERO_MAX = 24
HORIZONTAL = 0
VERTICAL = 1

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
TABLERO_ATAQUES = 3
BARCOS = 4
POSICIONES_BARCOS = 5
BARCOS_DISPONIBLES = 6
BARCOS_ROBADOS = 7
BARCOS_ROBADOS_DISPONIBLES = 8
GANADOR = 9

barcos_jugador_1 = []
barcos_jugador_2 = []

##############################################
#                   BACK                     #
##############################################

def validar_data(mensaje_usuario, tipo_=None, min_=None, max_=None, lista_=None, dimension_tablero_=None):
  if min_ is not None and max_ is not None and max_ < min_:
    raise ValueError("Backend Error: Wrong parameter values\n")
  while True:
    usr_input = input(mensaje_usuario)
    if tipo_ is not None:
      try:
        data = tipo_(usr_input)
      except ValueError:
        print("Tipo de dato erróneo.\n")
        continue
    if lista_ is not None:
      letra = usr_input[FILA]
      try:
        idx = lista_.index(letra)
      except ValueError:
        print("Valor fuera de rango. Por favor, ingresarlo nuevamente.\n")
        continue
      numero = int(usr_input[1:])
      if numero < 1 or numero > dimension_tablero_:
        print("Valor fuera de rango. Por favor, ingresarlo nuevamente.\n")
        continue
    if max_ is not None and min_ is not None and (data < min_ or data > max_):
      print("Valor fuera de rango. Por favor, ingresar un número del {0} al {1}".format(min_, max_))
    else:
      return data

def traducir_numero_fila(numero):
  return abecedario[numero]

def ubicar_barcos_horizontales(dimension_tablero, jugador):
  indice_maximo = len(jugador[BARCOS][HORIZONTAL])
  for barco, indice_barco in zip(jugador[BARCOS][HORIZONTAL], range(indice_maximo)):
    fila, columna = [], []
    fila, columna, jugador[TABLERO] = ubicar_barco(jugador[TABLERO], dimension_tablero, fila, columna, barco, HORIZONTAL)
    for x,y in zip(fila, columna):
      jugador[POSICIONES_BARCOS][indice_barco].append(x+str(y))

def ubicar_barcos_verticales(dimension_tablero, jugador):
  indice_minimo = len(jugador[BARCOS][HORIZONTAL])
  indice_maximo = len(jugador[BARCOS][HORIZONTAL] + jugador[BARCOS][VERTICAL])
  for barco, indice_barco in zip(jugador[BARCOS][VERTICAL], range(indice_minimo, indice_maximo)):
    fila, columna = [], []
    fila, columna, jugador[TABLERO] = ubicar_barco(jugador[TABLERO], dimension_tablero, fila, columna, barco, VERTICAL)
    for x,y in zip(fila, columna):
      jugador[POSICIONES_BARCOS][indice_barco].append(x+str(y))

def hay_barcos(tablero, dimension_barco, orientacion, fila, columna):
  w = h = 0
  barcos = False
  for aux in range(dimension_barco):
    if not barcos:
      if orientacion == HORIZONTAL: 
        w = aux 
      else:
        h = aux
      if tablero[fila+h][columna+w] == '0':
        barcos = True
    else:
      break
  return barcos

def ubicar_barco(tablero, dimension_tablero, fila, columna, dimension_barco, orientacion):
  w = h = 0
  if orientacion == HORIZONTAL: 
    w = dimension_barco 
  else:
    h = dimension_barco
  while True:
    x = randint(0, dimension_tablero-1)
    y = randint(0, dimension_tablero-1)
    fuera_de_rango = (x+h) > dimension_tablero-1 or (y+w) > dimension_tablero-1
    if not fuera_de_rango:
      if not hay_barcos(tablero, dimension_barco, orientacion, x, y):
        break
  for aux in range(dimension_barco):
    if orientacion == HORIZONTAL: 
      w = aux 
    else:
      h = aux
    tablero[x+h][y+w] = '0'
    fila.append(traducir_numero_fila(x+h))
    columna.append(y+w+1)
  return fila, columna, tablero

def ubicar_barcos(dimension_tablero, jugador):
  ubicar_barcos_horizontales(dimension_tablero, jugador)
  ubicar_barcos_verticales(dimension_tablero, jugador)

def generar_tablero(tablero, dimension_tablero):
  for i in range(dimension_tablero):
    fila = []
    for j in range(dimension_tablero):
      fila.append('~')
    tablero.append(fila)
  return tablero

def configurar_partida(jugador_1, jugador_2, tablero, dimension_tablero):
  print('\n\nVamo´ a jugá')
  jugador_1[NOMBRE] = validar_data("\nNombre Jugador 1: ", str)
  jugador_2[NOMBRE] = validar_data("\nNombre Jugador 2: ", str)
  print('\n\n¡Elegí tu jugador!\n')
  jugador_1[PERSONAJE] = validar_data("1) Sandokan y sus amigos\n2) Armada británica\n\n", int, SANDOKAN, ARMADA)
  jugador_2[PERSONAJE] = ARMADA if jugador_1[PERSONAJE] == SANDOKAN else SANDOKAN
  dimension_tablero = validar_data("\n\nIngresá el tamaño del tablero (entre 10 y 24): ", int, DIMENSION_TABLERO_MIN, DIMENSION_TABLERO_MAX)
  porcentaje_exito_partida_especial = validar_data("\n\nPorcentaje de probabilidad de ganar un defensa del oponente en una Partida Especial: ", int, 0, 100)
  tablero = generar_tablero(tablero, dimension_tablero)
  return jugador_1, jugador_2, tablero, dimension_tablero

def setear_jugadores(tablero, dimension_tablero, jugador, barcos, contador_barcos):
  jugador[TABLERO] = copy.deepcopy(tablero)
  jugador[TABLERO_ATAQUES] = copy.deepcopy(tablero)
  jugador[BARCOS] = barcos
  jugador[BARCOS_DISPONIBLES] = contador_barcos
  jugador[POSICIONES_BARCOS] = [[] for i in range(CANTIDAD_BARCOS)]
  ubicar_barcos(dimension_tablero, jugador)
  jugador[BARCOS_ROBADOS] = [[] for i in range(BARCOS_ROBADOS)]
  jugador[GANADOR] = False
  return jugador

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

def imprimir_barco_atacado(jugador, nombre_atacante, indice_barco, orientacion, robando_barco_ = False):
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
      print("¡{0} HUNDIÓ un{1} {2}!".format(nombre_atacante, adjetivo_femenino, barco_str))
    elif not robando_barco_:
      print("¡{0} ATACÓ a un{1} {2}!".format(nombre_atacante, adjetivo_femenino, barco_str))
  else:
    print("¡{0} se ROBÓ un{1} {2}!".format(nombre_atacante, adjetivo_femenino, barco_str))

def orientacion_barco(barcos, indice):
  if indice >= 0:
    if indice < len(barcos[HORIZONTAL]):
      return HORIZONTAL
    elif indice > len(barcos[HORIZONTAL]) and indice < len(barcos[HORIZONTAL])+len(barcos[VERTICAL]):
      return VERTICAL
  else:
    return -1

def atacar_barco(atacante, oponente, posiciones, contador, coordenada, fila, columna):
  coordenada_encontrada = False
  for indice_barco in range(len(oponente[posiciones])):
    if not coordenada_encontrada:
      for i in range(len(oponente[posiciones][indice_barco])):
        if oponente[posiciones][indice_barco][i] == coordenada:
          del oponente[posiciones][indice_barco][i]
          if contador == BARCOS_ROBADOS_DISPONIBLES:
            orientacion = orientacion_barco(oponente[BARCOS], indice_barco)
            oponente[contador][indice_barco]-=1
          elif contador == BARCOS_DISPONIBLES:
            oponente[contador][indice_barco]-=1
          orientacion = orientacion_barco(oponente[BARCOS], indice_barco)
          if orientacion != -1:
            imprimir_barco_atacado(oponente, atacante[NOMBRE], indice_barco, orientacion)
            oponente[TABLERO][fila][columna] = 'X'
            atacante[TABLERO_ATAQUES][fila][columna] = 'O'
            coordenada_encontrada = True
            break
          else:
            print("No se encontró el barco")
    else:
      break
  print("BCOS DISP: ", oponente[BARCOS_DISPONIBLES])
  print("BCOS robados DISP: ", oponente[BARCOS_ROBADOS_DISPONIBLES])
  return coordenada_encontrada, oponente, atacante

def atacar(atacante, oponente, coordenada, repetida):
  fila = abecedario.index(coordenada[FILA])
  columna = int(coordenada[1:])-1
  repetida = False
  if oponente[TABLERO][fila][columna] == '0':
    barco_encontrado, oponente, atacante = atacar_barco(atacante, oponente, POSICIONES_BARCOS, BARCOS_DISPONIBLES, coordenada, fila, columna)
    if not barco_encontrado:
      barco_encontrado, oponente, atacante = atacar_barco(atacante, oponente, BARCOS_ROBADOS, BARCOS_ROBADOS_DISPONIBLES, coordenada, fila, columna)
  elif oponente[TABLERO][fila][columna] == 'x' or oponente[TABLERO][fila][columna] == 'X':
    repetida = True
    print('\n\n¡Ya atacaste esa coordenada!\n')
  else:
    oponente[TABLERO][fila][columna] = 'x'
    atacante[TABLERO_ATAQUES][fila][columna] = 'o'
    print(mensaje_agua)
  no_tiene_barcos_robados = True
  for barco_robado in oponente[BARCOS_ROBADOS_DISPONIBLES]:
    if barco_robado != 0:
      no_tiene_barcos_robados = False
      break
  atacante[GANADOR] = all(barco_disponible == 0 for barco_disponible in oponente[BARCOS_DISPONIBLES]) and no_tiene_barcos_robados
  return atacante, oponente, repetida

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

def indices_barcos_disponibles(personaje, barcos_jugador, dimension_tablero):
  barcos_disponibles = [dimension_tablero]*len(barcos_jugador)
  for barco, indice in zip(barcos_jugador, range(len(barcos_jugador))):
    if barco != 0:
      dim_barco = 0
      dim_barco = dimension_barco(personaje, indice)
      barcos_disponibles[indice] = dim_barco
  return barcos_disponibles

def robar_defensa(atacante, oponente, dimension_tablero):
  barcos_disponibles = indices_barcos_disponibles(oponente[PERSONAJE], oponente[BARCOS_DISPONIBLES], dimension_tablero)
  dimension_barco_min = min(barcos_disponibles)
  indice = barcos_disponibles.index(dimension_barco_min)
  orientacion = orientacion_barco(oponente[BARCOS], indice)
  fila, columna = [], []
  fila, columna, atacante[TABLERO] = ubicar_barco(atacante[TABLERO], dimension_tablero, fila, columna, dimension_barco_min, orientacion)
  for x,y in zip(fila, columna):
    atacante[BARCOS_ROBADOS][indice].append(x+str(y))
  imprimir_barco_atacado(oponente, atacante[NOMBRE], indice, orientacion, True)
  for posicion in oponente[POSICIONES_BARCOS][indice]:
    x = abecedario.index(posicion[FILA])
    y = int(posicion[1:])-1
    oponente[TABLERO][x][y] = 'X'
  oponente[BARCOS_DISPONIBLES][indice] = 0
  personaje = oponente[PERSONAJE]
  atacante[BARCOS_ROBADOS_DISPONIBLES][indice] = dimension_barco_min
  no_tiene_barcos_robados = True
  for barco_robado in oponente[BARCOS_ROBADOS_DISPONIBLES]:
    if barco_robado != 0:
      no_tiene_barcos_robados = False
      break
  atacante[GANADOR] = all(barco_disponible == 0 for barco_disponible in oponente[BARCOS_DISPONIBLES]) and no_tiene_barcos_robados
  return atacante, oponente

def setear_barcos():
  for barco in barcos_horizontales_sandokan:
    barcos_sandokan[HORIZONTAL].append(barco)
  for barco in barcos_verticales_sandokan:
    barcos_sandokan[VERTICAL].append(barco)
  for barco in barcos_horizontales_armada:
    barcos_armada[HORIZONTAL].append(barco)
  for barco in barcos_verticales_armada:
    barcos_armada[VERTICAL].append(barco)

def jugar(tablero, dimension_tablero, jugador_1, jugador_2):
  setear_barcos()
  contador_barcos_sandokan = barcos_horizontales_sandokan + barcos_verticales_sandokan
  contador_barcos_armada = barcos_horizontales_armada + barcos_verticales_armada
  if jugador_1[PERSONAJE] == SANDOKAN:
    jugador_1 = setear_jugadores(tablero, dimension_tablero, jugador_1, barcos_sandokan, contador_barcos_sandokan)
    jugador_2 = setear_jugadores(tablero, dimension_tablero, jugador_2, barcos_armada, contador_barcos_armada)
  else:
    jugador_1 = setear_jugadores(tablero, dimension_tablero, jugador_1, barcos_armada, contador_barcos_armada)
    jugador_2 = setear_jugadores(tablero, dimension_tablero, jugador_2, barcos_sandokan, contador_barcos_sandokan)
  turno = 0
  while True:
    turno += 1
    coordenada_repetida = True
    partida_especial = choices(lista_booleana, weights = [porcentaje_exito_partida_especial, 100-porcentaje_exito_partida_especial])[0]
    if turno % 2 == 1:
      if jugador_1[PERSONAJE] == SANDOKAN:
        print("\n\n¡Turno para SANDOKAN Y SUS AMIGOS!\n")
      else:
        print("\n\n¡Turno de las FUERZAS BRITÁNICAS!\n")
      imprimir_tablero(jugador_2[TABLERO_ATAQUES], dimension_tablero)
      print()
      imprimir_tablero(jugador_2[TABLERO], dimension_tablero)
      while coordenada_repetida:
        coordenada_de_ataque = validar_data("\n\nIngrese coordenada a atacar: ", str, None, None, abecedario, dimension_tablero)
        jugador_1, jugador_2, coordenada_repetida = atacar(jugador_1, jugador_2, coordenada_de_ataque, coordenada_repetida)
      if partida_especial:
        jugador_1, jugador_2 = robar_defensa(jugador_1, jugador_2, dimension_tablero)
    else:
      if jugador_2[PERSONAJE] == SANDOKAN:
        print("\n\n¡Turno para SANDOKAN Y SUS AMIGOS!\n")
      else:
        print("\n\n¡Turno de las FUERZAS BRITÁNICAS!\n")
      imprimir_tablero(jugador_1[TABLERO_ATAQUES], dimension_tablero)
      print()
      imprimir_tablero(jugador_1[TABLERO], dimension_tablero)
      while coordenada_repetida:
        coordenada_de_ataque = validar_data("\nIngrese coordenada a atacar: ", str, None, None, abecedario, dimension_tablero)
        jugador_2, jugador_1, coordenada_repetida = atacar(jugador_2, jugador_1, coordenada_de_ataque, coordenada_repetida)
      if partida_especial:
        jugador_2, jugador_1 = robar_defensa(jugador_2, jugador_1, dimension_tablero)
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
    print(juego_finalizado)
    print('\n¡GANÓ {0}!\n\n'.format(winner))
    return FINALIZAR

##############################################
#                MAIN PROGRAM                #
##############################################

def main():
  resp = menu(MENU_INICIO)
  while True:
    if resp == COMENZAR:
      dimension_tablero = 0
      tablero = []
      jugador_1 = ['', 0, []*dimension_tablero, []*dimension_tablero, []*CANTIDAD_BARCOS, []*CANTIDAD_BARCOS, []*CANTIDAD_BARCOS, []*CANTIDAD_BARCOS, [0]*CANTIDAD_BARCOS, False]
      jugador_2 = ['', 0, []*dimension_tablero, []*dimension_tablero, []*CANTIDAD_BARCOS, []*CANTIDAD_BARCOS, []*CANTIDAD_BARCOS, []*CANTIDAD_BARCOS, [0]*CANTIDAD_BARCOS, False]
      jugador_1, jugador_2, tablero, dimension_tablero = configurar_partida(jugador_1, jugador_2, tablero, dimension_tablero)
      resp = jugar(tablero, dimension_tablero, jugador_1, jugador_2)
      continue
    if resp == FINALIZAR:
      quit()

if __name__ == "__main__":
  main()