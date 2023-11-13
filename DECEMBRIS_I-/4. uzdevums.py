
ievaditie_skaitli = int(input("Ievadi skaitli: "))
faktorials = 1
for skaitlis in range(1, ievaditie_skaitli + 1):
 faktorials *= skaitlis
print(f"Faktoriāls no {ievaditie_skaitli} ir: {faktorials}")