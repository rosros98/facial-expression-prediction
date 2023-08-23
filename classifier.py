import glob
import csv

import cv2
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn import tree
from sklearn import neighbors
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

import time


def classifier(riga_csv_local, riga_csv_global, y_test, nome_imm, nome_frame):
    x_train_local = pd.read_csv("Dataset CK+/Train&Test/ALL_LocalDistances/dataset_local_distances_80.csv", header=None,
                                delimiter=",", index_col=0)
    x_test_local = riga_csv_local
    x_train_global = pd.read_csv("Dataset CK+/Train&Test/ALL_GlobalDistances/dataset_global_distances_80.csv",
                                 header=None, delimiter=",", index_col=0)
    x_test_global = riga_csv_global

    y_train = pd.read_csv("Dataset CK+/Train&Test/ALL_Labels/dataset_labels_80.csv", header=None, delimiter=",",
                          index_col=0)

    start = time.time()

    """ DECISION TREE ALGORITHM 
    classifier_global = tree.DecisionTreeClassifier()
    classifier_local = tree.DecisionTreeClassifier()
    """

    """ KEY NEIGHBORS ALGORITHM 
    classifier_global = neighbors.KNeighborsClassifier()
    classifier_local = neighbors.KNeighborsClassifier()
    """

    """ SVC 
    classifier_global = make_pipeline(StandardScaler(), SVC(gamma='auto'))
    classifier_local = make_pipeline(StandardScaler(), SVC(gamma='auto'))
    """

    """ GAUSSIAN PROCESS CLASSIFIER 
    kernel = 1.0 * RBF(1.0)
    classifier_global = GaussianProcessClassifier(kernel=kernel, random_state=0)
    classifier_local = GaussianProcessClassifier(kernel=kernel, random_state=0)
    """

    """ RANDOM FOREST CLASSIFIER 
    classifier_global = RandomForestClassifier(max_depth=2, random_state=0)
    classifier_local = RandomForestClassifier(max_depth=2, random_state=0)
    """

    """ QUADRATIC DISCRIMINANT ANALYSIS 
    classifier_global = QuadraticDiscriminantAnalysis()
    classifier_local = QuadraticDiscriminantAnalysis()
    """

    """ GAUSSIANNB CLASSIFIER """
    classifier_global = GaussianNB()
    classifier_local = GaussianNB()


    """ ADABOOST CLASSIFIER 
    classifier_global = AdaBoostClassifier(n_estimators=100, random_state=0)
    classifier_local = AdaBoostClassifier(n_estimators=100, random_state=0)
    """

    """ MLP CLASSIFIER 
    classifier_global = MLPClassifier(random_state=1, max_iter=300)
    classifier_local = MLPClassifier(random_state=1, max_iter=300)
    """

    elapsed_time = time.time() - start

    # addestramento del modello - global
    classifier_global.fit(x_train_global, y_train.values.ravel())
    # addestramento del modello - local
    classifier_local.fit(x_train_local, y_train.values.ravel())
    # predizioni - global
    predictions_global = classifier_global.predict(x_test_global)
    # predizioni - local
    predictions_local = classifier_local.predict(x_test_local)
    # stampa dell'accuratezza delle predizioni
    print("ACCURACY - GLOBAL", accuracy_score(y_test, predictions_global))
    print("ACCURACY - LOCAL", accuracy_score(y_test, predictions_local))
    print("PREDICTION - GLOBAL", int(predictions_global))
    print("PREDICTION - LOCAL", int(predictions_local))

    #print(y_test, type(y_test))
    #print(predictions_local, type(predictions_local))

    nome_emozione = "NEUTRAL"
    if int(predictions_local) == 1:
        print("SONO QUI")
        nome_emozione = "ANGER"
    elif int(predictions_local) == 2:
        nome_emozione = "CONTEMPT"
    elif int(predictions_local) == 3:
        nome_emozione = "DISGUST"
    elif int(predictions_local) == 4:
        nome_emozione = "FEAR"
    elif int(predictions_local) == 5:
        nome_emozione = "HAPPINESS"
    elif int(predictions_local) == 6:
        nome_emozione = "SADNESS"
    elif int(predictions_local) == 7:
        nome_emozione = "SURPRISE"


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
        #print(nome_frame_dir)
        if (arr_general_csv_dist_path[2] == arr_nome_imm[0]) and (arr_general_csv_dist_path[3] == arr_nome_imm[1]) and (nome_frame_dir == nome_frame):
            img = cv2.imread(general_csv_dist_path, 0)
            plt.imshow(img, cmap="gray")
            plt.title("EMOTION: {}".format(nome_emozione))
            plt.show()

    print("Elapsed Time: ", elapsed_time)

"""
    x_train = training features
    x_test = testing features
    y_train = training labels
    y_test = testing labels
"""
#x_train_local = pd.read_csv("Dataset CK+/Train&Test/ALL_LocalDistances/dataset_local_distances_80.csv", header=None, delimiter=",", index_col=0)
#x_test_local = pd.read_csv("Dataset CK+/Train&Test/ALL_LocalDistances/dataset_local_distances_20.csv", header=None, delimiter=",", index_col=0)
#x_train_global = pd.read_csv("Dataset CK+/Train&Test/ALL_GlobalDistances/dataset_global_distances_80.csv", header=None, delimiter=",", index_col=0)
#x_test_global = pd.read_csv("Dataset CK+/Train&Test/ALL_GlobalDistances/dataset_global_distances_20.csv", header=None, delimiter=",", index_col=0)
#y_train = pd.read_csv("Dataset CK+/Train&Test/ALL_Labels/dataset_labels_80.csv", header=None, delimiter=",", index_col=0)
#y_test = pd.read_csv("Dataset CK+/Train&Test/ALL_Labels/dataset_labels_20.csv", header=None, delimiter=",", index_col=0)
#
#start = time.time()
#
#""" DECISION TREE ALGORITHM
#classifier_global = tree.DecisionTreeClassifier()
#classifier_local = tree.DecisionTreeClassifier()
#"""
#
#""" KEY NEIGHBORS ALGORITHM
#classifier_global = neighbors.KNeighborsClassifier()
#classifier_local = neighbors.KNeighborsClassifier()
#"""
#
#""" SVC
#classifier_global = make_pipeline(StandardScaler(), SVC(gamma='auto'))
#classifier_local = make_pipeline(StandardScaler(), SVC(gamma='auto'))
#"""
#
#""" GAUSSIAN PROCESS CLASSIFIER
#kernel = 1.0 * RBF(1.0)
#classifier_global = GaussianProcessClassifier(kernel=kernel, random_state=0)
#classifier_local = GaussianProcessClassifier(kernel=kernel, random_state=0)
#"""
#
#""" RANDOM FOREST CLASSIFIER
#classifier_global = RandomForestClassifier(max_depth=2, random_state=0)
#classifier_local = RandomForestClassifier(max_depth=2, random_state=0)
#"""
#
#""" QUADRATIC DISCRIMINANT ANALYSIS
#classifier_global = QuadraticDiscriminantAnalysis()
#classifier_local = QuadraticDiscriminantAnalysis()
#"""
#
#""" GAUSSIANNB CLASSIFIER
#classifier_global = GaussianNB()
#classifier_local = GaussianNB()
#"""
#
#""" ADABOOST CLASSIFIER
#classifier_global = AdaBoostClassifier(n_estimators=100, random_state=0)
#classifier_local = AdaBoostClassifier(n_estimators=100, random_state=0)
#"""
#
#""" MLP CLASSIFIER """
#classifier_global = MLPClassifier(random_state=1, max_iter=300)
#classifier_local = MLPClassifier(random_state=1, max_iter=300)
#
#elapsed_time = time.time() - start
#
## addestramento del modello - global
#classifier_global.fit(x_train_global, y_train.values.ravel())
## addestramento del modello - local
#classifier_local.fit(x_train_local, y_train.values.ravel())
## predizioni - global
#predictions_global = classifier_global.predict(x_test_global)
## predizioni - local
#predictions_local = classifier_local.predict(x_test_local)
## stampa dell'accuratezza delle predizioni
#print("ACCURACY - GLOBAL")
#print(accuracy_score(y_test, predictions_global))
#print("ACCURACY - LOCAL")
#print(accuracy_score(y_test, predictions_local))
#
#print(elapsed_time)
