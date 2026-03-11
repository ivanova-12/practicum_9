with open('input.txt', 'r', encoding='utf-8') as f:
    all_numbers = f.readlines()
    for num in all_numbers:
        if int(num) == 100:
            all_numbers.remove(num)
        with open('input.txt', 'w', encoding='utf-8') as f:
            for num in all_numbers:
                f.write(num)




