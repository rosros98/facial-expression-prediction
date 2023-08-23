import glob
import os
import cv2
from mediap_util import TESS
import csv
import mediapipe as mp
import itertools
from scipy.spatial import distance
from landmarks_csv import LANDMARKS_CSV
from distances_csv import DISTANCES_CSV

""" CREAZIONE DEI FILE CSV DEI LANDMARKS """
LANDMARKS_CSV()
""" CREAZIONE DEI FILE CSV DELLE DISTANZE LOCALI E GLOBALI """
DISTANCES_CSV()
