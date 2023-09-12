import random, time

numberOfQuestions = 10
correctAnswers = 0
attemptNum = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    print('#%s: %s x %s = ' % (questionNumber+1, num1, num2))

    attemptNum = 0
    startTime = time.time()
    while attemptNum < 3:
        try:
            response = int(input())
            if time.time() - startTime > 8:
                print('Correct... but')
                break
            if response == (num1 * num2):
                print('Correct!')
                correctAnswers += 1
                time.sleep(1)
                break
            else:
                print('Incorrect!')
                attemptNum+=1
        except:
            print('Incorrect!')
            attemptNum += 1
        if time.time() - startTime > 8:
            break
    if response == (num1 * num2):
        continue
    if attemptNum == 3:
        print('Out of tries!')
        continue
    if time.time() - startTime > 8:
        print('Out of time!')
        continue
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))