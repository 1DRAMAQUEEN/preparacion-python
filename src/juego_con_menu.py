#print("Bienvenido al juego, elige alguna de estas opciones
#    1-JUGAR 2-VER RESULTADOS 3-REINICIAR PUNTAJE 4-SALIR)

print("""
***********BIENVENIDO AL JUEGO*********
*            Eligue una opción:        *
*            1-JUGAR.                  *
*            2-VER RESULTADOS.         *
*            3-REINICIAR PUNTAJE.      *
*            4-SALIR.                  *
***************************************
""")
jugador = 0
while (jugador != "4"):
    jugador = input("Ingresa tu opción con número: ")

    if(jugador == "1"):
        print("VAMOS A JUGAR...")
        import random
        compute = random.choice(["papel","piedra","tijeras"])
        usuario = input("Escoje solo una de estás opciones : Piedra, Papel o Tijeras : (si quieres dejar de jugar escribe : salir)").lower().strip()

        puntaje = "0"
        cantidadesGanadas = "0"
        cantidadesPerdidas = "0"
        CantidadGanadaUsuario = "0"
        if (usuario == compute):
            print("¡Empate!")
        if (usuario == "tijeras" and compute == "papel"):
            print("¡Ganaste!")
            puntaje = puntaje + 10
            cantidadesGanadas = cantidadesGanadas + 1
        if (usuario == "papel" and compute == "piedra"):
            print ("¡Ganaste!")
            puntaje = puntaje + 10
            cantidadesGanadas = cantidadesGanadas + 1
        if (usuario == "piedra" and compute == "tijeras"):
            print("¡Ganaste!")
            puntaje = puntaje + "10"
            cantidadesGanadas = cantidadesGanadas + 1
        if (usuario == "tijeras" and compute == "piedra"):
            print("¡Perdiste!")
            puntaje = puntaje - 10
            cantidadesPerdidas = cantidadesPerdidas + 1
        if (usuario == "piedra" and compute == "papel"):
            print("¡Perdiste!")
            puntaje = puntaje - 10
            cantidadesPerdidas = cantidadesPerdidas + 1
        if (usuario == "papel" and compute == "tijeras"):
            print("¡Perdiste!")
            puntaje = puntaje - 10
            cantidadesPerdidas = cantidadesPerdidas + 1
        print(f"obtuviste {puntaje} puntos")
        mensajeFinal = f"""
    --------------------------------------------------------------|
                PUNTAJE FINAL :                                   |
    --------------------------------------------------------------|
            ganaste         |        {cantidadesGanadas}          |
    --------------------------------------------------------------|
            perdiste        |        {cantidadesPerdidas}         |
    --------------------------------------------------------------|
            puntaje         |        {puntaje}                    |
    --------------------------------------------------------------|
    """
        print (mensajeFinal)
    

    if(jugador == "2"):
        print("ESTOS SON LOS RESULTADOS...")
    if(jugador == "3"):
        print("VAMOS A REINICIAR EL JUEGO...")
    if(jugador == "4"):
        print("HASTA LUEGO, GRACIAS POR JUGAR.")














