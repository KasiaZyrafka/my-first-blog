print ('witaj w swiecie')
a = input('ile wynosi a?')
print (a)
b = input('ile wynosi b?')
c = input('ile wynosi c?')
a = int(a)
b = int(b)
c = int(c)
delta = b * b - a * c * 4
print (delta)
print ('delta to:', delta)
if (delta == 0):
    print ('masz jedno miejsce zerowe')
elif delta > 0:
    print ('masz dwa miejsca zerowe')
else:
    print ('nie ma miejsc zerowych ')

