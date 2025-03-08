# end-to-end-machine-learning-project-with-MLfllow

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py




# How to Run?

### STEPS

Clone the repository

'''bash
https://github.com/dhruvj94/end-to-end-machine-learning-project-with-MLfllow

### STEP 01- Create a conda envirionment after opening the repository

'''bash
conda create -n mlproject python -y

'''bash
conda activate mlproject


### STEP 02- install the requirements

'''bash
pip install -r requirements.txt

'''bash
# Finally run the following command
python app.py

Now,
'''bash
open up your local host and port



## MLFlow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/dhruvj94/end-to-end-machine-learning-project-with-MLfllow.mlflow
MLFLOW_TRACKING_USERNAME=dhruvj94
MLFLOW_TRACKING_PASSWORD=cdf52fd631956ba1e7a49f95f112f217a533fb4a
python script.py


Run this to export as env variables:

# 'export' command is valid only for unix shells. In Windows - use 'set' instead of 'export'


'''
bash
export MLFLOW_TRACKING_URI=https://dagshub.com/dhruvj94/end-to-end-machine-learning-project-with-MLfllow.mlflow
set MLFLOW_TRACKING_URI=https://dagshub.com/dhruvj94/end-to-end-machine-learning-project-with-MLfllow.mlflow

export MLFLOW_TRACKING_USERNAME=dhruvj94
set MLFLOW_TRACKING_USERNAME=dhruvj94

export MLFLOW_TRACKING_PASSWORD=5eb30e6c65eea9caa3e228545bb28e7be166334c
set MLFLOW_TRACKING_PASSWORD=5eb30e6c65eea9caa3e228545bb28e7be166334c

