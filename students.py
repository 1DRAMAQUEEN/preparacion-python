print("""
***********ESTUDIANTES***********
  1-Mostrar lista de estudiantes.
  2-Mostrar promedios.  
  3-Salir.    
*********************************   """) 
datos=[{
    "nombre": "Romina",
    "edad": "23",
    "rut": "20282364-5",
    "notas": [6.7, 6.6, 6.6]
    },
    {"nombre": "Tiare",
    "edad": "24",
    "rut": "20452650-8",
    "notas": [6.2, 6.4, 6.7]
    },
    { 
    "nombre": "Kristel",
    "edad": "21",
    "rut": "21336348-6",
    "notas": [6.4, 4.3, 6.5]
    }]


opcion_usuario = 0
while (opcion_usuario!=3):
    opcion_usuario= int(input("Ingresa tu opción con número: "))
    if (opcion_usuario== 1):
        print ("Esta es la  lista de estudiantes:")
        for dato in datos:
            print(f"El nombre de la estudiante es  {dato['nombre']} y su rut es {dato['rut']}")

    elif (opcion_usuario == 2):
        print("Estos son los promedios... ")
        for dato in datos:
            lista_notas=dato['notas']
            suma=0
            for nota in lista_notas:
                suma=suma+nota
            promedio = suma/len(lista_notas)
            promedio_aprox = round(promedio,1)
            #round es para quitrar decimales y decidir cuantos mostar#
            
            print(f"EL ESTUDIANTE {dato['nombre']} OBTUVO EL PROMEDIO DE {promedio_aprox}")

    else: 
        print ("Gracias por usar la aplicación...")







