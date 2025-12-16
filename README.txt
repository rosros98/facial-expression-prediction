# Facial Expression Prediction

This project focuses on the **regression and classification of facial expressions** using Machine Learning techniques and facial landmark extraction.  
The goal is to predict the **predominant emotion displayed on a person’s face** by analyzing both **macro-expressions** and **micro-expressions**.

## Project Overview

The system uses the **MediaPipe Face Mesh** framework to extract **468 3D facial landmarks** for each detected face.  
From these landmarks, **local and global Euclidean distances** are computed to model facial movements and expressions.

These features are then used to train and evaluate multiple **Machine Learning algorithms** for emotion prediction, both in classification and regression settings.

## Technologies & Tools

- **Language:** Python
- **Libraries:**
  - MediaPipe (facial landmark extraction)
  - pandas (data manipulation and preprocessing)
  - numpy
  - scikit-learn (machine learning algorithms)
- **ML Algorithms:**
  - Decision Tree
  - Random Forest
  - K-Nearest Neighbors (KNN)
  - Support Vector Classifier (SVC)
  - Gaussian Naive Bayes

## Facial Landmark Extraction & Feature Engineering

- **MediaPipe Face Mesh** extracts **468 3D facial landmarks**
- Landmarks are used to compute:
  - **Global Euclidean distances** (macro-expressions)
  - **Local Euclidean distances** (micro-expressions)
- These distances define the feature space used for training the models

## Dataset Information

The folder **`Dataset CK+`** already contains the datasets required for both:
- the **classifier**
- the **regressor**

Therefore, it is possible to **run the code directly starting from step 12**, without regenerating the entire dataset pipeline.

## Code Execution Order

To generate the complete dataset and train the models from scratch, the scripts should be executed in the following order:

1. `landmarks_csv`  
2. `distances_csv`  
3. `scriptCartelleGlobalDistances`  
4. `scriptCartelleLocalDistances`  
5. `create_labels`  
6. `create_labels_classifier`  
7. `scriptCartelleLabels`  
8. `scriptCartelleLabelsPercents`  
9. `scriptCartelleEmotions`  
10. `concatCsv_*` (8 files)  
11. `concatCsv_*_specific` (6 files)  
12. `testing_classifier`  
13. `testing_regressor`  

## Fast Testing Mode

To quickly test the system, the scripts:
- `testing_classifier`
- `testing_regressor`

allow **manual insertion** of:
- image name
- frame number
- emotion label (only for the regressor)

This enables rapid testing without rebuilding the full pipeline.

### User Input vs Hardcoded Testing

- The code for **user input** is already implemented but **commented out**
- For testing purposes, parameters can be hardcoded directly in the scripts

Specifically:
- In `testing_classifier`, user input code is commented from **line 7 to line 9**
- In `testing_regressor`, user input code is commented from **line 11 to line 14**

Ideally, these values should be provided by the user, but hardcoding allows faster experimentation.
