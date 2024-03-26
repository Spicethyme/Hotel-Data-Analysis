import pandas as pd 
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:Tisagoodmoon@localhost:5432/postgres')

"""
df = pd.read_csv('2018.csv')
df.to_sql('2018', engine, if_exists='replace')

df = pd.read_csv('2019.csv')
df.to_sql('2019', engine, if_exists='replace')

df = pd.read_csv('2020.csv')
df.to_sql('2020', engine, if_exists='replace')
"""

df = pd.read_csv('meal_cost.csv')
df.to_sql('meal_cost', engine, if_exists='replace')

df = pd.read_csv('market_segment.csv')
df.to_sql('market_segment', engine, if_exists='replace')