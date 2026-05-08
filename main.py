from temperature import is_overheating

def run_monitor():
    print("--- Sistema de Monitoreo de Temperatura ---")
    
    try:
        # Aquí es donde validamos la entrada del usuario
        entrada = input("Ingrese la temperatura actual en °C: ")
        temp = float(entrada) 
        
        # Si llega aquí, es porque es un número. Ahora revisamos la lógica.
        if is_overheating(temp):
            print("¡ALERTA! El sistema está recalentado.")
        else:
            print("Temperatura normal.")
            
    except ValueError:
        # Si el usuario escribió letras, el float() falla y salta aquí
        print("ERROR: Entrada inválida. Por favor, ingrese solo números (ej: 25.5).")

if __name__ == "__main__":
    run_monitor()