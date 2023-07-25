## modul 3
born_year = 1799
born_day = 26

answer_year = int(input("Введите год рождения А.С. Пушкина: "))

if answer_year == born_year:
    print("Верно")
    answer_day = int(input("Введите день рождения А.С. Пушкина: "))
    if answer_day == born_day:
        print("Верно")
    else:
        print("Неверно")
else:
    print("Неверно")

