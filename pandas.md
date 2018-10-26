# Pandas libraray
  Pandas is a library for data structures and data analysis.

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
