obiem = float(input("Объем раствора (в мл): "))
salt = obiem * 0.009
water = obiem
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: {obiem} мл\n")
    file.write(f"Масса соли: {salt:.2f} г\n")
    file.write(f"Объем воды: {water} мл\n")
