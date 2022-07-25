from sys import flags
import pandas as pd
import numpy as np
from re import IGNORECASE
from tkinter.filedialog import askopenfilename
# filename = askopenfilename()

df = pd.read_csv("RegionDelivery (2).csv")

# cities = ['Abbeville','Philadelphia','Aberdeen','Pontotoc', 'Calhoun','Chickasaw',
# 'Itawamba','Lafayette','Monroe','Pontotoc','Union']

# "FROZEN 5PK D2D (MW)"
# "FROZEN 5PK D2D (STATE)"


rdf = df.groupby(['MealType', 'City', 'Status'])['DeliveryID'].count()
rdf.to_frame()


writer = pd.ExcelWriter('Sum.xlsx', engine='xlsxwriter')
rdf.to_excel(writer, sheet_name="Summary")
workbook = writer.book
worksheet = writer.sheets["Summary"]

#Blue
format1 = workbook.add_format({'bg_color': '#9AD7A4',
                               'font_color': '#000000'})
#Gold
format2 = workbook.add_format({'bg_color': '#F0CA86',
                               'font_color': '#000000'})

for i in range(len(rdf)): 
    worksheet.set_row(i, cell_format=(format1 if i%2==0 else format2))   

worksheet.set_column('A:A', 25)
worksheet.set_column('B:B', 25)
worksheet.set_column('C:C', 25)

writer.save()

print(rdf)