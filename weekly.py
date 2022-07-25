from sys import flags
import pandas as pd
import numpy as np
from re import IGNORECASE
from tkinter.filedialog import askopenfilename
filename = askopenfilename(filetypes=[("Excel files", ".xlsx .csv")])

df = pd.read_csv(filename)

# cities = ['Abbeville','Philadelphia','Aberdeen','Pontotoc', 'Calhoun','Chickasaw',
# 'Itawamba','Lafayette','Monroe','Pontotoc','Union']

# "FROZEN 5PK D2D (MW)"
# "FROZEN 5PK D2D (STATE)"
mostRecentDate = df['ActivityDate'].max()
leastRecentDate = df['ActivityDate'].min()

rdf = df.groupby(['MealType', 'City', 'Status'])['DeliveryID'].count()
rdf.to_frame()

writer = pd.ExcelWriter('Sum.xlsx', engine='xlsxwriter')
rdf.to_excel(writer, sheet_name="Summary")
workbook = writer.book
worksheet = writer.sheets["Summary"]
           
#Align Left
formatL = workbook.add_format({'bold': True})
formatL.set_align('left')
  
for i in range(1, len(rdf)): 
    worksheet.set_row(i, cell_format=(formatL))

worksheet.set_column('A:A', 25)
worksheet.set_column('B:B', 25)
worksheet.set_column('C:C', 25)
worksheet.set_column('D:D', 15)

worksheet.write(0,6, 'Start Date')
worksheet.write(0,5, 'Last Date')
worksheet.write(1,5, mostRecentDate)
worksheet.write(1,6, leastRecentDate)
worksheet.set_column('F:F', 20)
worksheet.set_column('G:G', 20)

worksheet.write(0, 3, "Totals", formatL)
writer.save()
