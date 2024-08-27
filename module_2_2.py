first = input ( 'Введите значение 1: ' )
second = input ( 'Введите значение 2 : ' )
third = input ( 'Введите значение 3: ' )
if first == second and first == third and second == third :
    print( ' 3 ')
elif first == second and first == third or second == first :
    print( ' 2 ')
elif first != second and first != third and second != third :
    print ( ' 0 ')

