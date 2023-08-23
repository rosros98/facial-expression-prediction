import glob
import shutil

for general_csv_dist_path in glob.iglob('../Dataset CK+/Emotion/**/**/*_emotion.txt'):
    original = general_csv_dist_path
    arr_path = general_csv_dist_path.split('/')

    with open(general_csv_dist_path) as f:
        lines = f.readlines()
    # print(lines[0])

    if lines[0] == '   1.0000000e+00\n':
        shutil.copyfile(original, '../Dataset CK+/ALL_Emotions/1/' + arr_path[5])
    elif lines[0] == '   2.0000000e+00\n':
        shutil.copyfile(original, '../Dataset CK+/ALL_Emotions/2/' + arr_path[5])
    elif lines[0] == '   3.0000000e+00\n':
        shutil.copyfile(original, '../Dataset CK+/ALL_Emotions/3/' + arr_path[5])
    elif lines[0] == '   4.0000000e+00\n':
        shutil.copyfile(original, '../Dataset CK+/ALL_Emotions/4/' + arr_path[5])
    elif lines[0] == '   5.0000000e+00\n':
        shutil.copyfile(original, '../Dataset CK+/ALL_Emotions/5/' + arr_path[5])
    elif lines[0] == '   6.0000000e+00\n':
        shutil.copyfile(original, '../Dataset CK+/ALL_Emotions/6/' + arr_path[5])
    elif lines[0] == '   7.0000000e+00\n':
        shutil.copyfile(original, '../Dataset CK+/ALL_Emotions/7/' + arr_path[5])

    #print(general_csv_dist_path)
