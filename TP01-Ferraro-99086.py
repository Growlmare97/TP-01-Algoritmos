from random import randint

lista_abecedario =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

welcome_message = "\n<------------------------------------------------------\
                  \nBienvenido al juego del Sandokán contra la Armada Británica\
                  \n------------------------------------------------------> by Nacho, Inc."



FUERTE = 6
CAMPAMENTO = 3
DEPOSITO = 2
DEFENSA_NORTE = 2
DEFENSA_SUR = 1

FUERTE_SIMBOLO = 1
CAMPAMENTO_SIMBOLO = 2
DEPOSITO_SIMBOLO = 3
DEFENSA_NORTE_SIMBOLO = 4
DEFENSA_SUR_SIMBOLO = 5

barcos_horizontales_sandokan = [FUERTE,DEPOSITO]
barcos_verticales_sandokan = [CAMPAMENTO,DEFENSA_NORTE,DEFENSA_SUR]

barcos_horizontales_sandokan_simbolo = [FUERTE_SIMBOLO,DEPOSITO_SIMBOLO]
barcos_verticales_sandokan_simbolo = [CAMPAMENTO_SIMBOLO,DEFENSA_NORTE_SIMBOLO,DEFENSA_SUR_SIMBOLO]

coordenadas_fuerte = [0]*FUERTE
coordenadas_deposito = [0]*DEPOSITO
coordenadas_campamento = [0]*CAMPAMENTO
coordenadas_defensa_norte = [0]*DEFENSA_NORTE
coordenadas_defensa_sur = [0]*DEFENSA_SUR


CRUCERO_PESADO = 6
GALEON = 3
CANIONERO = 2
GALERA = 2
BARCAZA = 1

CRUCERO_PESADO_SYMBOLO = 1
GALEON_SIMBOLO = 2
CANIONERO_SIMBOLO = 3
GALERA_SIMBOLO = 4
BARCAZA_SIMBOLO = 5


barcos_horizontales_armada = [GALEON,GALERA]
barcos_verticales_armada = [CRUCERO_PESADO,CANIONERO,BARCAZA]

barcos_horizontales_armada_simbolo = [GALEON_SIMBOLO,GALERA_SIMBOLO]
barcos_verticales_armada_simbolo = [CRUCERO_PESADO_SYMBOLO,CANIONERO_SIMBOLO,BARCAZA_SIMBOLO]

#La función validate_data me valida los inputs que tengo. Me servirá para saber el tamaño del tablero y la ubicación de los ingresos.

def validate_data(display_message, type_=None, min_=None, max_=None):
  if min_ is not None and max_ is not None and max_ < min_:
    raise ValueError("Backend Error: Wrong parameter values")
  while True:
    usr_input = input(display_message)
    if type_ is not None:
      try:
        data = type_(usr_input)
      except ValueError:
        print("Tipo de dato erróneo.")
        continue
    if max_ is not None and min_ is not None and (data < min_ or data > max_):
      print("Valor fuera de rango. Por favor, ingresar un número del {0} al {1}".format(min_, max_))
    else:
      return data

def numero_a_letra(numero):
  return lista_abecedario[numero]

#Con la función asignar_aleatoriamente puedo cambiar el tablero en función de cada jugador

def asignar_aleatoriamente(tablero,naves_horizontales,naves_verticales,tamanio_tablero,naves_horizontales_simbolo,naves_verticales_simbolo):
  ubicacion_vertical = []
  ubicacion_horizontal = []
  for establecimiento_horizontal in naves_horizontales:
    coordenadas_nave_horizontal_X = []
    coordenadas_nave_horizontal_Y = []
    x = randint(0, tamanio_tablero-1)
    y = randint(0, tamanio_tablero-1)
    copia = tablero
    for i in range(establecimiento_horizontal):
      while (y+establecimiento_horizontal)>tamanio_tablero or copia[x][y+i]=="O":
        copia = tablero
        x = randint(0, tamanio_tablero-1)
        y = randint(0, tamanio_tablero-1)
      copia[x][y+i] = naves_horizontales_simbolo[naves_horizontales.index(establecimiento_horizontal)]
      coordenadas_nave_horizontal_X.append(x+1)
      coordenadas_nave_horizontal_Y.append(numero_a_letra(y+i+1))
    ubicacion_horizontal.append((coordenadas_nave_horizontal_X,coordenadas_nave_horizontal_Y))

  for establecimiento_vertical in naves_verticales:
    coordenada_nave_vertical_X = []
    coordenada_nave_vertical_Y = []
    x = randint(0, tamanio_tablero-1)
    y = randint(0, tamanio_tablero-1)
    copia = tablero
    for i in range(establecimiento_vertical):
      while (x+establecimiento_vertical)>tamanio_tablero or copia[x+i][y]=="O":
        copia = tablero
        x = randint(0, tamanio_tablero-1)
        y = randint(0, tamanio_tablero-1)
      copia[x+i][y] = naves_verticales_simbolo[naves_verticales.index(establecimiento_vertical)]
      coordenada_nave_vertical_X.append(x+i+1)
      coordenada_nave_vertical_Y.append(numero_a_letra(y+1))
    ubicacion_vertical.append((coordenada_nave_vertical_X,coordenada_nave_vertical_Y))
  return copia,ubicacion_horizontal,ubicacion_vertical


#Con la función mostrar_tablero puedo mostrar el tablero. Lo voy a usar en cada turno del jugador.

def mostrar_tablero(tablero,tamanio_tablero):
  for j in range(tamanio_tablero):
    print(" ",lista_abecedario[j], end= "")
  for fila in range(tamanio_tablero):
    print(f"\n{fila + 1}", end ="  ")
    for i in range(tamanio_tablero):
      print(tablero[fila][i], end="  ")

#Con la función generar_tablero puedo generar el tablero inicial que voy a mutar posteriormente

def generar_tablero(tablero, tamanio_tablero):
  for i in range(tamanio_tablero):
      fila = []
      for j in range(tamanio_tablero):
        fila.append('*')
      tablero.append(fila)
  return tablero

#Con la función main voy a inicializar el programa

def jugar(eleccion,jugador_1, jugador_2,tamanio_tablero,juego_terminado,turnos,horizontal_1,vertical_1,horizontal_2,vertical_2):
  while juego_terminado != True:
    if eleccion == 1:
      if turnos%2==1:
        print("Turno para Sandokan y sus amigos!")
        adivina_fila = validate_data("Ingrese fila: ", int, 1, tamanio_tablero)
        adivina_columna = validate_data("Ingrese columna: ", int, 1, tamanio_tablero)
        if jugador_2[adivina_fila-1][adivina_columna-1] == 1 or 2 or 3 or 4 or 5:
          jugador_2[adivina_fila-1][adivina_columna-1] = "X"
          print("Le pegaste al barco")
        else:
          if jugador_2[adivina_fila-1][adivina_columna-1] == "X" or jugador_2[adivina_fila-1][adivina_columna-1] == "/":
            print("Ya le diste a esa coordenada")
          else:
            jugador_2[adivina_fila - 1][adivina_columna - 1] = "/"
            print("Aguaaaa")
        #chequear_si_destrui_barco(jugador_2,horizontal_2)
        #chequear_si_destrui_barco(jugador_2,vertical_2)
        juego_terminado = chequear_si_gana(jugador_2,juego_terminado)
        mostrar_tablero(jugador_2,tamanio_tablero)
        print("\n")
        turnos+=1
      else:
        print("Turno de las fuerzas británicas!")
        adivina_fila = validate_data("Ingrese fila: ", int, 1, tamanio_tablero)
        adivina_columna = validate_data("Ingrese columna: ", int, 1, tamanio_tablero)
        if jugador_1[adivina_fila-1][adivina_columna-1] == 1 or 2 or 3 or 4 or 5:
          jugador_1[adivina_fila-1][adivina_columna-1] = "X"
          print("Le pegaste al barco")
        else:
          if jugador_1[adivina_fila-1][adivina_columna-1] == "X" or jugador_1[adivina_fila-1][adivina_columna-1] == "/":
            print("Ya le diste a esa coordenada")
          else:
            jugador_1[adivina_fila - 1][adivina_columna - 1] = "/"
            print("Aguaaaa")
        #chequear_si_destrui_barco(jugador_1,horizontal_1)
        #chequear_si_destrui_barco(jugador_1,vertical_1)
        juego_terminado = chequear_si_gana(jugador_1,juego_terminado)
        mostrar_tablero(jugador_1,tamanio_tablero)
        print("\n")
        turnos+=1
    else:
      if turnos%2==1:
        print("Turno de las fuerzas británicas!")
        adivina_fila = validate_data("Ingrese fila: ", int, 1, tamanio_tablero)
        adivina_columna = validate_data("Ingrese columna: ", int, 1, tamanio_tablero)
        if jugador_2[adivina_fila-1][adivina_columna-1] == 1 or 2 or 3 or 4 or 5:
          jugador_2[adivina_fila-1][adivina_columna-1] = "X"
          print("Le pegaste al barco")
        else:
          if jugador_2[adivina_fila-1][adivina_columna-1] == "X" or jugador_2[adivina_fila-1][adivina_columna-1] == "/":
            print("Ya le diste a esa coordenada")
          else:
            jugador_2[adivina_fila - 1][adivina_columna - 1] = "/"
            print("Aguaaaa")
        #chequear_si_destrui_barco(jugador_2,horizontal_2)
        #chequear_si_destrui_barco(jugador_2,vertical_2)
        juego_terminado = chequear_si_gana(jugador_2, juego_terminado)
        mostrar_tablero(jugador_2,tamanio_tablero)
        print("\n")
        turnos+=1
      else:
        print("Turno para Sandokan y sus amigos!")
        adivina_fila = validate_data("Ingrese fila: ", int, 1, tamanio_tablero)
        adivina_columna = validate_data("Ingrese columna: ", int, 1, tamanio_tablero)
        if jugador_1[adivina_fila-1][adivina_columna-1] == 1 or 2 or 3 or 4 or 5:
          jugador_1[adivina_fila-1][adivina_columna-1] = "X"
          print("Le pegaste al barco")
        else:
          if jugador_1[adivina_fila-1][adivina_columna-1] == "X" or jugador_1[adivina_fila-1][adivina_columna-1] == "/":
            print("Ya le diste a esa coordenada")
          else:
            jugador_1[adivina_fila - 1][adivina_columna - 1] = "/"
            print("Aguaaaa")
        #chequear_si_destrui_barco(jugador_1,horizontal_1)
        #chequear_si_destrui_barco(jugador_1,vertical_1)
        juego_terminado = chequear_si_gana(jugador_1, juego_terminado)
        mostrar_tablero(jugador_1,tamanio_tablero)
        print("\n")
        turnos+=1

def elegir_jugador(tablero_1,tablero_2,eleccion,tamanio_tablero):
  if eleccion == 1:
    jugador_1 = generar_tablero(tablero_1, tamanio_tablero)
    jugador_1,horizontal_sandokan,vertical_sandokan = asignar_aleatoriamente(jugador_1,barcos_horizontales_sandokan, barcos_verticales_sandokan,tamanio_tablero,barcos_horizontales_sandokan_simbolo,barcos_verticales_sandokan_simbolo)
    jugador_2 = generar_tablero(tablero_2, tamanio_tablero)
    jugador_2, horizontal_armada, vertical_armada = asignar_aleatoriamente(jugador_2,barcos_horizontales_armada, barcos_verticales_armada,tamanio_tablero,barcos_horizontales_armada_simbolo,barcos_verticales_armada_simbolo)
  else:
    jugador_1 = generar_tablero(tablero_1, tamanio_tablero)
    jugador_1, horizontal_armada,vertical_armada = asignar_aleatoriamente(jugador_1,barcos_horizontales_armada, barcos_verticales_armada,tamanio_tablero,barcos_horizontales_armada_simbolo,barcos_verticales_armada_simbolo)
    jugador_2 = generar_tablero(tablero_2, tamanio_tablero)
    jugador_2, horizontal_sandokan,vertical_sandokan = asignar_aleatoriamente(jugador_1,barcos_horizontales_sandokan, barcos_verticales_sandokan,tamanio_tablero,barcos_horizontales_sandokan_simbolo,barcos_verticales_sandokan_simbolo)
  return jugador_1,jugador_2,horizontal_sandokan,vertical_sandokan,horizontal_armada,vertical_armada

def chequear_si_gana(matriz,flag):
  count = 0
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if matriz[i][j] == 1 or 2 or 3 or 4 or 5:
        count+=1
      else:
        count+=0
  if count > 0:
    flag = False
  else:
    flag = True
  return flag



def probabilidad(P):
  aleatorio = random.randint(0, 1)
  if aleatorio <= float(P) * 1:
    return True
  else:
    return False


def guardar_coordenada(n, abc):
  coord_y = input(('\n Elija una coordenada Y para bombardear\n '))
  coord_y = val_int(n, coord_y)
  coord_x = input(("\n Elija una coordenada X para bombardear (En letra)\n ")).upper()
  coord_x = int(val_abc(abc, coord_x, n))
  XY = [coord_x, coord_y]
  return XY
'''
def chequear_si_destrui_barco(matriz,ubicaciones):
  valor_a_chequear = "X"
  print(ubicaciones)
  for i in range(len(ubicaciones)-1):
    count=0
    for j in range(len(ubicaciones[i])-1):
      print(ubicaciones[i][j])
      for k in range(len(ubicaciones[i][j])-1):
        if matriz[ubicaciones[i][j][k]][ubicaciones[i][j+1][k]-1] == valor_a_chequear:
          count+=1
          print(count)
          if count == len(ubicaciones[i][j])-1:
            print("Mataste uno!")
      print('\n')
'''
def main():
  print(welcome_message,"\n")
  comenzar = input('Escriba \'comenzar\' para empezar el juego: ')
  while (comenzar != str('comenzar')):
    comenzar = input('Escriba \'comenzar\' para arrancar:')
  eleccion = validate_data("\n\n¿Qué jugador quiere ser?\n1) Sandokan\n2) Armada Británica\n\n", int, 1, 2 )
  tipo_de_partida = validate_data("\n\n¿Qué tipo de partida querés jugar?\n1) Tradicional\n2) Robo de barcos\n\n", int, 1, 2 )
  tablero_1 = []
  tablero_2 = []

  tamanio_tablero = validate_data("\n\nIngrese un tamaño de tablero entre 10 y 24: ",int,10,24)

  tablero_1,tablero_2,horizontal_1,vertical_1, horizontal_2,vertical_2=elegir_jugador(tablero_1,tablero_2,eleccion,tamanio_tablero)

  juego_terminado = False
  jugar(eleccion,tablero_1, tablero_2, tamanio_tablero, juego_terminado,1,horizontal_1,vertical_1,horizontal_2,vertical_2)

main()