import csv
import glob
from Normalization import NORMALIZATION

""" CREAZIONE DELLE ETICHETTE """
# def CREATE_LABELS():
for general_csv_dist_path in glob.iglob('Dataset CK+/Landmarks/**/**'):
    # Contatore che tiene traccia del numero di csv in ogni cartella, va azzerato ogni volta che si cambia cartella
    cont_csv = 0
    arr_cont_csv = []

    for specific_csv_dist_path in glob.iglob(general_csv_dist_path + '/*.csv'):
        arr_cont_csv.append(cont_csv)
        # Incremento il contatore
        cont_csv = cont_csv + 1

    # Creo un array contenente per ogni cella le parti relative al path
    arr_labels_path = general_csv_dist_path.split('/')
    arr_labels_path[1] = 'Distances'
    arr_labels_path.append(str(arr_labels_path[2])+'_'+str(arr_labels_path[3])+'_'+'labels.csv')
    # Dato che sono stringhe staccate all'interno di un array, bisogna unire il tutto come unica stringa
    labels_path = '/'.join(arr_labels_path)
    # print(labels_path)

    # Eseguo un rescaling in base al numero di elementi e calcolo le percentuali
    labels = NORMALIZATION(cont_csv)
    #print(cont_csv)
    #print(labels)

    with open(labels_path, 'w') as csvfile:
        write = csv.writer(csvfile)
        #write.writerow(arr_cont_csv)
        write.writerows([labels])

    print("Data created in " + labels_path)
