def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def estado_salud(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad grado 1"
    elif 35 <= imc < 40:
        return "Obesidad grado 2"
    else:
        return "Obesidad grado 3 (obesidad mórbida)"


for i in range(10):
    print(f"\nIngresando datos para la persona {i+1}:")
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    estatura = float(input("Ingresa tu estatura en metros: "))
    peso = float(input("Ingresa tu peso en kg: "))

    
    imc = calcular_imc(peso, estatura)

    
    estado = estado_salud(imc)
    print(f"\n--- Información de la persona {i+1} ---")
    print(f"Nombre completo: {nombre} {apellido}")
    print(f"Estatura: {estatura} metros")
    print(f"Peso: {peso} kg")
    print(f"Índice de masa corporal (IMC): {imc:.2f}")
    print(f"Estado de salud: {estado}")
