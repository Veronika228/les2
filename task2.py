
var_list = ['1', '2', '3', '4', '5']


if len(var_list) % 2 == 0:
    i = 0
    while i < len(var_list):
        itm = var_list[i]
        var_list[i] = var_list[i + 1]
        var_list[i + 1] = itm
        i += 2
else:
    i = 0
    while i < len(var_list) - 1:
        itm = var_list[i]
        var_list[i] = var_list[i + 1]
        var_list[i + 1] = itm
        i += 2
print(var_list)
