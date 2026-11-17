file_path = r"C:\Users\maria\Kashlinova_MV\project_2\task_2_0\output.txt"
f = open(file_path, "w", encoding="utf-8")
print("Штирлиц вошёл в комнату, из окна дуло. Штирлиц закрыл окно, дуло исчезло.", file=f)
f.close()