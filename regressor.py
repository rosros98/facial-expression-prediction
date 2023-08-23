import glob

import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import svm, metrics
from sklearn.cross_decomposition import PLSRegression
from sklearn.decomposition import PCA
from sklearn.feature_selection import r_regression
from sklearn.linear_model import LinearRegression, Ridge, RidgeCV, SGDRegressor, HuberRegressor, \
    PassiveAggressiveRegressor, Lasso, LassoLars, OrthogonalMatchingPursuit, LogisticRegression, Perceptron
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn import linear_model

from scipy.special import loggamma
from scipy.special import expit, logit

import time

"""
    x_train = training features
    x_test = testing features
    y_train = training labels
    y_test = testing labels
"""


def regressor(riga_csv, y_test, emozione, nome_imm, nome_frame):
    if emozione == "1":
        nome_emozione = "ANGER"
    elif emozione == "2":
        nome_emozione = "CONTEMPT"
    elif emozione == "3":
        nome_emozione = "DISGUST"
    elif emozione == "4":
        nome_emozione = "FEAR"
    elif emozione == "5":
        nome_emozione = "HAPPINESS"
    elif emozione == "6":
        nome_emozione = "SADNESS"
    elif emozione == "7":
        nome_emozione = "SURPRISE"

    x_train_local = pd.read_csv("Dataset CK+/Train&Test/ALL_LocalDistances/1_dataset_local_distances_80.csv",
                                header=None, delimiter=",", index_col=0)
    x_train_local = x_train_local.replace("1", emozione)
    # x_test_local = csv pari alla riga corrispondente al nome dell'imm
    x_test_local = riga_csv
    y_train = pd.read_csv("Dataset CK+/Train&Test/ALL_LabelsPercents/1_dataset_labels_percents_80.csv", header=None,
                          delimiter=",", index_col=0)
    y_train = y_train.replace("1", emozione)
    y_train = y_train.to_numpy()

    start = time.time()

    """ Linear - LINEAR REGRESSOR """
    # regressor_local = LinearRegression()

    """ PLS REGRESSOR """
    # n_components = Number of components to keep. Should be in [1, min(n_samples, n_features, n_targets)]
    # regressor_local = PLSRegression(n_components=1)

    """ OrthogonalMatchingPursuit """
    # n_nonzero_coefs = 17
    # regressor_local = OrthogonalMatchingPursuit(n_nonzero_coefs=n_nonzero_coefs, normalize=False)

    """ Bayesian regressors - ARD REGRESSOR """
    # regressor_local = linear_model.ARDRegression()

    """ Bayesian regressors - BAYESIAN RIDGE REGRESSOR """
    # regressor_local = linear_model.BayesianRidge()

    """ Generalized linear models for regression - POISSON REGRESSOR """
    # regressor_local = linear_model.PoissonRegressor()

    """ Generalized linear models for regression - TWEEDIE REGRESSOR """
    regressor_local = linear_model.TweedieRegressor()

    # addestramento del modello per il regressore
    regressor_local.fit(x_train_local, y_train)
    y_pred_local = regressor_local.predict(x_test_local)
    elapsed_time = time.time() - start
    # stampa del predict
    print("PREDICT REGRESSOR - LOCAL -", nome_emozione)
    print(y_pred_local)
    diff_local_MAE = metrics.mean_absolute_error(y_test, y_pred_local)
    diff_local_MSE = metrics.mean_squared_error(y_test, y_pred_local)
    diff_local_RMSE = np.sqrt(metrics.mean_squared_error(y_test, y_pred_local))
    print('Mean Absolute Error: ', diff_local_MAE)
    print('Mean Squared Error: ', diff_local_MSE)
    print('Root Mean Squared Error: ', diff_local_RMSE)

    # stampo a video l'immagine
    arr_nome_imm = nome_imm.split("_")
    arr_nome_imm[0] = arr_nome_imm[0].replace(arr_nome_imm[0], "S" + arr_nome_imm[0])
    for general_csv_dist_path in glob.iglob("Dataset CK+/cohn-kanade-images/S*/*/*.png"):
        arr_general_csv_dist_path = general_csv_dist_path.split("/")
        arr_nome_frame_dir = arr_general_csv_dist_path[4].split("_")
        nome_frame_dir = arr_nome_frame_dir[2]
        nome_frame_dir = nome_frame_dir.replace(".png", "")
        nome_frame_dir = int(nome_frame_dir)
        nome_frame_dir = str(nome_frame_dir)
        # print(nome_frame_dir)
        if (arr_general_csv_dist_path[2] == arr_nome_imm[0]) and (arr_general_csv_dist_path[3] == arr_nome_imm[1]) and (
                nome_frame_dir == nome_frame):
            img = cv2.imread(general_csv_dist_path, 0)
            plt.imshow(img, cmap="gray")
            plt.title("{} - {}%".format(nome_emozione, y_pred_local))
            plt.show()

    print("Elapsed Time: ", elapsed_time)

#""" TEST REGRESSORE SU TUTTO IL TEST SET 20% """
#x_train_local = pd.read_csv("Dataset CK+/Train&Test/ALL_LocalDistances/1_dataset_local_distances_80.csv",
#                            header=None, delimiter=",", index_col=0)
## x_test_local = csv pari alla riga corrispondente al nome dell'imm
#x_test_local = pd.read_csv("Dataset CK+/Train&Test/ALL_LocalDistances/1_dataset_local_distances_20.csv", header=None,
#                           delimiter=",", index_col=0)
#y_train = pd.read_csv("Dataset CK+/Train&Test/ALL_LabelsPercents/1_dataset_labels_percents_80.csv", header=None,
#                      delimiter=",", index_col=0)
#y_train = y_train.to_numpy()
## y_test = riga corrispondente al nome del frame
#y_test = pd.read_csv("Dataset CK+/Train&Test/ALL_LabelsPercents/1_dataset_labels_percents_20.csv", header=None,
#                     delimiter=",", index_col=0)
#start = time.time()
#""" Linear - LINEAR REGRESSOR """
## regressor_local = LinearRegression()
#
#""" PLS REGRESSOR """
## n_components = Number of components to keep. Should be in [1, min(n_samples, n_features, n_targets)]
## regressor_local = PLSRegression(n_components=1)
#
#""" OrthogonalMatchingPursuit """
## n_nonzero_coefs = 17
## regressor_local = OrthogonalMatchingPursuit(n_nonzero_coefs=n_nonzero_coefs, normalize=False)
#
#""" Bayesian regressors - ARD REGRESSOR """
#regressor_local = linear_model.ARDRegression()
#
#""" Bayesian regressors - BAYESIAN RIDGE REGRESSOR """
## regressor_local = linear_model.BayesianRidge()
#
#""" Generalized linear models for regression - POISSON REGRESSOR """
## regressor_local = linear_model.PoissonRegressor()
#
#""" Generalized linear models for regression - TWEEDIE REGRESSOR """
## regressor_local = linear_model.TweedieRegressor()
#
## addestramento del modello per il regressore
#regressor_local.fit(x_train_local, y_train)
#
## stampa del predict
#print("PREDICT REGRESSOR - LOCAL - RABBIA")
#y_pred_local = regressor_local.predict(x_test_local)
#elapsed_time = time.time() - start
#print(y_pred_local)
#print("shape y_pred_local: ", y_pred_local.shape)
#
#diff_local_MAE = metrics.mean_absolute_error(y_test, y_pred_local)
#diff_local_MSE = metrics.mean_squared_error(y_test, y_pred_local)
#diff_local_RMSE = np.sqrt(metrics.mean_squared_error(y_test, y_pred_local))
#print('\nMean Absolute Error: ', diff_local_MAE)
#print('Mean Squared Error: ', diff_local_MSE)
#print('Root Mean Squared Error: ', diff_local_RMSE)
#
#print("Elapsed Time: ", elapsed_time)
