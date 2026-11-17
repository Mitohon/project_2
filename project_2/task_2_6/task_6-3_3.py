donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите фенотип группы крови пациента (I, II, III, IV): ").strip().upper()
if donor == recipient or donor == "I" or donor == "1":
    print("Можно.")
else:
    print("Нельзя.")