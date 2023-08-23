import csv
import pandas as pd

from classifier import classifier

cont = 0
# Prendo in input dall'utente varie informazioni:
# nome_imm = input('Inserisci il nome dell\'immagine: ')
# nome_frame = input('Inserisci il nome del frame: ')

# Per testare velocemente:
nome_imm = "160_006"
nome_frame = "10"

# Per praticità, si sceglie un'imm già contenuta nel test set (normalmente andrebbe presa la riga nel file unico delle distanze, ma in questo caso potrebbe trovarsi nel training set)
# path del csv contenente le distanze locali dell'imm
path_local = "Dataset CK+/Train&Test/ALL_LocalDistances/dataset_local_distances_20.csv"
path_global = "Dataset CK+/Train&Test/ALL_GlobalDistances/dataset_global_distances_20.csv"

# path del csv contenente la label rappresentante l'emozione del soggetto (serve per calcolare gli errori in seguito)
path_y_test = "Dataset CK+/Train&Test/ALL_Labels/dataset_labels_20.csv"

# prelevo la riga di interesse in base al nome inserito sia nel csv delle distanze locali che in quello delle labels
with open(path_local, newline="") as filecsv_local, open(path_global, newline="") as filecsv_global, open(path_y_test,
                                                                                                          newline="") as filecsv_y_test:
    reader_local = csv.reader(filecsv_local)
    reader_global = csv.reader(filecsv_global)
    reader_y_test = csv.reader(filecsv_y_test)
    for row_local, row_global, row_y_test in zip(reader_local, reader_global, reader_y_test):
        # se l'index della riga (nome imm) coincide con il nome dell'imm...
        if row_local[0] == nome_imm:
            # incremento il contatore del frame
            cont = cont + 1
            # se il contatore coincide con il numero del frame...
            if cont == int(nome_frame):
                # salvo le righe
                riga_csv_local = row_local
                riga_csv_global = row_global
                riga_csv_y_test = row_y_test
                # cancello il primo elemento della riga dato che è un index (=nome imm)
                del riga_csv_local[0]
                del riga_csv_global[0]
                del riga_csv_y_test[0]
                # trasformo la riga delle distanze in dataframe (come lo vuole la funzione regressore())
                riga_csv_local = pd.DataFrame(riga_csv_local)
                riga_csv_global = pd.DataFrame(riga_csv_global)
                # traspongo il dataframe in modo da avere una lista orizzontale
                riga_csv_local = riga_csv_local.T
                riga_csv_global = riga_csv_global.T
                # print(riga_csv)
                # print(riga_csv_y_test)

                # chiamo la funzione passandogli la riga delle distanze dell'imm e la percentuale di emozione relativa
                classifier(riga_csv_local, riga_csv_global, riga_csv_y_test, nome_imm, nome_frame)
