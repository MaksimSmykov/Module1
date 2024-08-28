my_dict = {'Maksim': 1996, 'Egor': 1999, 'Masha': 2002}
print('My dictionary:',my_dict)
print('Existing value:',my_dict.get('Maksim'))
print('Not existing value:',my_dict.get('Mahsa'))
print('Not existing value:',my_dict.get('Mahsa','Такого ключа нет'))
my_dict.update({'Alex':1996,'Katya':2005})
my_dict['Masha'] = 2001
deleted_value = my_dict.pop('Egor')
print('Deleted value:',deleted_value)
print('Modified dictionary:',my_dict)
print('\n')
my_set = {1,'Яблоко',True,5,7,1,5,'Яблоко','Груша',False,(4,6,8)}
print('My set:',my_set)
my_set.add(0.5)
my_set.add(5.6)
my_set.discard((4,6,8))
my_set.remove('Груша')
print('Modified set:',my_set)