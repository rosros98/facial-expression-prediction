import glob
import csv

import pandas as pd

""" CREAZIONE DEL DATASET """
index_name = []
# Creo la lista dei nomi delle righe che corrisponde al nome della cartella e sottocartella (es: 010_004)
for general_csv_dist_path in glob.iglob('../Dataset CK+/Train&Test/ALL_GlobalDistances/**/20/*.csv'):
    arr_general_csv_dist_path = general_csv_dist_path.split('/')
    arr_csv_name = arr_general_csv_dist_path[6].split('_')
    arr_csv_name[0] = arr_csv_name[0].replace('S', '')
    csv_name = '_'.join(arr_csv_name)
    csv_name = csv_name.replace('_global_distances.csv', '')

    # il nome della riga deve essere ripetuto tante volte quante sono le righe del csv in questione
    file = open(general_csv_dist_path)
    reader = csv.reader(file)
    lines = len(list(reader))
    file.close()
    #print(lines)

    for line in range(lines):
        index_name.append(csv_name)

#print(index_name)
#print(len(index_name))

# Dichiaro un DataFrame
df = pd.DataFrame()

# Scorro tutte le cartelle contenenti le distanze globali
for general_csv_dist_path in glob.iglob('../Dataset CK+/Train&Test/ALL_GlobalDistances/**/20/*.csv'):
    # Trasformo ogni csv in dataframe
    df_csv = pd.read_csv(general_csv_dist_path, header=None)
    df = pd.concat([df, df_csv])

# il nome delle righe corrisponde al csv di appartenenza
df.index = index_name

# Trasformo il DataFrame in una lista così da poterlo scrivere su file
df_list = df.reset_index().values.tolist()
#print(df_list)

with open('../Dataset CK+/Train&Test/ALL_GlobalDistances/dataset_global_distances_20.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerows(df_list)
