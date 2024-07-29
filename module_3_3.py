def print_params( a = 1, b = 'строка', c = True ):
    print(a, b, c)
print_params()
print_params('war')
print_params(6, 's')
print_params('x', 47, False )
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [4, 'mafia', True]
values_dict = {'a': 'nigga', 'b': 7, 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['gangsta', 40]
print_params(*values_list_2, 42)








