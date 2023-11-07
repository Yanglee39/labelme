import os

def rename_label_files(root_path, new_folder_path):
    # 获取总文件中所有的子文件夹
    subfolders = [f.path for f in os.scandir(root_path) if f.is_dir()]      # 得到的是一维列表

    # 遍历每个子文件夹
    for subfolder in subfolders:
        # 构建新文件文件名
       folder_name = os.path.basename(subfolder)
       index = folder_name.find("_json")
       new_name = folder_name[:index] + ".png"

        # 构建旧文件的完整路径
       old_file_path = os.path.join(subfolder, "label.png")

        # 构建新文件的完整路径
       new_file_path = os.path.join(new_folder_path, new_name)
       
        # 重命名文件
       os.rename(old_file_path, new_file_path)

       print(f'Renamed: {old_file_path} to {new_file_path}')

# 指定总文件夹路径
root_path = 'C:\\Users\\20272\\Desktop\\project\\custom_data\\labelmask_folder'

# 指定新文件夹路径
new_folder_path = 'C:\\Users\\20272\\Desktop\\project\\custom_data\\mask'

# 创建新文件夹
os.makedirs(new_folder_path, exist_ok=True)

# 调用函数进行重命名
rename_label_files(root_path, new_folder_path)
