#from shiny import App, render, ui
import matplotlib.pyplot as plt
from shiny.express import render, ui
import sqlite3
import pandas as pd

# Function to get the data from the SQLite database
#def get_attractions():
#    conn = sqlite3.connect('attractions.db')
#    query = 'SELECT * FROM attractions'
#    df = pd.read_sql_query(query, conn)
#    conn.close()
#    return df

df=pd.read_csv('FYA_World_Class.csv')

ui.h2('World Class Attractions')

@render.data_frame
def attraction_df():
    return render.DataGrid(df)

ui.h2('Distribution of Scores')

@render.plot
def score_hist():
    score = df['Score']
    fig = score.hist(range = [0,10])
    return fig  