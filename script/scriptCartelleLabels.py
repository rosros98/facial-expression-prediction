import glob
import shutil

for dist_path in glob.iglob('../Dataset CK+/Distances/**/**/*_labels.csv'):
    arr_dist_path_complete = dist_path.split('/')
    arr_dist_path = dist_path.split('/')
    arr_dist_path[5] = arr_dist_path[5].replace('_labels.csv', '')

    for allemotions_path in glob.iglob('../Dataset CK+/ALL_Emotions/**/*_emotion.txt'):
        arr_allemotions_path = allemotions_path.split('/')
        arr_allemotions_path[4] = arr_allemotions_path[4].replace('_emotion.txt', '')
        final_str_allemotions_path = arr_allemotions_path[4]
        arr_final_str_allemotions_path = final_str_allemotions_path.split('_')
        del arr_final_str_allemotions_path[-1]
        arr_allemotions_path[4] = '_'.join(arr_final_str_allemotions_path)

        #print(arr_dist_path[-1])
        #print(arr_allemotions_path[-1])

        if arr_dist_path[-1] == arr_allemotions_path[-1]:
            print(arr_dist_path[-1])
            print(arr_allemotions_path[-1])

            origin = dist_path
            destination = '../Dataset CK+/ALL_Labels/'+arr_allemotions_path[3]+'/'+arr_dist_path_complete[5]
            shutil.copyfile(origin, destination)

    print(dist_path)
