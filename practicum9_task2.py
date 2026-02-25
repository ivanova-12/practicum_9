with open('input.txt', 'w+', encoding='utf-8') as f:
    while True:
        s = input()
        f.write(s + '\n')
        if s == '':
            break
    f.seek(0)
    new_lines = []
    for line in f:
        if line[0] == 'a' or line[0] == 'A':
            new_lines.append(line.strip() + '\n')

with open('output.txt', 'w', encoding='utf-8') as fi:
    fi.writelines(new_lines)












































