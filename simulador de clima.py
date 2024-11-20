import random

diaspredi = int(input("Introduce el número de días para la predicción: "))
tempinicial = int(input("Introduce la temperatura inicial: "))
problluviainicial = int(input("Introduce la probabilidad inicial de lluvia: "))

def clima(dias, tempinicial, problluviainicial):
    temperatura = tempinicial
    problluvia = problluviainicial
    diaslluv = 0
    tempmax = temperatura
    tempmin = temperatura
    for dia in range(1, dias + 1):
        print(f"\nDía {dia}:") 
        if random.random() < 0.1:
            cambio = random.choice([-2, 2])
            temperatura += cambio
            print(f"La temperatura cambió {cambio} grados.")
        if temperatura > 25:
            problluvia = min(problluvia + 20, 100)
            print("La temperatura es superior a 25 grados, la probabilidad de lluvia aumentó un 20%")
        if temperatura < 5:
            problluvia = max(problluvia - 20, 0)
            print("La temperatura es inferior a 5 grados, la probabilidad de lluvia disminuyó un 20%")
        llueve = random.randint(1, 100) <= problluvia
        if llueve:
            diaslluv += 1
            temperatura -= 1
            print("Está lloviendo. La temperatura baja 1 grado")
        print(f"Temperatura actual: {temperatura}°C, Probabilidad de lluvia: {problluvia}%")
        tempmax = max(tempmax, temperatura)
        tempmin = min(tempmin, temperatura)
    print("\nResumen:")
    print(f"Temperatura máxima: {tempmax}°C")
    print(f"Temperatura mínima: {tempmin}°C")
    print(f"Días con lluvia: {diaslluv} de {dias}")

clima(diaspredi, tempinicial, problluviainicial)
