from PySide6.QtWidgets import QFileDialog, QMessageBox, QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem
import pandas as pd
import os
import re



'''def upload_file(parent, table_view: QTableView, skip_rows: int = 0):
    """
    Opens a file dialog to allow the user to select an Excel or CSV file and previews it in a QTableView.

    Args:
        parent: The parent widget (usually the main window) to attach dialogs to.
        table_view: The QTableView widget to display the content of the selected file.
        skip_rows (int): Number of rows to skip when reading the file.

    Returns:
        df: The loaded DataFrame, or None if an error occurs.
    """
    file_path, _ = QFileDialog.getOpenFileName(
        parent,
        "Select File",
        "",
        "Data Files (*.xlsx *.xls *.csv);;All Files (*)"
    )
    if file_path:
        try:
            # Determine the file type based on the extension
            _, file_extension = os.path.splitext(file_path)
            file_extension = file_extension.lower()

            if file_extension in ['.xlsx', '.xls']:
                # Load Excel file
                df = pd.read_excel(file_path, skiprows=skip_rows).fillna('2000-01-01')
            elif file_extension == '.csv':
                # Load CSV file
                df = pd.read_csv(file_path, skiprows=skip_rows).fillna('2000-01-01')
            else:
                raise ValueError("Unsupported file type. Please select an Excel or CSV file.")

            # Preview the DataFrame in the QTableView
            preview_dataframe(df, table_view)

            # Show success message
            QMessageBox.information(parent, "File Loaded", f"Successfully loaded: {file_path}")
            return df
        except Exception as e:
            QMessageBox.critical(parent, "Error", f"Failed to load file: {e}")
            return None
    else:
        QMessageBox.warning(parent, "No File", "No file was selected!")
        return None'''

import pandas as pd
import os
from PySide6.QtWidgets import QFileDialog, QMessageBox, QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem

def upload_file(parent, table_view: QTableView):
    """
    Opens a file dialog to allow the user to select an Excel or CSV file and previews it in a QTableView.
    Automatically determines the skip rows based on 'Employee ID' or 'Card ID' in column A.

    Args:
        parent: The parent widget (usually the main window) to attach dialogs to.
        table_view: The QTableView widget to display the content of the selected file.

    Returns:
        df: The loaded DataFrame, or None if an error occurs.
    """
    file_path, _ = QFileDialog.getOpenFileName(
        parent,
        "Select File",
        "",
        "Data Files (*.xlsx *.xls *.csv);;All Files (*)"
    )
    if file_path:
        try:
            # Determine the file type based on the extension
            _, file_extension = os.path.splitext(file_path)
            file_extension = file_extension.lower()

            # Load the file into a raw DataFrame
            if file_extension in ['.xlsx', '.xls']:
                raw_df = pd.read_excel(file_path, header=None)
            elif file_extension == '.csv':
                raw_df = pd.read_csv(file_path, header=None)
            else:
                raise ValueError("Unsupported file type. Please select an Excel or CSV file.")

            # Automatically determine the skip rows
            skip_rows = -1
            for index, row in raw_df.iterrows():
                if row.iloc[0] in ['Employee ID', 'Card ID']:
                    skip_rows = index
                    break

            if skip_rows == -1:
                raise ValueError("Could not find 'Employee ID' or 'Card ID' in column A.")

            # Reload the DataFrame with the determined skip rows
            if file_extension in ['.xlsx', '.xls']:
                df = pd.read_excel(file_path, skiprows=skip_rows).fillna('2000-01-01')
            elif file_extension == '.csv':
                df = pd.read_csv(file_path, skiprows=skip_rows).fillna('2000-01-01')

            # Preview the DataFrame in the QTableView
            preview_dataframe(df, table_view)

            # Show success message
            QMessageBox.information(parent, "File Loaded", f"Successfully loaded: {file_path}")
            return df
        except Exception as e:
            QMessageBox.critical(parent, "Error", f"Failed to load file: {e}")
            return None
    else:
        QMessageBox.warning(parent, "No File", "No file was selected!")
        return None

def preview_dataframe(dataframe: pd.DataFrame, table_view: QTableView):
    """
    Previews a pandas DataFrame in a QTableView widget.

    Args:
        dataframe (pd.DataFrame): The DataFrame to display.
        table_view (QTableView): The QTableView widget where the DataFrame will be displayed.
    """
    model = QStandardItemModel()
    for col_index, col_name in enumerate(dataframe.columns):
        model.setHorizontalHeaderItem(col_index, QStandardItem(str(col_name)))

    for row_index, row in dataframe.iterrows():
        items = [QStandardItem(str(cell)) for cell in row]
        model.appendRow(items)

    table_view.setModel(model)


def preview_dataframe(df: pd.DataFrame, table_view: QTableView):
    """
    Previews a DataFrame in a QTableView.

    Args:
        df (pd.DataFrame): The DataFrame to preview.
        table_view (QTableView): The QTableView widget to display the content.
    """
    # Create a model for the QTableView
    model = QStandardItemModel()

    # Set the headers
    model.setColumnCount(len(df.columns))
    model.setHorizontalHeaderLabels(df.columns.tolist())

    # Populate the rows
    for row in df.itertuples(index=False):
        model.appendRow([QStandardItem(str(value)) for value in row])

    # Set the model to the table view
    table_view.setModel(model)






