# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

S = int(input('Напишите сумму загаданых чисел: '))
P = int(input('Напишите произведение данных чисел: '))
for a in range(S):
    b = S - a
    a = S - b
    if (a * b == P):
        print(f'Числа, которые вы загадили, это {a} и {b}.')
        break
    else:
        if (b == 1):
            print('Перепроверьте Ваши данные.')