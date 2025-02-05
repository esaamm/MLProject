import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):  # It saves the data transformation pickle file into the harddisk.
    try:
        dir_path = os.path.dirname(file_path) # dirname finds the path of directory in which a file is +nt if I give the complete path of a file.

        os.makedirs(dir_path, exist_ok=True)  # Creates the directory if dir_path directory is not present. 

        with open(file_path, "wb") as file_obj: # The file at file_path location is opened in write binary 'wb' mode. 
            pickle.dump(obj, file_obj)  # This line stores the object obj to the file represented by file_obj name.

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]] # Doing Hyperparameter Tuning

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            # model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            # model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
    
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj: # The file at file_path location is opened in read binary mode.
            return pickle.load(file_obj)  # This line converts file_obj which is a binary pickle file into a normal file. We convert a file into a binary file which is in the form of data bytes so that any file can be transmitted/stored in a hard disk . 

    except Exception as e:
        raise CustomException(e, sys)  