import pandas as pd
import pandas as pd
import re
import streamlit as st

# Read the log file and store each line as a separate row in a list
logfile = r'C:\Users\vieir\OneDrive\Documentos\GitHub\SL\streamlit\openvpn.log'
with open(logfile, 'r') as file:
    data = [line.strip() for line in file]

# Create a DataFrame from the list

data = [line.split() for line in data]
df = pd.DataFrame(data)

pd.set_option('display.max_columns', None)
df.columns = ['mes', 'dia', 'hora', 'firewall', 'sessao', 'username', 'client', 'occurrence', 'origem', 'key', 'ip_origem', 'peer', 'info', 'version', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20']  

# Extract session time and username using regular expressions
df['session_time'] = df['hora'].str.extract(r'(\d+:\d+:\d+)')
#df['username'] = df['username'].str.extract(r'(?<=Username: )(\w+)')


# Group by 'sessao' and calculate the session duration
session_duration = df.groupby(['username', 'sessao'])['hora'].apply(lambda x: pd.to_datetime(x.max()) - pd.to_datetime(x.min())).reset_index()

# Merge the session_duration DataFrame with the original DataFrame
df = pd.merge(df, session_duration, on=['username', 'sessao'], how='left')

# Print the updated DataFrame
df
print(session_duration)
st.dataframe(session_duration)

