from PySide6.QtWidgets import QFileDialog, QMessageBox, QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem
import pandas as pd
import os
import re


def find_new_entries(df_old: pd.DataFrame, df_new: pd.DataFrame) -> pd.DataFrame:
    """
    Finds new entries in df_new that are not present in df_old.

    Args:
        df_old (pd.DataFrame): The old DataFrame.
        df_new (pd.DataFrame): The new DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing rows that are in df_new but not in df_old.
    """
    df_old['Pay Through Date'] = df_old['Pay Through Date'].astype('datetime64[ns]')
    df_new['Pay Through Date'] = df_new['Pay Through Date'].astype('datetime64[ns]')

    merged_df = pd.merge(df_old, df_new, how='outer', indicator=True)
    new_entries = merged_df[merged_df['_merge'] == 'right_only'].drop(columns=['_merge'])
    return new_entries



def find_new_entries_comparing_to_trello(trello_df: pd.DataFrame,new_entries: pd.DataFrame)->pd.date_range:
    trello_df.rename(columns = {'Card Description':'Employee ID'}, inplace = True)
    merged_df = pd.merge(trello_df, new_entries, on='Employee ID',how='outer', indicator=True)
    new_entries = merged_df[merged_df['_merge'] == 'right_only'].drop(columns=['Card ID','Card URL', 'Card Name', 'Labels',
       'Members', 'Due Date', 'Attachment Count', 'Attachment Links',
       'Checklist Item Total Count', 'Checklist Item Completed Count',
       'Vote Count', 'Comment Count', 'Last Activity Date', 'List ID',
       'List Name', 'Board ID', 'Board Name', 'Archived', 'Start Date',
       'Due Complete', 'To DO Date', 'Priority', 'Status','_merge']).fillna(0)
    return new_entries

def find_differences(old_df: pd.DataFrame, new_entry_df: pd.DataFrame):
    merged_df = pd.merge(old_df, new_entry_df, on='Employee ID', suffixes=('_df1', '_df2'))
    all_results=[]
    # Checking for differences
    for index, row in merged_df.iterrows():
        differences = []
        for col in old_df.columns[1:]:  # Skip 'Employee ID' since it's the key for merge
            if row[col + '_df1'] != row[col + '_df2']:
                differences.append(f"{col} differs: {row[col + '_df1']} vs {row[col + '_df2']}")
        if differences:
            text=f"Employee name {row['Worker_df1']} with ID {row['Employee ID']} has differences:  ", '; '.join(differences)
            all_results.append(str(text))
    return all_results