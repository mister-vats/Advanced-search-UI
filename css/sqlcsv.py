import csv

sql_output = open('crm-dump-data.csv', mode='w')
# csv.register_dialect('myDialect', delimiter = ',', lineterminator = '\r\n\r\n')

with open('crm-dump-data.txt', 'r') as f:
    rows = []
    writer = csv.writer(sql_output)
    for index, line in enumerate(f.readlines()):
       
        if line[0] is '+':
            continue
        elif line is not '':
            line_arr = line[1 : -1].split('|')
            temp = []
            for item in line_arr:
                 temp.append(item.strip())
            writer.writerow(temp)
            continue
    print(temp)