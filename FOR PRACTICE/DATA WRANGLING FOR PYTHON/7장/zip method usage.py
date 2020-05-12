from csv import reader

data_reader = reader(open("mn.csv","r"))
header_reader = reader(open("mn_headers.csv","r")) # 책처럼 rb 로 하면 안되네. 왜지?
print(header_reader) # iterator임. 따라서 반복문으로 안을 확인해봐야 함

data_rows = [i for i in data_reader]
header_rows = [i for i in header_reader]

print(data_rows[0])
print(header_rows[:4])

print(len(data_rows[0]))
print(len(header_rows))
# 159개와 210개는 즉 헤더가 210개가 있는데 그 중 쓰는게 159개 밖에 없다는 소리
# 따라서 어떤 헤더가 쓰였으며, 고려하지 않아도 되는 헤더는 무엇인지 찾아내야 함.

bad_rows = []

for i in header_rows:
    if i[0] not in data_rows[0]:
        bad_rows.append(i) # 통채로 붙임. 단순히 "MCM12D" 뿐만이 아니라.

print(bad_rows)

for i in bad_rows:
    header_rows.remove(i) # 그래서 통채로 하나의 []리스트를 없애서 가능한 것.

print(len(header_rows))

# 이제 data가 header보다 9개 더 많다. 왜 ?

shorten_form_of_headers = [i[0] for i in header_rows]

for i in data_rows[0]: # 이게 159개로 더 많으니까; 150개가 이거보다 아래에 있어야지;
    if i not in shorten_form_of_headers:
        print("mismatch %s" % i)


