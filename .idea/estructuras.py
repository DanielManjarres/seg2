

# Caso 1: Lista de Listas
notas_listas = [
    ["Calculo", 3.5, 2.5, 1.5],
    ["Química", 2.5, 3.0, 5.0],
    ["Deporte", 2.4, 2.0, 2.2],
    ["Lógica", 1.5, 4.0, 4.5]
]

def c11_final():
    for materia in notas_listas:
        # Calcular la nota final con ponderaciones 30%, 30%, 40%
        nota_final = materia[1] * 0.3 + materia[2] * 0.3 + materia[3] * 0.4
        materia.append(round(nota_final, 2))  # Agregar nota final a la lista

def c12_promedio():
    total = sum(materia[-1] for materia in notas_listas)
    promedio = total / len(notas_listas)
    return round(promedio, 2)

c11_final()
print("Caso 1: Lista de Listas")
print(notas_listas)
print(f"Promedio del estudiante: {c12_promedio()}")

# Caso 2: Diccionario de Listas
notas_dict_listas = {
    "Calculo": [3.5, 2.5, 1.5],
    "Química": [2.5, 3.0, 5.0],
    "Deporte": [2.4, 2.0, 2.2],
    "Lógica": [1.5, 4.0, 4.5]
}

def c21_final():
    for materia, notas in notas_dict_listas.items():
        nota_final = notas[0] * 0.3 + notas[1] * 0.3 + notas[2] * 0.4
        notas.append(round(nota_final, 2))  # Agregar nota final

def c22_promedio():
    total = sum(notas[-1] for notas in notas_dict_listas.values())
    promedio = total / len(notas_dict_listas)
    return round(promedio, 2)

c21_final()
print("\nCaso 2: Diccionario de Listas")
print(notas_dict_listas)
print(f"Promedio del estudiante: {c22_promedio()}")

# Caso 3: Diccionario de Diccionarios
notas_dict_dict = {
    "Calculo": {"pp": 3.5, "sp": 2.5, "tp": 1.5},
    "Química": {"pp": 2.5, "sp": 3.0, "tp": 5.0},
    "Deporte": {"pp": 2.4, "sp": 2.0, "tp": 2.2},
    "Lógica": {"pp": 1.5, "sp": 4.0, "tp": 4.5}
}

def c31_final():
    for materia, notas in notas_dict_dict.items():
        nota_final = notas["pp"] * 0.3 + notas["sp"] * 0.3 + notas["tp"] * 0.4
        notas["final"] = round(nota_final, 2)  # Agregar nota final al diccionario

def c32_promedio():
    total = sum(notas["final"] for notas in notas_dict_dict.values())
    promedio = total / len(notas_dict_dict)
    return round(promedio, 2)

c31_final()
print("\nCaso 3: Diccionario de Diccionarios")
print(notas_dict_dict)
print(f"Promedio del estudiante: {c32_promedio()}")
