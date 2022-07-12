import pandas as pd
import numpy as np



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


print(rf_df.iloc[: , :])

rf_df.to_csv('summary.csv')

# Open file from 'Summarize' folder, get a sum for all categories, create new excel or csv file, put sum's under columns in file