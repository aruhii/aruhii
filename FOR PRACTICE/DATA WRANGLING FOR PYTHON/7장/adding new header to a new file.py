from csv import reader

data_reader = reader(open("mn.csv","r"))
data_rows = [i for i in data_reader]

header_reader = reader(open("mn_headers_updated.csv","r"))
header_rows = [i for i in header_reader if i[0] in data_rows[0]]

print(data_rows[0])
print(len(header_rows))

all_short_headers = [i[0] for i in header_rows]

skip_index = []

for header in data_rows[0]:
    if header not in all_short_headers:
        index = data_rows[0].index(header)
        skip_index.append(index)

data_headers = []

for i, header in enumerate(data_rows[0]):
    if i not in skip_index:
        data_headers.append(header)

header_match = zip(data_headers,all_short_headers)
print(list(header_match))

"""
new_data = []

for row in data_rows[1:]:
    new_row = []
    for i, d in enumerate(row):
        if i not in skip_index:
            new_row.append(d)
    new_data.append(new_row)

print(new_data[:2])

zipped_data = []

for drow in new_data:
    zipped_data.append(zip(header_rows,drow))
    """




