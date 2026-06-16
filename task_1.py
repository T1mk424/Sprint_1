times = '1h 45m,360s,25m,30m 120s,2h 60s'

total_sum = 0

for i in times.split(','):
    sum_of_part = 0
    for j in i.split():
        if 'h' in j:
            sum_of_part += 60*int(j.replace('h', ''))
        elif 'm' in j:
            sum_of_part += int(j.replace('m', ''))
        elif 's' in j:
            sum_of_part += int(j.replace('s', ''))/60
    total_sum += sum_of_part
print(int(total_sum))