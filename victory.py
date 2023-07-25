peoples = {'Пушкин': 1799, 'Ленин': 1870, 'Сталин': 1878, 'Ельцин': 1931, 'Путин': 1952}

def print_result(count_correct_answers, count_error_answers, number_questions):
    print("--------- RESULTS----------", end='\n')
    print(f"Количество верных ответов: {count_correct_answers}")
    print(f"Количество не верных ответов: {count_error_answers}")
    print(f"Процент правильных ответов: {count_correct_answers / number_questions * 100} %")
    print(f"Процент не правильных ответов: {count_error_answers / number_questions * 100} %")

def game(dictionary):
    count_errors = 0
    count_correct = 0
    for key in dictionary:
        answer = int(input(f'Введите год рождения {key}: '))
        if answer == dictionary[key]:
            count_correct += 1
        else:
            count_errors += 1
    print_result(count_correct, count_errors, len(dictionary))

game(peoples)

