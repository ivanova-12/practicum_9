with open('input.txt', 'r', encoding='utf-8') as f:
    all_lines = f.readlines()
    with open('output.txt', 'w+', encoding='utf-8') as fi:
        cnt = 0
        for num in all_lines:
            try:
                new_num = int(num)
                cnt += 1
            except ValueError:
                print('data error', file=fi)
                exit()
            if cnt == 1:
                ans = new_num
            elif cnt == 2:
                try:
                    ans /= new_num
                except ZeroDivisionError:
                    print('division by 0', file=fi)
                    exit()
            else:
                ans += new_num
                fi.write(str(ans))



