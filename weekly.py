from sys import flags
import pandas as pd
import numpy as np
from re import IGNORECASE

# 
df = pd.read_csv("RegionDelivery.csv")


# cols = ['Last Name', 
#         'First Name',  
#         'MedicaidNo', 
#         'ActivityDate',
#         'DeliveryID', 
#         'DeliveryTime', 
#         'MealType', 
#         'Units', 
#         'Status', 
#         'Unnamed: 11', 
#         'Unnamed: 12', 
#         'Unnamed: 13']

# df = df.reindex(columns=cols)

# rf_df = df[cols]
df.rename(columns={"Unnamed: 11": "County"}, inplace=True)
df.rename(columns={"Unnamed: 12": "Agent"}, inplace=True)
df.rename(columns={"Unnamed: 13": "City"}, inplace=True)

cities = ['Abbeville',
'Philadelphia',
'Aberdeen',
'Pontotoc', 
'Calhoun',
'Chickasaw',
'Itawamba',
'Lafayette',
'Monroe',
'Pontotoc',
'Union']

citynums = {
  "Delivered": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  "Not Delivered": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}


# "FROZEN 5PK D2D (MW)"

# "FROZEN 5PK D2D (STATE)"


medicaiddf = pd.DataFrame(citynums, index=cities)
statedf = pd.DataFrame(citynums, index=cities)

# if df.MealType.str.contains("(MW)"):

for i in df.index:
  if df.City.str.count('Abbe', flags=IGNORECASE).sum() >= 1:
        medicaiddf.loc['Abbeville', 'Delivered'] += 1

print(medicaiddf)

# print(rf_df.iloc[: , :])

# rf_df.to_excel('summary.xlsx', sheet_name='Report')

# Open file from 'Summarize' folder, get a sum for all categories, create new excel or csv file, put sum's under columns in file