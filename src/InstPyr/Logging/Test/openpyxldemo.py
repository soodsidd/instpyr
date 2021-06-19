from openpyxl import Workbook

workbook=Workbook()
sheet=workbook.active

sheet['A1']='Hello'
sheet['B1']='World!'
sheet.append([1,2])
sheet.append([2,3])

workbook.save(filename='helloworld.xlsx')
