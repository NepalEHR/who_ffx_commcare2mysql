#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:01:07 2019

@author: nepalehr
"""
#Set up logger
import logging
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO)
logger = logging.getLogger()

import requests
from requests.auth import HTTPBasicAuth
from pandas.io.json import json_normalize
import datetime as dt
import pandas as pd
import numpy as np
import pandas as pd
import MySQLdb
from sqlalchemy import create_engine, engine
from config import *

logger.info('[COMPLETE] All modules loaded')

###############################################################################
# FUNCTIONS
###############################################################################

def get_json(feed_url):
    """Takes a odata feed url, and returns feed data as json dictionary"""

    username = commcare_credentials['username']
    api = commcare_credentials['api']
    response = requests.get(
            feed_url,
            auth=HTTPBasicAuth(username, api))
    return response.json()

def load_data(name, feed_url):
    """Takes the name and url of odata feed, and returns a dataframe"""

    logger.info('Start downloading \'%s\' data', name)
    res_json = get_json(feed_url)
    df = json_normalize(res_json, 'value')
    while '@odata.nextLink' in res_json:
        logger.debug('%d rows of \'%s\' data downloaded...', len(df.index), name)
        nextLink = res_json['@odata.nextLink']
        res_json = get_json(nextLink)
        df = pd.concat([df, json_normalize(res_json, 'value')], sort=False)
    logger.info('[COMPLETE] Download \'%s\' data (%d rows)', name, len(df.index))
    df = df.replace({'---':np.NaN,'':np.NaN})
    return df

###############################################################################
# GET DATA FROM FEED INTO DATAFRAME
###############################################################################

df = load_data(odata_feed['name'], odata_feed['feed_url'])

###############################################################################
# OUTPUT DATA TO CSV
###############################################################################

if csv_output['skip'] == 'false':
    df.to_csv(csv_output['location']+odata_feed['name']+' '+dt.datetime.today().strftime('%m-%d-%Y %H%M%S')+'.csv', index=False)
    logger.info("[COMPLETE] Generate csv file to \'%s\'", csv_output['location'] + odata_feed['name']+' '+dt.datetime.today().strftime('%m-%d-%Y %H%M%S')+'.csv')
else:
    logger.info('[SKIP] Generate csv file')

###############################################################################
# WRITE TO MYSQL DATABASE
###############################################################################

connect_url = engine.url.URL(
        'mysql+mysqldb',
    username=mysql_credentials['username'],
    password=mysql_credentials['password'],
    host=mysql_credentials['host'],
    port=mysql_credentials['port'],
    database=mysql_credentials['database'])

engine = create_engine(connect_url)
df.to_sql(name=target_mysql_table['name'], con=engine, if_exists = target_mysql_table['if_exists'], index=False)
logger.info("[COMPLETE] %s the data in table \'%s\' in MySQL database \'%s\'", target_mysql_table['if_exists'].capitalize(), target_mysql_table['name'],mysql_credentials['database'])

# Close connection
engine.dispose()
                                                                                                                         1,1           To
