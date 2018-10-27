# Python: Pandas

Pandas is a library for data structures and data analysis. Tutorials from pythonprogramming.net. Pandas has io tools to import data from different types and analysis tools useful for analysis.

## Basics
Import pandas as pd, using DataFrame function to create a data frame, and printing it.
```
import pandas as pd

web_stats = { 'Day': [1, 2, 3, 4, 5, 6],
              'Visitors': [43, 53, 34, 45, 64, 34],
              'Bounce_Rate': [65, 72, 62, 64, 54, 66] }

df = pd.DataFrame(web_stats)

print(df)
print(df.head(2))
print(df.tail(2))
```
The values are printed with index values by default. You can define the index as one of your data values.

```
df.set_index('Day', inplace=True)
```

The inplace=True param tells the function to mutate the df value, without it we would have to reassign it.
```
df = df.set_index('Day')
```
You can plot the values by using matplotlib.
To plot the visitors column:
```
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df['Visitors'].plot()
#or df.Visitors
plt.show()
```
Or plot the whole dataframe:

```
df.plot()
plt.show()
```

Convert dataframe to list:
```
print(df.Visitors.tolist())
```

or an array:
```
import numpy as np
print(np.array(df[['Bounce_Rate', 'Visitors']]))
```

and back:

```
df2 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))

```

## Pandas IO
Read and display some sample data from quandl.com, and add indexing by date.

```
import pandas as pd

df = pd.read_csv('ZILL-Z77006_3B.csv')
print(df.head())

df.set_index('Date', inplace = True)
```

Export data:
```
df.to_csv('newcsv2.csv')
```

Export just a column of data:
```
df['Value'].to_csv('newcsv2.csv')
```
Read, index and display the new file:
```
df = pd.read_csv('newcsv2.csv')
df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())
```

Change the name of values:
```
df.columns = ['House_Prices']
print(df.head())
```

Rename specific values:
```
df = pd.read_csv('newcsv4.csv', names = ['Date','House_Price'])
print(df.head())

df.rename(columns={'House_Price':'Prices'}, inplace=True)
print(df.head())
```


Save to csv:
```
df.to_csv('newcsv3.csv')
```

Save without headers:
```
df.to_csv('newcsv4.csv', header=False)
```

Use pandas to convert data type:
```
df.to_html('example.html')
```

## Building a Dataset

We use quandl library to get the data.

```
import quandl

df = quandl.get("FMAC/HPI_TX")

print(df.head())
```

Because quandl data is per state, we can pull the US states table from simple
wiki, and then iterate through it.
```
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(fiddy_states)

for abbv in fiddy_states[0][0][1:]:
    print(abbv)
```

After making sure it works we can make the codes to get the data from quandl.

```
for abbv in fiddy_states[0][0][1:]:
    #print(abbv)
    print("FMAC/HPI_"+str(abbv))
```

## Concatenating and Appending Dataframes
The first and third dataframe have the same index but different columns, the wecond and third different indexes and some different columns.

```
import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])
```

Concatenation works for the dataframes with the same columns, and the continuation of indexes.
```
concat = pd.concat([df1,df2])
print(concat)

#output

      HPI  Int_rate  US_GDP_Thousands
2001   80         2                50
2002   85         3                55
2003   88         2                65
2004   85         2                55
2005   80         2                50
2006   85         3                55
2007   88         2                65
2008   85         2                55

```

Concatenation of dataframes with different columns populates the missing values with NaN.

```
concat = pd.concat([df1,df2,df3])
print(concat)

#output

      HPI  Int_rate  Low_tier_HPI  US_GDP_Thousands
2001   80         2           NaN                50
2002   85         3           NaN                55
2003   88         2           NaN                65
2004   85         2           NaN                55
2005   80         2           NaN                50
2006   85         3           NaN                55
2007   88         2           NaN                65
2008   85         2           NaN                55
2001   80         2            50               NaN
2002   85         3            52               NaN
2003   88         2            50               NaN
2004   85         2            53               NaN
```
We can also append the first two dataframes without issues.

```
df4 = df1.append(df2)
print(df4)

#output

      HPI  Int_rate  US_GDP_Thousands
2001   80         2                50
2002   85         3                55
2003   88         2                65
2004   85         2                55
2005   80         2                50
2006   85         3                55
2007   88         2                65
2008   85         2                55
```

We can make single-columned dataframes with series.
```
s = pd.Series([80,2,50], index=['HPI','Int_rate','US_GDP_Thousands'])
df4 = df1.append(s, ignore_index=True)
print(df4)

#output
  HPI  Int_rate  US_GDP_Thousands
0   80         2                50
1   85         3                55
2   88         2                65
3   85         2                55
4   80         2                50
```

## Joining and Merging Dataframes
