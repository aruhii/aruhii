import xlrd

loc = "/Users/hyun/PycharmProjects/GIT/FOR PRACTICE/GEEKFORGEEKS/EXCEL/list.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
# 뭐든지, 우선 주소를 한 변수에 저장하고(키값 저장하는 거 같이)
# 이를 이용하여 관련 파일을 여는 객체를 하나 만든다.
# 그리고 이 밖으로의 최대 영역에서 한개씩 안으로 들어가는 것. 위의 객체를 이용해 방금 말한 객체를 새로 만들고..
print(sheet.cell_value(0,0)) # 0,0이 시작임을 잊지말자

print(sheet.nrows)
print(sheet.ncols)

for i in range(sheet.ncols):
    print(sheet.cell_value(0,i))

for i in range(sheet.nrows):
    print(sheet.cell_value(i,0))


print(sheet.row_values(1))