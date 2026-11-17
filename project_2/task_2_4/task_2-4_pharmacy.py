total = int(input("Общее количество капсул: "))
pack_size = int(input("Количество капсул в одной упаковке: "))
full_packs = total // pack_size
remain = total % pack_size
print(f"Полных упаковок:\t{full_packs}")
print(f"Остаток:\t\t{remain}")