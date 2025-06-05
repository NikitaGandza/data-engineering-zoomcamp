import pandas as pd
import sqlalchemy
import argparse
import os


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    csv_name = 'output.csv'

    os.system(f"wget {url} -O {csv_name}")

    engine = sqlalchemy.create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter = pd.read_csv(
        csv_name,
        compression='gzip',
        iterator=True,
        chunksize=100_000,
        low_memory=False,
        dtype={
            6: 'str'
        }
    )

    df = next(df_iter)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(table_name, index=False, con=engine, if_exists='replace')
    df.to_sql(table_name, index=False, con=engine, if_exists='append')


    while True:
        df = next(df_iter)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(table_name, index=False, con=engine, if_exists='append')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to postgres')

    parser.add_argument("--user", help="user name for postgres")
    parser.add_argument("--password", help="password for postgres")
    parser.add_argument("--host", help="host for postgres")
    parser.add_argument("--port", help="port for postgres")
    parser.add_argument("--db", help="database name in postgres")
    parser.add_argument("--table-name", help="table name in database")
    parser.add_argument("--url", help="csv file url")

    args = parser.parse_args()

    main(args)