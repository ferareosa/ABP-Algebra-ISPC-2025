### Validaciones

def validar_entrada_usuario(mensaje: str, tipo=float, min_val=None, max_val=None):
    """
    Valida la entrada del usuario con manejo de errores
    """
    while True:
        try:
            entrada = input(mensaje)
            
            if not entrada:
                print("⚠️  Entrada vacía. Intente nuevamente.")
                continue
                
            if tipo == float:
                valor = float(entrada)
            elif tipo == int:
                valor = int(entrada)
            else:
                valor = entrada
                
            if min_val is not None and valor < min_val:
                print(f"⚠️  El valor debe ser mayor o igual a {min_val}")
                continue
                
            if max_val is not None and valor > max_val:
                print(f"⚠️  El valor debe ser menor o igual a {max_val}")
                continue
                
            return valor
            
        except ValueError:
            print(f"❌ Error: Por favor ingrese un número válido ({tipo.__name__})")
        except KeyboardInterrupt:
            print("\n\n⚠️  Entrada cancelada por el usuario")
            return None
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            return None