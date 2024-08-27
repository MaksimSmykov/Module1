immutable_var = (1, 2, [3, 4], 'String1', True)
print('Immutable tuple:', immutable_var)
print(immutable_var[2])
#immutable_var[1] = 2.5 - не сработает, т.к. это кортеж, поэтому закомментировано
immutable_var[2][0] = 3.5
print(immutable_var)
immutable_var = immutable_var*2
print(immutable_var)
print('\n')
mutable_list = [5, 6, [7, 8], 'String2', False]
print('Mutable list:',mutable_list)
mutable_list[0] = [4, 5]
mutable_list[2] = 78
print('Mutable list:', mutable_list)
mutable_list.append(5.5)
print('Mutable list:', mutable_list)
mutable_list.extend('Hi')
print('Mutable list:', mutable_list)
mutable_list.extend(['Hi', 'Urban'])
print('Mutable list:', mutable_list)
print('Urban' in mutable_list)
print('hi' in mutable_list)
print('hi' not in mutable_list)
print(mutable_list[0:4],'\n',mutable_list[5:], '\n', mutable_list[1:10:3])