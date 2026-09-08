# Working with excel using openpyxl library.
import openpyxl as xl
from openpyxl.chart import BarChart, Reference

wb = xl.load_workbook("Data/transactions.xlsx")
sheet = wb['Sheet1']    # Access sheet from xlsx file
cell = sheet['a1']  # Access cells individually
acell = sheet.cell(1,1) # Access cells using cell() function

print(f"Cell access using sheet[a1]: {cell}")
print(f"Cell access using cell() function: {acell}")

# Loop through rows of the excel
for row in range(1, sheet.max_row + 1):
    print(row)  # Prints row numbers


# Loop through to access cell value
for row in range(1, sheet.max_row + 1):
    cVal = sheet.cell(row, 3)   # Pick price column
    print(cVal.value)


# Calculate the modified price, name a new column and add values in it.
col4 = sheet.cell(1, 4)
col4.value = "Modified_Price"

for row in range(2, sheet.max_row + 1):
    p_cell = sheet.cell(row, 3)
    mp_price = p_cell.value * 0.9
    mp_cell = sheet.cell(row, 4)   # Pick price column
    mp_cell.value = mp_price


# Add a BarChart
mp_values = Reference(sheet, min_row = 2, max_row = sheet.max_row,
                      min_col = 4, max_col = 4)

chart = BarChart()
chart.add_data(mp_values)
sheet.add_chart(chart, 'g2')

# call workbook save() function
wb.save("Data/modified_transactions.xlsx")



