import csv
import glob
import shutil

""" CREAZIONE DELLE ETICHETTE PER IL CLASSIFICATORE """
for general_csv_dist_path_class in glob.iglob('Dataset CK+/Distances/**/**/*_labels.csv'):

    arr_general_csv_dist_path_class = general_csv_dist_path_class.split('/')
    arr_general_csv_dist_path = arr_general_csv_dist_path_class.copy()
    arr_general_csv_dist_path[4] = arr_general_csv_dist_path[4].replace("_labels.csv", "_labels_percents.csv")

    general_csv_dist_path_class = '/'.join(arr_general_csv_dist_path_class)
    general_csv_dist_path = '/'.join(arr_general_csv_dist_path)

    # print("classifier\t-->\t" + general_csv_dist_path_class)
    # print("original\t-->\t" + general_csv_dist_path)
    shutil.copyfile(general_csv_dist_path_class, general_csv_dist_path)

    arr_stringa = arr_general_csv_dist_path[4].split('_')

    i = 0
    count_row = 0

    # general_csv_dist_path = file contenente le labels originali, general_csv_dist_path_class = labels per il classificatore
    with open(general_csv_dist_path, 'r') as csvfile, open(general_csv_dist_path_class, 'w') as csvfile_class:
        reader = csv.reader(csvfile)
        writer = csv.writer(csvfile_class)
        data = list(reader)
        #print(data)

        for row in data:
            count_row = count_row + 1

        # Se è stato memorizzato l'header, va saltato
        if count_row > 1:
            for col in data[1]:
                if float(col) <= 20:
                    data[1][i] = 0
                else:
                    for all_emotions_path in glob.iglob('Dataset CK+/ALL_Emotions/**/*.txt'):
                        arr_all_emotions_path = all_emotions_path.split('/')
                        stringa_emotions = arr_all_emotions_path[3].split('_')
                        if (arr_stringa[0] == stringa_emotions[0]) and (arr_stringa[1] == stringa_emotions[1]):
                            data[1][i] = arr_all_emotions_path[2]

                i = i + 1
        else:
            for col in data[0]:
                if float(col) <= 20:
                    data[0][i] = 0
                else:
                    for all_emotions_path in glob.iglob('Dataset CK+/ALL_Emotions/**/*.txt'):
                        arr_all_emotions_path = all_emotions_path.split('/')
                        stringa_emotions = arr_all_emotions_path[3].split('_')
                        if (arr_stringa[0] == stringa_emotions[0]) and (arr_stringa[1] == stringa_emotions[1]):
                            arr_all_emotions_path[2] = int(arr_all_emotions_path[2])
                            if isinstance(arr_all_emotions_path[2], int):
                                data[0][i] = arr_all_emotions_path[2]
                            else:
                                print('Emozione non presente')

                i = i + 1

        writer.writerows(data)
        #print(f"************ {i} ************")
        #print(general_csv_dist_path_class)
        #print(data)

    print(general_csv_dist_path_class)
