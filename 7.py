import pandas as pd
import quandl

api_key = open('quandlapikey.text', 'r').read()

# df = quandl.get('FMAC/HPI_AK')

# print(df.head())

fiddy_states = pd.read_html(
    'https://simple.wikipedia.org/wiki/List_of_U.S._states'
    )

# print(fiddy_states[0][1])
main_df = pd.DataFrame()

for abbv in fiddy_states[0][1][1:]:
    query = "FMAC/HPI_" + str(abbv)
    df = quandl.get(query)
    df.columns = [str(abbv)]

    if main_df.empty:
        main_df = df
    else:
        main_df = main_df.join(df)

print(main_df.head())

