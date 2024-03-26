# Hotel-Data-Analysis
Develop a database to analyse &amp; visualize hotel booking data

### Questions
- Is our hotel revenue growing by year?
- Should we increase our parking lot size?
- What trends can we see in the data?

### Methodology
1. Build a Database
2. Develop the SQL Query
3. Connect PowerBI to the Database
4. Visualize
5. Summarize Findings

### Data Sources
Hotel Revenue Dataset for (2018, 2019, 2020) 
- file : hotel_revenue_historical_full-2.csv
- file : market_segment.csv
- file : meal_cost.csv

### Tools
- Python - Scripts to upload csv files to database
- SQL(Postgres) - Data Analysis
- PowerBI - Visualization and creating a report

## 1. Build a Database
- I used the sqlalchemy python package to create all my tables in my postgres database
    - file : sql_alchemy.py

## 2. Develop the SQL Query
- I wrote an SQL query to join the multiple tables I will need for the visualization
  - file : hotel_dataset_full.sql
 
## 3. Connect PowerBI to the Database
- I imported the dataset from my postgres SQL server database using my previous SQL statement

## 4. Visualize
- I used PowerBI to create an interactive dashboard to visualize :
    - Total Revenue
    - Parking needed
    - Revenue by time
    - Revenue by hotel type
    - Trends

## 5. Summarize Findings
