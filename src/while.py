contador= 0
while(contador<6): 
    contador= contador +1
    user_option=int(input(f"intento {contador} "))
    print(f"LLEVAS {contador} INTENTOS")

    if(user_option >=10):
        print(f"tu número es mayor a 10")
        break


