import numpy as np
import matplotlib.pyplot as plt

from sklearn.svm import OneClassSVM

#from sklearn.experimental import enable_halving_search_cv  # noqa
#from sklearn.model_selection import HalvingGridSearchCV

from calculate_metrics import calculate_metrics

def experiment_oneclass(X_train, y_train, X_test, y_test, settings, mlflow):
    
    for i, setting in enumerate(settings):

        #print(f"experiment_dmkdc {i} setting {setting}")
        with mlflow.start_run(run_name=setting["z_run_name"]):

            model = OneClassSVM(kernel="rbf", gamma=setting["z_gamma"], 
                                nu=setting["z_nu"], tol=setting["z_tol"])
            model.fit(X_train)
            y_test_pred = model.predict(X_test)
            
            y_test = y_test.flatten()
            y_test_pred[ y_test_pred == 1 ] = setting["z_pos_label"]
            y_test_pred[ y_test_pred == -1 ] = setting["z_neg_label"]            

            metrics = calculate_metrics(y_test, y_test_pred)

            mlflow.log_params(setting)
            mlflow.log_metrics(metrics)
            print(f"experiment_dmkdc {i} metrics {metrics}")