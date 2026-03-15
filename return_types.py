def obtener_precio_usuario():
    precio = input("Enter the item's price:\n")
    precio = float(precio)
    return precio


# Ejemplo de uso
precio = obtener_precio_usuario()
print(precio)