import pandas as pd
import numpy as np

# 
df = pd.read_csv("RegionDelivery.csv")


cols = ['Last Name', 
        'First Name',  
        'MedicaidNo', 
        'ActivityDate',
        'DeliveryID', 
        'DeliveryTime', 
        'MealType', 
        'Units', 
        'Status', 
        'Unnamed: 11', 
        'Unnamed: 12', 
        'Unnamed: 13']

df = df.reindex(columns=cols)

rf_df = df[cols]
rf_df.rename(columns={"Unnamed: 11": "County"}, inplace=True)
rf_df.rename(columns={"Unnamed: 12": "Agent"}, inplace=True)
rf_df.rename(columns={"Unnamed: 13": "City"}, inplace=True)

stsumrows = ['Abbeville',
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

stsumcols = ['Delivered',
             'Not Delivered'
             ]



FZ_ST = df.loc[df['MealType'] == "FROZEN 5PK D2D (MW)"]

# FZ_MW = df.loc[df['MealType'] == "FROZEN 5PK D2D (STATE)"]  

# site = df.loc[df['City'].str.contains("Abbe")]

medicaiddf = pd.DataFrame(columns = stsumcols, index=stsumrows)
statedf = pd.DataFrame(columns = stsumcols, index=stsumrows)


for i in range(len(df)):
        if df['MealType'] == "FROZEN 5PK D2D (MW)":
                if site:
                        sdf.append
        


# print(rf_df.iloc[: , :])

# rf_df.to_excel('summary.xlsx', sheet_name='Report')

# Open file from 'Summarize' folder, get a sum for all categories, create new excel or csv file, put sum's under columns in file