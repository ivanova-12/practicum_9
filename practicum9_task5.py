with open('input.txt', 'w+', encoding='utf-8') as f:
    with open('output.txt', 'w+', encoding='utf-8') as fi:
        for i in range(3):
            s = input()
            f.write(s + '\n')
        cnt = 0
        ans = 0
        f.seek(0)
        for num in f:
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


