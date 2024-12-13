numbers = [2,3,4,2,5,5,4,3,5,4]

for x in numbers:
    carroX = numbers[x] + numbers[x+1]
    carroY = numbers[x+2] + numbers[x+3]
    x = 0
print(carroX)
print(carroY)

if carroX > carroY:
    print("Carro X ganador")
else:
    print("Carro Y ganador")