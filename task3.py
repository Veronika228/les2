number: int = input('Введите номер месяца.\n')

if number <= 12 and number >= 1:
    month_dict: {1: 'Январь',
                 2: 'Февраль',
                 3: 'Март',
                 4: 'Апрель',
                 5: 'Май',
                 6: 'Июнь',
                 7: 'Июль',
                 8: 'Август',
                 9: "Сентябрь",
                 10: 'Октябрь',
                 11: 'Ноябрь',
                 12: 'Декабрь',
                 }
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if el == number-1:
            print("Месяц из списка {month_list[i]}")
            break
    print("Месяц из кортежа {month_dict[i]}")
else:
    print("Вы сделали ошибку.")

