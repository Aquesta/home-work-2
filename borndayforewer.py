## modul 5
born_year = 1799
born_day = 26

while True:
    answer_year = int(input("Введите год рождения А.С. Пушкина: "))
    if answer_year == born_year:
        break
    print("Не верно")

while True:
    answer_day = int(input("Введите день рождения А.С. Пушкина: "))
    if answer_day == born_day:
        break
    print("Не верно")

print("Верно")