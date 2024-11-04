print('Canção: Um Elefante Incomoda Muita Gente.\n')

for i in range(1, 11):
    if i % 2 == 1:
        if i == 1:
            print(f'{i} elefante incomoda muita gente')
        else:
            print(f'{i} elefantes incomodam muita gente')
    else:
        msg = f'{i} elefantes'
        for j in range(1, i + 1):
            msg += ' incomodam'
        msg += ' muito mais!'
        if i in (4, 8):
            msg += '\n'
        print(msg)
print()
for i in range(10, 0, -1):
    if i % 2 == 0:
        print(f'{i} elefantes incomodam muita gente')
    else:
        if i == 1:
            msg = f'{i} elefante incomoda'
        else:
            msg = f'{i} elefantes'
            for j in range(1, i + 1):
                msg += ' incomodam'
        msg += ' muito menos!'
        if i == 7:
            msg += '\n'
        print(msg)
print()