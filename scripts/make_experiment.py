from experiment_dmkde import experiment_dmkde
from experiment_dmkde_sgd import experiment_dmkde_sgd
from experiment_lof import experiment_lof
from experiment_oneclass import experiment_oneclass
from experiment_isolation import experiment_isolation
from experiment_covariance import experiment_covariance
from experiment_lake import experiment_lake

# Uncomment the following line when running a Pyod notebook
# Keep it commented otherwise
from experiment_pyod import experiment_pyod

def make_experiment(algorithm, X_train, y_train, X_test, y_test, settings, mlflow):
    
    if algorithm == "oneclass":
        experiment_oneclass(X_train, y_train, X_test, y_test, settings, mlflow)
    if algorithm == "isolation":
        experiment_isolation(X_train, y_train, X_test, y_test, settings, mlflow)
    if algorithm == "covariance":
        experiment_covariance(X_train, y_train, X_test, y_test, settings, mlflow)
    if algorithm == "localoutlier":
        experiment_lof(X_train, y_train, X_test, y_test, settings, mlflow)
    if algorithm == "dmkde":
        experiment_dmkde(X_train, y_train, X_test, y_test, settings, mlflow)
    if algorithm == "dmkde_sgd":
        experiment_dmkde_sgd(X_train, y_train, X_test, y_test, settings, mlflow)
    if algorithm == "lake":
        experiment_lake(X_train, y_train, X_test, y_test, settings, mlflow)
    if algorithm.startswith("pyod"):
        experiment_pyod(X_train, y_train, X_test, y_test, settings, mlflow)
