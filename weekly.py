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

cols = ['DeliveryID', 
        'Last Name', 
        'First Name', 
        'MiddleName', 
        'MedicaidNo', 
        'ActivityDate', 
        'DeliveryTime', 
        'MealType', 
        'Units', 
        'Status', 
        'Unnamed: 10', 
        'Unnamed: 11', 
        'Unnamed: 12', 
        'Unnamed: 13']

print(cols)