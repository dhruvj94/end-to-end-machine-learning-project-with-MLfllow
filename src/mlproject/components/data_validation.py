import os
from mlproject import logger
from mlproject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self):
        try:
            validation_status= None

            data= pd.read_csv(self.config.unzip_data_dir)
            all_cols= list(data.columns)

            all_schema= self.config.all_schema.keys()

            for col in all_cols:
                if len(all_schema) != len(all_cols):
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status for column name: {validation_status}\n")
                        f.write("Warning: Lists have different lengths.")
                    break
                if col not in all_schema:
                    validation_status= False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status for column name: {validation_status}")
                else:
                    validation_status= True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status for column name: {validation_status}")

            column_dtypes = data.dtypes.astype(str).tolist()
            all_schema_dtypes= list(self.config.all_schema.values())

            for i in range(len(column_dtypes)):
                if len(all_schema_dtypes) != len(column_dtypes):
                    validation_status = False
                    with open(self.config.STATUS_FILE_2, "w") as f:
                        f.write(f"Validation status for column data-type: {validation_status}\n")
                        f.write("Warning: Lists have different lengths.")
                    break
                if all_schema_dtypes[i] != column_dtypes[i]:
                    validation_status= False
                    with open(self.config.STATUS_FILE_2, "w") as f:
                        f.write(f"Validation status for column data-type: {validation_status}")
                else:
                    validation_status= True
                    with open(self.config.STATUS_FILE_2, "w") as f:
                        f.write(f"Validation status for column data-type: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise e