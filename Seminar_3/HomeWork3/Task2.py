from operator import itemgetter

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.

MAX_VALUE = 10

s = "Средний срок жизни кошек составляет 14 лет. Вместе с тем, известен случай, когда кошка по кличке Крим Пафф " \
    "дожила до 38 лет. На январь 2011 года самой старой считалась кошка Люси. Она жила в британской семье и отметила " \
    "своё 39-летие. Как рассказал владелец животного Билл Томас, кошка появилась на свет в 1972 году. Представители " \
    "Книги рекордов Гиннесса официально признали, что кошка Люси — самая старая представительница своего вида в мире." \
    "Кастрация котов и стерилизация кошек благоприятно сказывается на их здоровье, так как у котов-кастратов не может" \
    "развиться рак семенников, а у стерильных кошек — рак матки или рак яичников, кроме того и у котов и у кошек " \
    "снижается риск заболевания раком молочных желёз. Стерилизация кошек до первой течки является профилактикой рака " \
    "молочной железы. Однако кастрированные коты часто страдают мочекаменной болезнью и подвержены ожирению. " \
    "Ранняя кастрация (в возрасте меньше 8—9 месяцев) может приводить к развитию мочекаменной болезни."

word_list = s.split()

word_dict = {}
for el in word_list:
    if el.isalpha():
        word_dict.setdefault(el, word_list.count(el))

sorted_word_dict = sorted(word_dict.items(), key=itemgetter(1), reverse=True)

for i in range(MAX_VALUE):
    print("Слово '", sorted_word_dict[i][0], "' повторяется", sorted_word_dict[i][1], "раз(а)")