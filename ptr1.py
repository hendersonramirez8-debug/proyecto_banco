pin_correcto = "1234"
intentos_maximos = 3
intentos_usados = 0

while intentos_usados < intentos_maximos:
    pin_ingresado = input("Introduzca su PIN:")

    if pin_ingresado == pin_correcto:
        print("¡Acceso concedido! Bienvenido a Fintechbank.")
        break
    else:
        intentos_usados = intentos_usados + 1
        intentos_restantes = intentos_maximos - intentos_usados
        print(f"PIN incorrecto. Te quedan {intentos_restantes} intentos.")
if intentos_usados == intentos_maximos:
    print("x Cuenta bloqueada. Por seguridad, retendremos su tarjeta.")

