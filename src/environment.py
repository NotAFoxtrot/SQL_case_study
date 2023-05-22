import psycopg2
import pandas as pd
from psycopg2 import OperationalError
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_HOST = os.getenv('PG_HOST')
PG_PORT = os.getenv('PG_PORT')
PG_DATABASE = os.getenv('PG_DATABASE')

# If using docker change host to 'localhost' and password to the password
# set in the 'docker run' command

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection
conn = create_connection(PG_DATABASE,PG_USER,PG_PASSWORD, PG_HOST,PG_PORT)

c = conn.cursor()

# with open('../sql_queries/HR_Question_1.sql') as f:
#     lines= f.read()


# df = pd.read_sql(lines, conn)
# df.to_excel('../excel_reports/Test.xlsx', sheet_name='Test.xlsx')

def convert_sql_to_xlsx(sql_in, xlsx_out, xlsx_name=None):
    """
    Runs query in given .sql file, stores result as .xlsx file.

    Parameters:
        sql_in (str): relative filepath to .sql file
        xlsx_out (str): relative filepath to directory where .xlsx will be stored
        xlsx_name (str or None): If not None, file named xlsx_name.xlsx
                                 If None, file named same as sql_in

    Returns:
        None
    """
    with open(sql_in) as f:
        lines= f.read()

    sheet_name = xlsx_name if xlsx_name else sql_in

    xlsx_file = f'{xlsx_out}/{xlsx_name}.xlsx' if xlsx_name else f'{xlsx_out}/{sql_in}.xlsx' 

    df = pd.read_sql(lines, conn)
        
    df.to_excel(xlsx_file, sheet_name=sheet_name)

convert_sql_to_xlsx('../sql_queries/HR_Question_1.sql', '../excel_reports', xlsx_name='Test 1')

#convert_sql_to_xlsx('../sql_queries/HR_Question_1.sql','../excel_reports','Test.xlsx')

def convert_directory_of_queries(sql_in_dir, xlsx_out_dir):
    """
    Runs each query in sql_in_dir directory,
        stores each result as .xlsx in xlsx_out_dir.

    Parameters:
        sql_in_dir (str): relative filepath to directory
                          containing .sql files
        xlsx_out_dir (str): relative filepath to directory
                            where .xlsx will be stored
                            files named same as sql_in

    Returns:
        None
    """
    pass

def convert_sql_to_xlsx_from_cli():
    """
    Converts directory of sql queries to xlsx from CLI.
    """
    pass