
import pandas as pd

import re

def extract_Employee_ID_from_Trello(trello_df: pd.DataFrame)-> pd.DataFrame:
    employee_id_list=[]
    for description in trello_df["Card Description"]:
            # Using regular expressions to find all 6-digit numbers
        if len(re.findall(r'\b\d{6}\b', str(description)))>0:
            numbers = re.findall(r'\b\d{6}\b', str(description))
            employee_id_list.extend(numbers)
        else:
             employee_id_list.extend('0')
    trello_df["Card Description"]=employee_id_list
    trello_df["Card Description"]=trello_df["Card Description"].astype(int)
    return trello_df


