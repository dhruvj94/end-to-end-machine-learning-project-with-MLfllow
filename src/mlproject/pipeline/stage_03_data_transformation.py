from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as file:
                status = file.read().split(" ")[-1]
                
            with open(Path("artifacts/data_validation/status_2.txt"), "r") as file:
                status_2 = file.read().split(" ")[-1]
            
            if (status == "True") and (status_2 == "True"):
                config = ConfigurationManager()
                data_transformation_config= config.get_data_transformation_config()
                data_tranformation= DataTransformation(config=data_transformation_config)
                data_tranformation.train_test_splitting()

            else:
                raise Exception("Data is not valid")
            
        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
    except Exception as e:
        logger.exception(e)
        raise e