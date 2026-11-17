weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (см): "))
height_1 = height / 100
bmi = weight / (height_1 ** 2)
print("--- Отчет о состоянии здоровья ---")
print(f"Рост:\t\t{height} см")
print(f"Вес:\t\t{weight} кг")
print(f"Индекс массы тела: {bmi:.2f}")
