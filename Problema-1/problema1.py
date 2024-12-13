numbers = [2,3,4,2,5,5,4,3,5,4,2,4]

PRIMERA_CARRERA_X = numbers[0] + numbers[1]
PRIMERA_CARRERA_Y = numbers[2] + numbers[3]

for x in numbers:
    SEGUNDA_CARRERA_X = numbers[x] + numbers[x+1]
    SEGUNDA_CARRERA_Y = numbers[x+2] + numbers[x+3]

print(PRIMERA_CARRERA_X)
print(PRIMERA_CARRERA_Y)
print(SEGUNDA_CARRERA_X)
print(SEGUNDA_CARRERA_Y)

if PRIMERA_CARRERA_X  > PRIMERA_CARRERA_Y:
    print("Carro X ganador")
else:
    print("Carro Y ganador")

if SEGUNDA_CARRERA_X  > SEGUNDA_CARRERA_Y:
    print("Carro X ganador")
else:
    print("Carro Y ganador")
