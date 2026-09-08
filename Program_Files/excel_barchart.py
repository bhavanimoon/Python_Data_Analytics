# Working with excel using openpyxl library.
import openpyxl as xl
from openpyxl.chart import BarChart, Reference

def add_barchart(file_name, sheet_name):
    wb = xl.load_workbook(file_name)
    sheet = wb[sheet_name]    # Access sheet from xlsx file

    # Calculate the modified price, name a new column and add values in it.
    col4 = sheet.cell(1, 4)
    col4.value = "Modified_Price"

    for row in range(2, sheet.max_row + 1):
        p_cell = sheet.cell(row, 3)
        mp_price = p_cell.value * 0.85
        mp_cell = sheet.cell(row, 4)   # Pick price column
        mp_cell.value = mp_price

    # Add a BarChart
    mp_values = Reference(sheet, min_row = 2, max_row = sheet.max_row,
                        min_col = 4, max_col = 4)

    chart = BarChart()
    chart.add_data(mp_values)
    sheet.add_chart(chart, 'g2')

    # call workbook save() function
    wb.save(file_name)


add_barchart("Data/modified_transactions.xlsx", "Sheet1")
print("Excel modified and barchart added")