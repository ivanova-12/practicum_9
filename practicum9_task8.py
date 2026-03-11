with open('input.txt', 'r', encoding='utf-8') as f:
    all_days = f.readlines()
    num_of_31 = [1, 3, 5, 7, 8, 10, 12]
    with open('output.txt', 'w', encoding='utf-8') as fi:
        for cnt in range(1, 13):
            month = []
            if cnt in num_of_31:
                for day in all_days[:31]:
                    month.append(int(day))
                fi.write(str(sum(month)/len(month)) + '\n')
                all_days = all_days[31:]
            elif cnt not in num_of_31 and cnt != 2:
                for day in all_days[:30]:
                    month.append(int(day))
                fi.write(str(sum(month)/len(month)) + '\n')
                all_days = all_days[30:]
            else:
                if len(all_days) == 366:
                    for day in all_days[:29]:
                        month.append(int(day))
                    fi.write(str(sum(month)/len(month)) + '\n')
                    all_days = all_days[29:]
                else:
                    for day in all_days[:28]:
                        month.append(int(day))
                    fi.write(str(sum(month)/len(month)) + '\n')
                    all_days = all_days[28:]
