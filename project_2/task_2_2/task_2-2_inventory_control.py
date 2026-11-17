reagent_name = input("Название реактива: ")
quantity = int(input("Количество (в шт.): "))
report =  f"Реактив [{reagent_name}] поступил на склад в количестве [{quantity}] шт."
print (report)
with open("inventory.txt", "w", encoding="utf-8") as file:
    file.write(report)
