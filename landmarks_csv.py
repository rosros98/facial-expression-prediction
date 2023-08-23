import glob
import cv2
from mediap_util import TESS
import pandas as pd

""" CREAZIONE DEI FILE CSV DEI LANDMARKS """
# def LANDMARKS_CSV():
# Scorro tutti i png per cartelle e sottocartelle
for filepath in glob.iglob('Dataset CK+/cohn-kanade-images/**/**/*.png'):
    """ imm_path = array contenente ogni parola del file path:
                • imm_path[0] = "Dataset CK+"
                • imm_path[1] = "cohn-kanade-images"
                • imm_path[2] = nome prima cartella (es: S110)
                • imm_path[3] = nome seconda cartella (es: 001)
                • imm_path[4] = nome immagine """
    imm_path = filepath.split('/')
    # Creo il path per i landmarks
    landmarks_path = imm_path
    landmarks_path[1] = 'Landmarks'
    landmarks_path[4] = landmarks_path[4].replace(".png", "_landmarks.csv")
    # print(landmarks_path)
    # Dato che sono stringhe staccate all'interno di un array, bisogna unire il tutto come unica stringa
    csv_land_path = '/'.join(landmarks_path)
    # print(csv_land_path)

    # Leggo l'immagine
    img = cv2.imread(filepath)

    # Catturo le coordinate dei landmark
    (n, coords) = TESS(img)
    # print(coords)

    # coords da tipo lista viene trasformato in tipo DataFrame con colonne nominate x, y, z
    df_coords = pd.DataFrame(coords, columns=['x', 'y', 'z'])
    # print(df_coords)

    # contents = DataFrame sotto forma di csv
    contents = df_coords.to_csv(index=False, header=False)
    # Apro/Creo il file
    csvfile = open(csv_land_path, 'w')
    # Scrivo nel file il DataFrame
    csvfile.write(contents)
    # Chiudo il file
    csvfile.close()
    print("OK: "+csv_land_path)

print("DONE")
