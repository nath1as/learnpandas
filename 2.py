import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import style
# style.use('ggplot')

web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 53, 34, 45, 64, 34],
             'Bounce_Rate': [65, 72, 62, 64, 54, 66] }


df = pd.DataFrame(web_stats)
df.set_index('Day', inplace=True)

print(df)
print(df.head(2))
print(df.tail(2))


style.use('fivethirtyeight')

print(df['Visitors'])
print(df.Visitors)

#plot a single column with df['Visitors'].plot()
df.plot()
plt.show()
