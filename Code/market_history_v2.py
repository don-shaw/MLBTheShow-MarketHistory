'''
Title: MLB The Show Market History
Purpose: This script will download your completed transactions from theshownation.com
         It will also load your transactions into into a PostgreSQL database.
'''

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from sqlalchemy import create_engine
requests.packages.urllib3.disable_warnings()


def process_market_history(csv_file, pages, browser_headers):
    try:
        with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
            market_file = csv.DictWriter(csv_file, fieldnames=['name', 'purchase_type', 'price', 'time'])
            market_file.writeheader()

            for x in range(1, pages):
                print(f'Processing page {x}')

                r = requests.get(f'https://theshownation.com/mlb20/orders/completed_orders?page={x}&', headers=browser_headers)
                # print(r.url)
                pagetext = r.text
                soup = BeautifulSoup(pagetext, 'html.parser')
                # print(soup)

                table = soup.find('tbody')
                index = table.find_all('tr')

                for i in index:
                    name = i.contents[1].text.strip()
                    print(name)
                    purchase_type = i.contents[3].text.split(' ')[0].strip()
                    amount_i = i.contents[3].text.split(' ')[1].strip()
                    amount = amount_i[3:].strip()
                    time = i.contents[5].text
                    market_file.writerow({'name': name, 'purchase_type': purchase_type, 'price': amount, 'time': time})
    except Exception as e:
        print(e)


def process_sql(db_connection, db_table, csv_file):
    try:

        engine = create_engine(db_connection)

        transactions = pd.read_csv(csv_file)
        transactions.columns = map(str.lower, transactions.columns)
        transactions = transactions.replace('\n', '', regex=True)

        transactions['price'] = transactions['price'].str.replace(',', '').astype(int)
        transactions["price"] = pd.to_numeric(transactions["price"])

        transactions['date'] = pd.to_datetime(transactions['time'])
        transactions['date'] = transactions['date'].dt.strftime('%m-%d-%Y')

        transactions.to_sql(db_table, con=engine, index=False, if_exists='replace')

    except Exception as error:
        print(error)


if __name__ == '__main__':

    # These headers need to be updated with from your browser
    headers = {}

    # Set the following variables
    market_csv = 'market_history.csv'
    num_pages = 5
    postgres_conn = 'postgresql+psycopg2://postgres:postgres@localhost:5433/show'
    db_table = 'transactions'

    # Go!
    print('processing market history...')
    process_market_history(market_csv, num_pages, headers)

    print('processing sql table(s)...')
    process_sql(postgres_conn, db_table, market_csv)
