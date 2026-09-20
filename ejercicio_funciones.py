# Función con parámetros y retorno
def calcular_total_productos(producto1, producto2, producto3):
    
    suma = producto1 + producto2 + producto3
    return suma


# Bloque principal del programa
if __name__ == "__main__":

    # Valores de los productos o datos de entrada
    p1 = 32.00
    p2 = 24.50
    p3 = 16.50

    # Llamada a la función
    resultado = calcular_total_productos(p1, p2, p3)

    # Salida de datos
    print(f"Costo total de los productos: {resultado:.2f} euros")
    