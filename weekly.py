from email import header
import pandas as pd

# filename = "RegionDelivery.csv"

# fields = []
# rows = []

# with open(filename, 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     fields = next(csvreader)

#     for row in csvreader:
#         rows.append(row)

#     print("Total no. of rows: %d"%(csvreader.line_num))


# print('Field names are:' + ', '.join(field for field in fields))
# print('\nFirst 5 rows are:\n')
# for row in rows[:5]:
#     for col in row:
#         print("%10s"%col,end=" "),
#     print('\n')

df = pd.read_csv("RegionDelivery.csv")
df2 = pd.read_csv("RegionalDelivery.csv")

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

print(rf_df.iloc[: , -4:])


# Open file from 'Summarize' folder, get a sum for all categories, create new excel or csv file, put sum's under columns in file