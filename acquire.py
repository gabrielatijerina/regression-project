#Acquire data from CodeUp SQL database; credentials are required for login.

#import
import numpy as np
import pandas as pd
from env import host, user, password
import os

# This function creates a connection to CodeUp SQL Database 
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# This function gets Zillow data from MySQL and return as a pandas DataFrame
def get_zillow_data():
    '''
    This function reads in the zillow data from the Codeup db,
    selects all columns from the properties_2017 table,
    joins predictions_2017 table,
    and acquires single unit properties with transactions during May 2017 - August 2017
    and returns a pandas DataFrame with all columns.
    '''
 
    #create SQL query
    sql_query = '''
                SELECT *
                FROM properties_2017
                JOIN predictions_2017 USING(parcelid)
                WHERE propertylandusetypeid IN (260, 261, 263, 264, 265, 266, 273, 275, 276, 279)
                AND transactiondate >= "2017-05-01" AND transactiondate <= "2017-08-31";
                '''
    
    #read in dataframe from Codeup db
    df = pd.read_sql(sql_query, get_connection('zillow'))
    
    return df

