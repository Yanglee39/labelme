import os


def rename_label_files(root_path):
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
       new_file_path = os.path.join(subfolder, new_name)
       
        # 重命名文件
       os.rename(old_file_path, new_file_path)

       print(f'Renamed: {old_file_path} to {new_file_path}')

# def rename_files_in_folder(folder_path, old_filename, new_filename):
#     # 获取文件夹中的所有文件
#     files = os.listdir(folder_path)
#     print(files)

#     for file in files:
#         # 检查文件名是否包含需要更改的旧文件名
#         if old_filename in file:
#             # 构建旧文件的完整路径
#             old_file_path = os.path.join(folder_path, file)

#             # 构建新文件的完整路径
#             new_file_path = os.path.join(folder_path, file.replace(old_filename, new_filename))

#             # 重命名文件
#             os.rename(old_file_path, new_file_path)

#             print(f'Renamed: {old_file_path} to {new_file_path}')

# 指定总文件夹路径
root_path = 'C:\\Users\\CGJWW93\\Desktop\\labelme\\custom_data\\labelme_mask'

# 调用函数进行重命名
rename_label_files(root_path)
