import random

words = ["предмет","азбука","окулист","арбуз","лесник","яблоко","гений","ян","щавель","список"]
session = 0

while True:
    session += 1
    #print("Debug: Session {}".format(session))
    word = random.choice(words)
    #print("Debug: randomed word \"{}\"".format(word))
    letters = [*word]
    solved = []
    for l in letters:
        solved += "-"
    #print("Debug: " + str(solved))
    attempts = 6
    while True:
        print(" ".join(solved))
        usr_letter = input("У вас осталось {} попыток. Введите букву/слово: ".format(attempts)).lower()
        lett = 0
        matched = False
        for l in letters:
            if usr_letter == l:
                solved[lett] = usr_letter
                matched = True
                lett += 1
            else:
                lett += 1
        if usr_letter == word:
            print("Да, это правильно. начинается новая сессия...")
            break
        if matched == False:
            attempts -= 1
        if attempts == 0:
            print("Сожалеем, вы проиграли! Это было слово \"{}\" Начинается новая сессия!".format(word))
            break
        if "-" in solved:
            pass
        else:
            print("Поздравляем! Вы выиграли всего с {} ошибками. Запуск новой сессии...".format(6-attempts))
            break