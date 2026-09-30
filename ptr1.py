pin_correcto = "1234"
intentos_maximos = 3
intentos_usados = 0
saldo_disponible = 5000.0  

while intentos_usados < intentos_maximos:
    pin_ingresado = input("Introduzca su PIN: ")
    
    if pin_ingresado == pin_correcto:
        print("¡Acceso concedido! Bienvenido a FintechBank.")
        
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Consultar Saldo")
            print("2. Retirar Dinero")
            print("3. Salir")
            
            opcion = input("Seleccione una opción (1-3): ")
            
            if opcion == "1":
                print(f"💰 Su saldo disponible es: ${saldo_disponible}")
                
            elif opcion == "2":
                monto_a_retirar = float(input("¿Cuánto dinero desea retirar?: $"))
                if monto_a_retirar <= saldo_disponible:
                    saldo_disponible = saldo_disponible - monto_a_retirar
                    print("💸 Retiro exitoso. Por favor, retire su dinero.")
                else:
                    print("❌ Error: Fondos insuficientes.")
                    
            elif opcion == "3":
                print("👋 Gracias por usar FintechBank. ¡Vuelva pronto!")
                break 
                
            else:
                print("⚠️ Opción inválida. Intente de nuevo.")
                
        break 
        
    else:
        intentos_usados = intentos_usados + 1
        intentos_restantes = intentos_maximos - intentos_usados
        print(f"PIN incorrecto. Te quedan {intentos_restantes} intentos.")

if intentos_usados == intentos_maximos:
    print("❌ Cuenta bloqueada. Por seguridad, retendremos su tarjeta.")
