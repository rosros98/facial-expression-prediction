import glob
import numpy as np
import pandas as pd

""" CREAZIONE DEI FILE CSV DELLE DISTANZE GLOBALI (tra il primo frame e tutti gli altri) """
# def DISTANCES_CSV():
for general_csv_land_path in glob.iglob('Dataset CK+/Landmarks/**/**'):

    # Contatore che tiene traccia del numero di csv in ogni cartella, va azzerato ogni volta che si cambia cartella (qui è utile solo per una print messa a commento)
    cont_csv = 0
    # Array contenente tutti i path di una cartella specifica (es: S111/001/*_landmarks.csv), serve per l'ordinamento dei csv da confrontare
    arr_specific_csv_land_path = []

    # arr_ALL_csv_globdist_path = array contenente le singole parti del path in questione delle distanze globali
    arr_ALL_csv_globdist_path = general_csv_land_path.split('/')
    arr_ALL_csv_globdist_path[1] = 'Distances'
    # arr_ALL_csv_locdist_path  = è una copia di arr_ALL_csv_globdist_path, ma riguarda le distanze locali
    arr_ALL_csv_locdist_path = arr_ALL_csv_globdist_path.copy()
    arr_ALL_csv_globdist_path.append(
        str(arr_ALL_csv_globdist_path[2]) + '_' + str(arr_ALL_csv_globdist_path[3]) + '_' + 'global_distances.csv')
    arr_ALL_csv_locdist_path.append(
        str(arr_ALL_csv_globdist_path[2]) + '_' + str(arr_ALL_csv_globdist_path[3]) + '_' + 'local_distances.csv')
    # Path del csv che conterrà tutte le distanze globali unite
    ALL_csv_globdist_path = '/'.join(arr_ALL_csv_globdist_path)
    # Path del csv che conterrà tutte le distanze locali unite
    ALL_csv_locdist_path = '/'.join(arr_ALL_csv_locdist_path)
    # print(ALL_csv_locdist_path)
    # print(ALL_csv_globdist_path)

    for specific_csv_land_path in glob.iglob(general_csv_land_path + '/*.csv'):
        # Inserisco nell'array il path in questione per i landmark
        arr_specific_csv_land_path.append(specific_csv_land_path)
        # Incremento il contatore
        cont_csv = cont_csv + 1

    # cont_csv = numero di csv totali nella cartella specifica (es: S111/001 = 14 csv)
    # print(str(cont_csv) + ' --> ' + general_csv_land_path)

    # Ordino in modo crescente i file nell'array in modo da poterlo manipolare in seguito
    arr_specific_csv_land_path.sort()

    # Azzero il contatore in modo da poterlo ri-utilizzare nel seguente ciclo for
    cont_csv = 0
    # Azzero la lista contenente il nome della colonna
    nome_colonna = []

    """ L'inserimento delle distanze nei rispettivi csv avviene all'interno dell'else e non nell'if
        dato che comunque a prescindere il codice entrerà nell'else poichè c'è sempre più di un frame nelle cartelle"""
    # Scorro tutti i csv nella cartella specifica (i rappresenta il path i-esimo)
    for i in arr_specific_csv_land_path:
        # print(arr_i)
        # Alla lista aggiungo il nome della colonna, cioè la cartella e sottocartella relativa al frame (es: S022_001 -> 022001)
        nome_colonna.append(str(arr_ALL_csv_globdist_path[2]).replace('S', '') + str(arr_ALL_csv_globdist_path[3]))
        # print(nome_colonna)
        # print(i)
        # Se sto analizzando il primo csv, questo deve contenere tutte le distanze pari a 0 (distanze con se stesso)
        if cont_csv == 0:
            # Creo un DataFrame di 468 elementi (matrice 468x1) posti a 0, sia per le dist locali che globali
            df_ALL_glob = pd.DataFrame(np.zeros((468, 1)))
            df_ALL_loc = pd.DataFrame(np.zeros((468, 1)))
            # print(df_ALL_glob)
            # print(df_ALL_loc)
            # print("DONE --> "+i)

            """ Altrimenti si deve effettuare la differenza con il primo csv per le globali e
                con il csv precedente per le locali """
        else:
            """ i = path corrente (curr)
                arr_specific_csv_land_path[0] = path del primo (first)
                arr_specific_csv_land_path[cont_csv-1] = path precedente (prev) """

            """ Trasformo in DataFrame i csv di curr_csvfile, di prev_csvfile e di first_csvfile 
                (considerando la prima riga non come titolo, ma come riga vera e propria) """
            df_curr = pd.read_csv(i, header=None)
            df_first = pd.read_csv(arr_specific_csv_land_path[0], header=None)
            df_prev = pd.read_csv(arr_specific_csv_land_path[cont_csv - 1], header=None)
            # print(df_curr)
            # print(df_first)
            # printf(df_prev)

            # Calcolo le distanze euclidee globali e locali
            for index, row in df_curr.iterrows():
                distanza_globale = np.sqrt(np.square(df_first).sum(axis=1))
                distanza_locale = np.sqrt(np.square(df_prev).sum(axis=1))
            # print(distanza_globale)
            # print(distanza_locale)

            # Accodo al DataFrame finale la colonna di dist globali calcolate convertita da tipo Series a DataFrame
            df_ALL_glob[cont_csv] = distanza_globale.to_frame()
            # print(df_ALL_glob)
            # Accodo al DataFrame finale la colonna di dist locali calcolate convertita da tipo Series a DataFrame
            df_ALL_loc[cont_csv] = distanza_locale.to_frame()
            # print(df_ALL_loc)

        # Incremento il contatore dei file csv nella cartella specifica
        cont_csv = cont_csv + 1

    # Scrivo il DataFrame contenente tutte le distanze globali all'interno del file csv corrispondente
    # Nomino le colonne
    df_ALL_glob.columns = nome_colonna
    # Traspongo
    df_ALL_glob = df_ALL_glob.T
    # header = True per memorizzare come riga il nome delle colonne
    df_ALL_glob.to_csv(ALL_csv_globdist_path, mode='w', index=False, header=None)
    # print(df_ALL_glob)
    df_ALL_loc.columns = nome_colonna
    # Traspongo
    df_ALL_loc = df_ALL_loc.T
    # Scrivo il DataFrame contenente tutte le distanze locali all'interno del file csv corrispondente
    df_ALL_loc.to_csv(ALL_csv_locdist_path, mode='w', index=False, header=None)
    # print(df_ALL_loc)

    print("Data appended in " + ALL_csv_globdist_path + " and in " + ALL_csv_locdist_path)
