import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import snowflake.connector

SFAccount   = 'bnjwuct-rpb64317'
SFUser      = 'ingestion'
SFPassword  = '<a*-S$4!16@U'
SFWarehouse = 'ingestion_wh'
SFDB        = 'tbc'
SFSchema    = 'protheus'

#st.set_page_config(layout= 'wide')

st.title('SF Monitor :snowflake:')

snowflake_conn = snowflake.connector.connect(user=SFUser, password=SFPassword, account=SFAccount, warehouse=SFWarehouse, database=SFDB, schema=SFSchema)
sf_cursor = snowflake_conn.cursor()
sf_cursor.execute(f'select table_schema, table_name from tbc.information_schema.tables where row_count=0')
dados = sf_cursor.fetch_pandas_all()
sf_cursor.close()        
snowflake_conn.close()

filtro_vendedores = st.sidebar.multiselect('SCHEMA', dados['TABLE_SCHEMA'].unique())
if filtro_vendedores:
    dados = dados[dados['TABLE_SCHEMA'].isin(filtro_vendedores)]

st.dataframe(dados, width=1024, height=768)


