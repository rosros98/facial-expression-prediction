La cartella Dataset CK+ già contiene i dataset opportuni per il classificatore e il repressore, quindi si può eseguire il codice a partire dal punto 12.

Ordine di esecuzione codici:
1. landmarks_csv
2. distances_csv
3. scriptCartelleGlobalDistances
4. scriptCartelleLocalDistances
5. create_labels
6. create_labels_classifier
7. scriptCartelleLabels 
8. scriptCartelleLabelsPercents
9. scriptCartelleEmotions
10. concatCsv_* (8 file)
11. concatCsv_*_specific (6 file)
12. testing_classifier
13. testing_regressor

Per testare il programma velocemente, nei codici testing_classifier e testing_regressor si possono inserire direttamente il nome dell'immagine, il numero del frame e l'emozione (quest'ultima solo per il regressore).
Idealmente queste informazioni vanno inserite dall'utente, infatti il codice inerente a questa funzionalità è commentato dalla riga 7 alla 9 in testing_classifier e dalla riga 11 alla 14 in testing_regressor.