with open('input.txt', 'r', encoding='utf-8') as f:
    all_lines = f.readlines()
    end = ''
    for line in all_lines:
        end += line[0]

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(end)















































