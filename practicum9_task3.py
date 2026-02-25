with open('input.txt', 'w+', encoding='utf-8') as f:
    while True:
        s = input()
        f.write(s + '\n')
        if s == '':
            break
    f.seek(0)
    new_lines = []
    end = ''
    for line in f:
        end += line[0]

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(end)













































