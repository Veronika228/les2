
sentence = input('Введите строку из нескольх слов.\n')

for itm in enumerate(sentence.split(' ')):
    print(itm)
    if len(itm) > 10:
        itm = itm[0:10]

