import pandas as pd

#pandas reading Recognized_Shop_Healthy_Stores20250505.csv data and storing in dfhealthy
dfhealthy = pd.read_csv("Recognized_Shop_Healthy_Stores_20250505.csv")
print("In the Recognized_Shop_Healthy_Stores data our headers are: " , dfhealthy.columns.to_list())

print(dfhealthy.head())

for count in dfhealthy.columns:
    print("The data types are: ", dfhealthy[count].dtype)


print("We will be using the 'Borough', and 'Year Awarded' data to make our analysis")
#3 different variables that saves stores by borough and award given either before or on 2022
#ensures data matches obesity data, (Borough &if 2013-2022)
bronx_healthy = dfhealthy[(dfhealthy['Borough'] == 'Bronx')& (dfhealthy['Year Awarded'] <= 2022)]
brooklyn_healthy = dfhealthy[(dfhealthy['Borough'] == 'Brooklyn')& (dfhealthy['Year Awarded'] <= 2022)]
manhattan_healthy = dfhealthy[(dfhealthy['Borough'] == 'New York')& (dfhealthy['Year Awarded'] <= 2022)]

#printing found data
print("The Bronx has had a total of: ", len(bronx_healthy), "stores participating in Shop Healthy's Retail Challenge.")
print("Brooklyn has had a total of: ", len(brooklyn_healthy), "stores participating in Shop Healthy's Retail Challenge.")
print("Manhattan has had a total of: ", len(manhattan_healthy), "stores participating in Shop Healthy's Retail Challenge.")
print("The total amount of Shop Healthy stores between all boroughs is: ", len(bronx_healthy) + len(brooklyn_healthy) + len(manhattan_healthy))



#
#
#Obesity Data Analysis
#
#


#pandas reading "NYC EH Data Portal - Obesity (adults) (filtered)-2.csv" and storing in dfob
dfob = pd.read_csv("NYC EH Data Portal - Obesity (adults) (filtered)-2.csv")
print("In the NYC EH Data Portal - Obesity data our headers are: " , dfob.columns.to_list())


print(dfob.head())

for count in dfob.columns:
    print("The data types are: ", dfob[count].dtype)


#3 variables that stores via borough, ob data does not include 2021 data in data
#ensures data matches healthy data
bronx_ob = dfob[(dfob['Borough'] == 'Bronx') & (dfob['GeoTypeDesc'] != 'UHF 34')]
brooklyn_ob = dfob[(dfob['Borough'] == 'Brooklyn') & (dfob['GeoTypeDesc'] != 'UHF 34')]
manhattan_ob = dfob[(dfob['Borough'] == 'Manhattan') & (dfob['GeoTypeDesc'] != 'UHF 34')]

#using pandas cleans the commas and change type to integer for all boroughs
cleanbronxnum = pd.to_numeric((bronx_ob['Number'].str.replace(",","")))
cleanbrooklynnum = + pd.to_numeric((brooklyn_ob['Number'].str.replace(",","")))
cleanmanhattannum = + pd.to_numeric((manhattan_ob['Number'].str.replace(",","")))

print("In the Bronx, the highest amount of obese people from 2013-2022 is: ", cleanbronxnum.max(), "and the lowest is: ", cleanbronxnum.min())
print("In Brooklyn, the highest amount of obese people from 2013-2022 is: " , cleanbrooklynnum.max(), "and the lowest is: ", cleanbrooklynnum.min())
print("In Manhattan, the highest number of obese people from 2013-2022 is: " , cleanmanhattannum.max(), "and the lowest is: ", cleanmanhattannum.min())


