#TASK 1 - Data cleaning and preprocessing using Pandas 
#import pandas as pd
# Load the dataset
#df = pd.read_csv("KaggleV2-May-2016.csv")
#df.head()
#import pandas as pd
# Load the dataset
#df = pd.read_csv("KaggleV2-May-2016.csv")
#df.head()


#1. Remove Duplicates

import pandas as pd
# Load the dataset
df = pd.read_csv("KaggleV2-May-2016.csv")
# df.head()   ← you can un-comment this later to see the first few rows
# Check for duplicates
print("Duplicate rows:", df.duplicated().sum())
# Remove duplicates
df = df.drop_duplicates()


#2. Check NULL value

import pandas as pd
# Load the dataset
df = pd.read_csv("KaggleV2-May-2016.csv")
# Show first few rows (optional, to get a feel of data)
# print(df.head())
# Check for duplicate rows
print("Duplicate rows:", df.duplicated().sum())
# Drop duplicates
df = df.drop_duplicates()
# Check for missing/null values in each column
print("\nMissing values in each column:")
print(df.isnull().sum())


#3. Fix date format

import pandas as pd
# Load dataset
df = pd.read_csv("KaggleV2-May-2016.csv")
# Convert date columns to datetime format
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])
# Print to check format
print(df[['ScheduledDay', 'AppointmentDay']].head())

