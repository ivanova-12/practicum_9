with open('input.txt', 'w+', encoding='utf-8') as f:
    f.writelines(input())
    f.seek(0)
    new_lines = []
    for line in f:
        new_line = line.upper()
        new_lines.append(new_line)

with open('output.txt', 'w', encoding='utf-8') as fi:
    fi.writelines(new_lines)










































