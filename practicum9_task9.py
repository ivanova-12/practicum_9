import os

os.makedirs('simple', exist_ok=True)
current_file_path = os.path.abspath('simple')
with open('input.txt', 'r', encoding='utf-8') as f:
    all_lines = f.readlines()
    with open(os.path.join(current_file_path, 'output.txt'), 'w', encoding='utf-8') as fi:
        for ind in range(len(all_lines)):
            if ind % 2 == 1:
                fi.write(all_lines[ind])

