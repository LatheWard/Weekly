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


#medicaiddf = df[(df['MealType'].str.contains('(MW)')) & (df['Status'].str.contains('Completed OKAY'))].groupby('City')['DeliveryID'].count()

medicaiddf = pd.DataFrame(df.groupby(['City', 'Status'])['DeliveryID'].count())

print(medicaiddf)


writer = pd.ExcelWriter('Sum.xlsx') 
medicaiddf.to_excel(writer, sheet_name='Report', index=False, na_rep='NaN')

for column in medicaiddf:
    column_length = max(medicaiddf[column].astype(str).map(len).max(), len(column))
    col_idx = medicaiddf.columns.get_loc(column)
    writer.sheets['Report'].set_column(col_idx, col_idx, column_length)



col_idx = df.columns.get_loc('City')
writer.sheets['Report'].set_column(col_idx, col_idx, 15)

col_idx = df.columns.get_loc('Status')
writer.sheets['Report'].set_column(col_idx, col_idx, 15)

col_idx = df.columns.get_loc('DeliveryID')
writer.sheets['Report'].set_column(col_idx, col_idx, 15)

writer.save()
