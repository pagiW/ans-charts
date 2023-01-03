import csv
with open('./WhatsgoodlyData-6.csv') as file:
    rows = csv.reader(file, delimiter=',')
    header = next(rows)[1:]
    data = []
    for row in rows:
        obj = dict(zip(header, row[1:]))
        data.append(obj)

    data = tuple(data)
