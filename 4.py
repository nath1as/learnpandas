import pandas as pd
import quandl

api_key = open('quandlapikey.text', 'r').read()

df = quandl.get('FMAC/HPI_AK')

print(df.head()) 

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

# print(fiddy_states[0][1])

for abbv in fiddy_states[0][1][1:]:
    print("FMAC/HPI_" + str(abbv))
