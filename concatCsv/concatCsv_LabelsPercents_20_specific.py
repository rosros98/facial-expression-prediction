import glob
import csv

import numpy as np
import pandas as pd

""" CREAZIONE DEL DATASET """
for super_general_csv_dist_path in glob.iglob('../Dataset CK+/Train&Test/ALL_LabelsPercents/**'):
    index_name = []
    arr_super_general_csv_dist_path = super_general_csv_dist_path.split('/')

    if arr_super_general_csv_dist_path[4] == '1' or arr_super_general_csv_dist_path[4] == '2' or \
            arr_super_general_csv_dist_path[4] == '3' or arr_super_general_csv_dist_path[4] == '4' or \
            arr_super_general_csv_dist_path[4] == '5' or arr_super_general_csv_dist_path[4] == '6' or \
            arr_super_general_csv_dist_path[4] == '7':

        # Creo la lista dei nomi delle righe che corrisponde al nome della cartella e sottocartella (es: 010_004)
        for general_csv_dist_path in glob.iglob(super_general_csv_dist_path + '/20/*.csv'):
            arr_general_csv_dist_path = general_csv_dist_path.split('/')
            arr_csv_name = arr_general_csv_dist_path[6].split('_')
            arr_csv_name[0] = arr_csv_name[0].replace('S', '')
            csv_name = '_'.join(arr_csv_name)
            csv_name = csv_name.replace('_labels_percents.csv', '')

            # il nome della riga deve essere ripetuto tante volte quante sono le righe del csv in questione
            file = open(general_csv_dist_path)
            reader = csv.reader(file)
            columns = len(next(reader))
            file.close()
            # print(columns)

            for line in range(columns):
                index_name.append(csv_name)

        #print(index_name)
        #print(len(index_name))

        # Dichiaro un DataFrame
        df = pd.DataFrame()

        # Scorro tutte le cartelle contenenti le distanze globali
        for general_csv_dist_path in glob.iglob(super_general_csv_dist_path + '/20/*.csv'):
            # Trasformo ogni csv in dataframe
            df_csv = pd.read_csv(general_csv_dist_path, header=None)
            df_csv = df_csv.T
            df = pd.concat([df, df_csv])

        # il nome delle righe corrisponde al csv di appartenenza
        df.index = index_name

        # sort data frame
        df.sort_index(ascending=True)

        # Trasformo il DataFrame in una lista così da poterlo scrivere su file
        df_list = df.reset_index().values.tolist()
        print(df_list)

        with open(super_general_csv_dist_path + '_dataset_labels_percents_20.csv', 'w', newline='') as f:
            write = csv.writer(f)
            write.writerows(df_list)
