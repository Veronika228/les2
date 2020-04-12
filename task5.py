
my_list = [7, 5, 3, 3, 2]
user_number = int(input('Введите рейтинг.\n'))

while True:
    if user_number >= my_list[0]:
        my_list.insert(0, int(user_number))
        print(my_list)
        break
    if user_number >= my_list[1]:
        my_list.insert(2, int(user_number))
        print(my_list)
        break
    if user_number >= my_list[2]:
        my_list.insert(4, int(user_number))
        print(my_list)
        break
    if user_number >= my_list[4]:
        my_list.insert(5, int(user_number))
        print(my_list)
        break
    if user_number < my_list[4]:
        my_list.insert(5, int(user_number))
        print(my_list)
        break
    else:
        my_list.insert(5, int(user_number))
        print(my_list)
        break
