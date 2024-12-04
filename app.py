import sys
import logging
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QFileDialog, QMessageBox
from PySide6.QtCore import QStringListModel
from PySide6.QtGui import QIcon
from load_data import *
from compare import *
from process_data import *
from main import Ui_MainWindow

# Constants for configuration
ICON_PATH = "BCG_Corporate_Logo.ico"

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestClass(QMainWindow):
    def __init__(self):
        super(TestClass, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Termination Report App")
        self.setWindowIcon(QIcon(ICON_PATH))

        # Dictionary to store DataFrames by variable name
        self.dataframes = {}

        # Setup UI connections
        self.setup_connections()

    def setup_connections(self):
        """
        Sets up the connections between UI elements and logic.
        """
        self.ui.pushButton.clicked.connect(
            lambda: self.handle_upload("df_OLD_REPORT", self.ui.TW_old_report_preview)
        )
        self.ui.pushButton_2.clicked.connect(
            lambda: self.handle_upload("df_NEW_REPORT", self.ui.Preview_new_report_TV)
        )
        self.ui.pushButton_3.clicked.connect(
            lambda: self.handle_upload("df_Trello", self.ui.Preview_trello_TV)
        )
        self.ui.Download_BTN.clicked.connect(self.download_final_report)

    def check_and_compare(self):
        """
        Automatically triggers the comparison processes when the necessary DataFrames are present.
        """
        required_keys = ["df_OLD_REPORT", "df_NEW_REPORT", "df_Trello"]
        missing_keys = [key for key in required_keys if key not in self.dataframes]
        
        if missing_keys:
            logger.info(f"Waiting for all required datasets to be uploaded: {missing_keys}")
        else:
            logger.info("All required datasets are available. Running comparisons...")
            self.compare_reports()
            self.compare_to_trello()
            self.find_differencies_old_new()

    def handle_upload(self, variable_name: str, table_view: QTableView, skip_rows: int = 0):
        """
        Handles the file upload, stores the DataFrame, and updates dependent processes.
        """
        try:
            df = upload_file(self, table_view)
            if df is not None:
                self.dataframes[variable_name] = df
                logger.info(f"DataFrame stored as '{variable_name}' and previewed in the table view.")
                self.check_and_compare()
            else:
                logger.warning(f"Failed to load DataFrame for variable '{variable_name}'.")
        except Exception as e:
            logger.error(f"Error during file upload for '{variable_name}': {str(e)}")
            QMessageBox.critical(self, "Upload Error", f"Failed to upload file: {str(e)}")

    def download_final_report(self):
        """
        Allows the user to download the final results DataFrame as an Excel file.
        """
        try:
            final_results = self.dataframes.get("df_final_results")
            if final_results is None:
                QMessageBox.warning(self, "No Results", "No final results to download.")
                return

            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self, "Save Excel File", "", "Excel Files (*.xlsx)")

            if file_path:
                final_results.to_excel(file_path, index=False)
                QMessageBox.information(self, "Success", f"File saved to {file_path}")
                logger.info(f"Final report saved to {file_path}")
            else:
                logger.warning("Download cancelled by the user.")
        except Exception as e:
            logger.error(f"Failed to save file: {str(e)}")
            QMessageBox.critical(self, "Error", f"Failed to save file: {str(e)}")

    def compare_reports(self):
        """
        Compares the old and new reports to identify new entries.
        """
        df_old = self.dataframes.get("df_OLD_REPORT")
        df_new = self.dataframes.get("df_NEW_REPORT")

        if df_old is not None and df_new is not None:
            new_entries = find_new_entries(df_old, df_new)
            self.dataframes["df_NEW_ENTRIES"] = new_entries

            if not new_entries.empty:
                preview_dataframe(new_entries, self.ui.Preview_old_new_report_TV)
                #QMessageBox.information(self, "Comparison Complete", "New entries displayed.")
            else:
                self.ui.Preview_old_new_report_TV.setModel(None)
                #QMessageBox.information(self, "No New Entries", "No new entries found.")
        else:
            print("Old or new reports are missing. Skipping comparison.")

    def compare_to_trello(self):
        """
        Compares new entries against Trello data and displays the final results.
        """
        try:
            self.get_trello_id()
        except:
            print('Id already extracted')

        df_new_entries = self.dataframes.get("df_NEW_ENTRIES")
        df_trello = self.dataframes.get("df_Trello")

        if df_new_entries is not None and df_trello is not None:
            final_comparison_df = find_new_entries_comparing_to_trello(df_trello, df_new_entries)
            self.dataframes["df_final_results"] = final_comparison_df

            if not final_comparison_df.empty:
                preview_dataframe(final_comparison_df, self.ui.Preview_Final_results_TV)
                QMessageBox.information(self, "Comparison Complete", "Final results displayed.")
            else:
                self.ui.Preview_Final_results_TV.setModel(None)
                QMessageBox.information(self, "No New Entries", "No new entries found in the comparison.")
        else:
            print("Comparison to Trello skipped. Ensure the necessary DataFrames are loaded.")

    def find_differencies_old_new(self):
        """
        Finds differences between the old and new reports and updates the list view.
        If no differences are found, the list view is cleared or displays a message.
        """
        df_new_entries = self.dataframes.get("df_NEW_ENTRIES")
        df_old_entries = self.dataframes.get("df_OLD_REPORT")

        if df_new_entries is not None and df_old_entries is not None:
            differences = find_differences(df_old_entries, df_new_entries)
            print(f"Differences found: {differences}")  # Debugging log

            # If differences exist, update the model and list view
            if differences:
                self.model = QStringListModel(differences)
            else:
                # No differences; display an appropriate message
                self.model = QStringListModel(["No differences found."])

            # Set the model to the QListView
            self.ui.Differences_LV.setModel(self.model)
        else:
            # Clear the list view if necessary data is missing
            self.model = QStringListModel(["Required data not available for comparison."])
            self.ui.Differences_LV.setModel(self.model)
            print("Comparison skipped. Ensure the required DataFrames are loaded.")

    def get_trello_id(self):
        """
        Extracts employee IDs from the Trello DataFrame.
        """
        df_trello = self.dataframes.get("df_Trello")
        if df_trello is not None:
            self.dataframes["df_Trello"] = extract_Employee_ID_from_Trello(df_trello)

    def list_dataframes(self):
        """
        Lists all saved DataFrame variable names.
        """
        return list(self.dataframes.keys())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(ICON_PATH))

    window = TestClass()
    window.show()

    sys.exit(app.exec())
