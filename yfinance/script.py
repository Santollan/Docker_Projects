# Module Import
import yfinance as yf
import pandas as pd
import mariadb
import sys
import configparser
from sqlalchemy import create_engine

#DB_initial_setup
config = configparser.ConfigParser()

# Read the configuration file
config.read(r'config/config.ini')

# Access the configuration values
db_host = config.get('DB', 'host')
db_user = config.get('DB', 'user')
db_password = config.get('DB', 'password')
db_port = config.getint('DB', 'port')
database = "stocks"

# Create the database engine
engine = create_engine(f"mariadb+mariadbconnector://{db_user}:{db_password}@{db_host}:{db_port}/{database}")

data = yf.download("SPY AAPL", period="1mo")
df = pd.DataFrame(data)

# Write the DataFrame to the MariaDB database
df.to_sql('stock_test', con=engine, if_exists='replace', index=False)