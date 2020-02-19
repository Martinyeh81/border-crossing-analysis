import csv
import math
from operator import itemgetter
from itertools import groupby


def round(number):

    f = math.floor(number)
    return f if number - f < 0.5 else f+1

def outpot_csv(output_file, final_list):
    with open(output_file, mode='w') as csv_outfile:
        outfile_writer = csv.writer(csv_outfile, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_NONE)

        # column headers
        outfile_writer.writerow(['Border', 'Date', 'Measure', 'Value', 'Average'])

        outfile_writer = csv.writer(csv_outfile, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)

        #add the list
        for row in final_list:
            outfile_writer.writerow(row)

#read.csv
with open('sample.csv',newline='') as csv_file:
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

    data2 = []
    for row in data1:
        data2.append(row)

    #remove column headers
    del (data2[0])

    data2[0] = data2 [0] + [0]
    for i in range(len(data2)-1,0,-1):
        if data2[i][2] != data2[i-1][2]:
            accumulation, counter = 0, 0
            data2[i] = data2[i] + [0]

        elif data2[i][2] == data2[i-1][2] == data2[i-2][2]:
            # Add the previous months' values

            accumulation = data2[i-1][3] + data2[i-2][3]

            # counter of month

            counter = (int(data2[i][1][0:2])-1) + (int(data2[i][1][6:10])-int(data2[i-1][1][6:10]))*12

            # average
            data2[i] = data2[i] + [round(accumulation/counter)]

        elif data2[i][2] == data2[i-1][2] != data2[i-2][2]:

            data2[i] = data2[i] + [data2[i-1][3]]


    sorted_data = sorted(data2, key=itemgetter(1,3,2,0),reverse=True)

outpot_csv('report.csv', sorted_data)










