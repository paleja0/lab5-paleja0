def promedio_estudiante(calificaciones):
    if not calificaciones:
        return 0.0
    suma_total = sum(calificaciones)
    cantidad = len(calificaciones)
    promedio = float(suma_total / cantidad)
    
    return promedio