import datetime

with open('input.txt', 'r', encoding='utf-8') as f:
    date_today = f.readline()
    date_today_d = (date_today.split('.'))[0]
    date_today_m = (date_today.split('.'))[1]
    end_date_today = datetime.datetime(2025, int(date_today_m), int(date_today_d))
    count_of_bags = int(f.readline())
    all_lines = f.readlines()
    with open('output.txt', 'w', encoding='utf-8') as fi:
        for line in all_lines:
            new_line = line.strip().split()
            date_this_bag_d = int((new_line[1].split('.'))[0])
            date_this_bag_m = int((new_line[1].split('.'))[1])
            end_date_bag = datetime.datetime(2025, int(date_this_bag_m), int(date_this_bag_d))
            interval = end_date_today - end_date_bag
            if interval.days > 3:
                print(new_line[0], file=fi)




