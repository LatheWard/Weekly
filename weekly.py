from sys import flags
import pandas as pd
import numpy as np
from re import IGNORECASE

df = pd.read_csv("RegionDelivery (2).csv")


# cities = ['Abbeville',
# 'Philadelphia',
# 'Aberdeen',
# 'Pontotoc', 
# 'Calhoun',
# 'Chickasaw',
# 'Itawamba',
# 'Lafayette',
# 'Monroe',
# 'Pontotoc',
# 'Union']


# "FROZEN 5PK D2D (MW)"
# "FROZEN 5PK D2D (STATE)"


medicaiddf = pd.DataFrame(df.groupby(['MealType', 'City', 'Status'])['DeliveryID'].count())

writer = pd.ExcelWriter('Sum.xlsx', engine='xlsxwriter')
medicaiddf.to_excel(writer, sheet_name="Summary")
workbook = writer.book
worksheet = writer.sheets["Summary"]
#set the column width as per your requirement
worksheet.set_column('A:A', 25)
worksheet.set_column('B:B', 25)
worksheet.set_column('C:C', 25)
writer.save()

