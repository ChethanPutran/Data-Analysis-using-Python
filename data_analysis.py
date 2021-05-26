## Pandas for Data-Analysis

import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pd.read_csv("reviews.csv",parse_dates=['Timestamp'])
data.head()

#data.shape
#data.columns
#data.hist("Rating")

data['Rating'].mean()

#Select multiple columns
data[["Rating","Comment"]]

#Getting single row
data.iloc[3]

#Getting multiple rows
data.iloc[1:3]

#Selecting a cell
data['Rating'].iloc[2]

#Or

data.at[2,'Rating']



#Extracting the data based on condition
d2=data[data['Rating']== 5]
d2['Rating'].mean()


#Time based filtering 
data[(data["Timestamp"]> datetime(2020,7,1,tzinfo=utc)) & (data["Timestamp"]< datetime(2020,12,31,tzinfo=utc))]



#Turning data into information
data[data["Comment"].str.contains("word",na=False)]

#Searching for not null values
data[data["Comment"].notnull()]

#Searching for not null values
data[data["Comment"].isnull()].count()

#Grouping based on day
data['Day'] = data["Timestamp"].dt.date

#Getting rating per day
data_t = data.groupby(["Day"]).mean()
x_ = list(data_t.index)

#Grouping based on week
data['Week'] = data["Timestamp"].dt.strftime("%Y-%U")

#Grouping based on month
data['Month'] = data["Timestamp"].dt.strftime("%Y-%m")

rating = data.groupby(['Month','Course Name'])['Rating'].mean().unstack()
rating.plot(figsize=(25,10))
# x_ = list(data_t.index)
# y_ = data_t["Rating"]
# plt.figure(figsize=(25,3))
# plt.plot(x_,y_)