n1 = float(input('Numero um: '))
n2 = float(input('Numero dois: '))
n3 = float(input('Numero três: '))

if n1 > n2 and n1 > n3:
    print('O maior numero é o: ',n1)
elif n2 > n1 and n2 > n3:
    print('O maior numero é o: ',n2)
elif n3 > n1 and n3 > n2:
    print('O maior numero é o: ',n3)