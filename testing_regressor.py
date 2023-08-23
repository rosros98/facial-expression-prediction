import csv
import glob
import cv2
import pandas as pd
from matplotlib import pyplot as plt

from regressor import regressor

cont = 0
emozione = 0
# Prendo in input dall'utente varie informazioni:
# nome_imm = input('Inserisci il nome dell\'immagine: ')
# nome_frame = input('Inserisci il nome del frame: ')
# emozione = input('Inserisci l\'emozione:\n ')

# Per testare velocemente:
nome_imm = "130_007"
nome_frame = "5"
emozione = "1"

# Per praticità, si sceglie un'imm già contenuta nel test set (normalmente andrebbe presa la riga nel file unico delle distanze, ma in questo caso potrebbe trovarsi nel training set)
# path del csv contenente le distanze locali dell'imm
path = "Dataset CK+/Train&Test/ALL_LocalDistances/1_dataset_local_distances_20.csv"
# path del csv contenente la label rappresentante la percentuale di emozione del soggetto (serve per calcolare gli errori in seguito)
path_y_test = "Dataset CK+/Train&Test/ALL_LabelsPercents/1_dataset_labels_percents_20.csv"

# sostituisco nei path l'emozione indicata
path = path.replace("1", emozione)
path_y_test = path_y_test.replace("1", emozione)
# se non è stata inserita un'emozione tra 1 e 7, allora termina
if int(emozione) < 1 or int(emozione) > 7:
    print('Emozione non presente')
    exit(0)

# prelevo la riga di interesse in base al nome inserito sia nel csv delle distanze locali che in quello delle labels
with open(path, newline="") as filecsv, open(path_y_test, newline="") as filecsv_y_test:
    reader = csv.reader(filecsv)
    reader_y_test = csv.reader(filecsv_y_test)
    for row, row_y_test in zip(reader, reader_y_test):
        # se l'index della riga (nome imm) coincide con il nome dell'imm...
        if row[0] == nome_imm:
            # incremento il contatore del frame
            cont = cont + 1
            # se il contatore coincide con il numero del frame...
            if cont == int(nome_frame):
                # salvo le righe
                riga_csv = row
                riga_csv_y_test = row_y_test
                # cancello il primo elemento della riga dato che è un index (=nome imm)
                del riga_csv[0]
                del riga_csv_y_test[0]
                # trasformo la riga delle distanze in dataframe (come lo vuole la funzione regressore())
                riga_csv = pd.DataFrame(riga_csv)
                # traspongo il dataframe in modo da avere una lista orizzontale
                riga_csv = riga_csv.T
                # print(riga_csv)
                # print(riga_csv_y_test)


                # chiamo la funzione passandogli la riga delle distanze dell'imm e la percentuale di emozione relativa
                regressor(riga_csv, riga_csv_y_test, emozione, nome_imm, nome_frame)

