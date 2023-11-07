import os 

labelme_json_path = 'C:\\Users\\20272\\Desktop\\project\\custom_data\\annotations_labelme_v2_noignorelabel'

json_file = os.listdir(labelme_json_path)

for file in json_file:
    file_path = os.path.join(labelme_json_path, file)
    os.system("labelme_json_to_dataset %s"%(file_path))