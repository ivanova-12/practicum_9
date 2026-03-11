with open('input.txt', 'r', encoding='utf-8') as f:
    number = f.readline()
    try:
        number = int(number)
    except ValueError:
        print('ERROR')
        exit()
    all_other_lines = f.readlines()
    with open('output.txt', 'w', encoding='utf-8') as fi:
        if len(all_other_lines) == number:
            fi.write('YES')
        else:
            fi.write('NO')




