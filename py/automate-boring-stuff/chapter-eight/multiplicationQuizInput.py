import re
import random
import time

number_questions = 10
correct_answers = 0

for i in range(number_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    number_tries = 0
    while number_tries < 3:
        print('#%s: %s x %s = ' % (i, num1, num2), end='')
        question = re.compile(r'^%s$' % (num1 * num2))
        time_before_answer = time.time() # gets time since epoch before answer in secs
        answer = input()
        time_after_answer = time.time() # gets time since epoch after answer in secs
        if (time_after_answer - time_before_answer) > 8:
            print('Time is up!')
            break
        elif question.search(answer) != None:
            correct_answers += 1
            print('Good!')
            break
        else:
            number_tries += 1
            print('Incorrect answer!')

    if number_tries == 3:
        print('Too many tries!')
    time.sleep(1)

print('correct answers: %s/%s' % (correct_answers, number_questions))
