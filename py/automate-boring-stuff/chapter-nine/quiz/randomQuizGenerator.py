#! python3
# randomQuizGenerator.py -- Tworzy quiz wraz z pytaniami i odpowiedziami
# ułożonymi w losowej kolejności wraz z odpowiedziami.abs

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'Kalifornia': 'Sacramento', 'Kolorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Floryda': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaje': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
            'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Luizjana': 'Baton Rouge',
            'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'Nowy Meksyk': 'Santa Fe', 'Nowy Jork': 'Albany', 'Karolina Północna': 'Raleigh',
            'Dakota Północna': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pensylwania': 'Harrisburg', 'Rhode Island': 'Providence',
            'Karolina Południowa': 'Columbia', 'Dakota Południowa': 'Pierre',
            'Tennessee': 'Nashville', 'Teksas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Wirginia': 'Richmond', 'Waszyngton': 'Olympia',
            'Wirginia Zachodnia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Wygenerowanie 35 plików quizu.
for quizNum in range(35):
    # Utworzenie plików quizu i odpowiedzi na pytania.
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

    # Zapis nagłówka quizu.
    quizFile.write('Imię i nazwisko:\n\nData:\n\nKlasa:\n\n')
    quizFile.write((' ' * 20) + f'Quiz stolic stanów (Quiz {quizNum + 1})')
    quizFile.write('\n\n')

    # Losowe ustalenie kolejności stanów.
    states = list(capitals.keys())
    random.shuffle(states)

    # Iteracja przez 50 stanów i utworzenie pytania dotyczącego każdego z nich.
    for questionNum in range(50):

        # Przygotowanie prawidłowych i niprawidłowych odpowiedzi.
        correctAnswers = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswers)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswers]
        random.shuffle(answerOptions)

        # Zapis pytania i odpowiedzi w pliku quizu.
        quizFile.write(
            f'{questionNum + 1}. Co jest stolicą stanu {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"{'ABCD'[i]}. {answerOptions[i]}\n")
        quizFile.write('\n')

        # Zapis odpowiedzi w pliku.
        answerKeyFile.write(
            f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswers)]} \n")
    quizFile.close()
    answerKeyFile.close()
