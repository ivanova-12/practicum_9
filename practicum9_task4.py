with open('input.txt', 'r', encoding='utf-8') as f:
    all_lines = f.readlines()
    new_lines = []
    for line in all_lines:
        if len(line.rstrip()) > 20:
            new_lines.append(line.strip() + '\n')

with open('output.txt', 'w', encoding='utf-8') as fi:
    fi.writelines(new_lines)









































