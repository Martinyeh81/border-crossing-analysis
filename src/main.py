import csv
import math
from operator import itemgetter
from itertools import groupby
from datetime import datetime

def outpot_csv(output_file, final_data):
    with open(output_file, mode='w') as csv_outfile:
        outfile_writer = csv.writer(csv_outfile, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_NONE)

        # column headers
        outfile_writer.writerow(['Border', 'Date', 'Measure', 'Value', 'Average'])

        outfile_writer = csv.writer(csv_outfile, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)

        #add the list
        for row in final_data:
            outfile_writer.writerow(row)

#read.csv
with open('Border_Crossing_Entry_Data.csv',newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #descending the border measure date
    sorted_list = sorted(csv_reader, key=itemgetter(3, 5, 4))
    data1 = []
    #choose border date measure value
    for key, group in groupby(sorted_list, key=lambda x: x[3:6]):
        total_value = []
        for row in group:
            if row[6].isdigit() and row[6] != 0:
                total_value.append(int(row[6]))
        # sum the value
        data1.append(key + [sum(total_value)])

    # remove column headers
    del (data1[0])

    # add average and count
    data2 = []
    for row in data1:
        row = row + [0] + [0]
        data2.append(row)


    #datetime
    data3 = []
    for row in data2:
        data3.append(datetime.strptime(row[1], '%m/%d/%Y %I:%M:%S %p'))


    for key in range(len(data3)):
        for key1 in range(len(data3)):
            if key != key1:
                date1 = data3[key]
                date2 = data3[key1]
                if date1 > date2 and data2[key][2] == data2[key1][2]:
                    data2[key][4] += data2[key1][3] #total
                    data2[key][5] += 1  #count


    final_data = []
    for key in range(len(data2)):
        if data2[key][5] != 0:
            final_data.append([data2[key][0], data2[key][1], data2[key][2], data2[key][3],
                               math.ceil(data2[key][4] / data2[key][5])])
        else:
            final_data.append([data2[key][0], data2[key][1], data2[key][2], data2[key][3], 0])


    sorted_data = sorted(final_data, key=itemgetter(1,3,2,0),reverse=True)


outpot_csv('report.csv', sorted_data)










