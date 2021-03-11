from BaseFile.ReadExcelSheet import ReadExcel

filelocation = "C:\\Users\\abc\\Desktop\\Python P\\EmployeeData.xlsx"
row,column,sheet = ReadExcel.readExcelsheet(filelocation,'Empl')
print(row,column,sheet)

col= []

for row in range(2,row+1):
    col.append(sheet.cell(row=row,column= 1).value)
print(col)