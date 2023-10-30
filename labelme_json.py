import os

labelme_path = 'C:\\Users\\CGJWW93\\Desktop\\labelme\\custom_data\\annotations_labelme_mask' 

json_file = os.listdir(labelme_path)

# os.system("conda activate labelme")

for file in json_file:
    file_path = os.path.join(labelme_path, file)
    os.system("labelme_json_to_dataset %s"%(file_path))

