with open('input.txt', 'r', encoding='utf-8') as f:
    all_lines = f.readlines()
    with open('output.txt', 'w', encoding='utf-8') as fi:
        for line in all_lines:
            new_line = line.upper()
            fi.write(new_line)











































