import xlwt
from xlwt import Workbook

wb = Workbook()

sheet1 = wb.add_sheet("sheet1")

for i in range(1,10):
    sheet1.write(i,0,"%s" % str(i+3))

style = xlwt.easyxf("font: bold 1")

sheet1.write(0,0,"SAMPLE",style)

wb.save("xlwt_example.xls")