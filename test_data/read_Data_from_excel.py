import os

import pandas as pd


class ReadFile:
    @staticmethod
    def read_file(file_path):
        # Reading data from file excel
        df = pd.read_excel(file_path)
        df = pd.DataFrame(df, columns=["username_email", "password"])
        df = df.fillna('')
        return df.values.tolist()

    @staticmethod
    def get_test_data(index):
        # Gets the directory where the current script is located
        script_dir = os.path.dirname(__file__)
        # This constructs the full path to the Excel
        data_file_path = os.path.join(script_dir, '../test_data/DDT.xlsx')
        # Reads data from the specified Excel file
        data_values = ReadFile.read_file(data_file_path)
        if index < len(data_values):
            return data_values[index]
        else:
            return None
