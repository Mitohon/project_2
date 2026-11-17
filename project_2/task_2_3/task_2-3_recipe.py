nutrient_medium = input("Название питательной среды: ")
agar_concentration = int(input("Концентрация агара (%): "))
sterilization_temp = int(input("Температура стерилизации (°C): "))

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"{nutrient_medium}\n")
    file.write(f"- Концентрация агара: {agar_concentration}%\n")
    file.write(f"- Температура стерилизации: {sterilization_temp}°C\n")
print("Файл 'recipe.txt' успешно сформирован!")