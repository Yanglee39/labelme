import os
import shutil

def copy_images_from_list(image_list_file, source_folder, destination_folder):
    # 读取imagelist.txt中的文件名列表
    with open(image_list_file, 'r') as f:
        file_names = f.read().splitlines()

    # 遍历文件名列表，并复制图像文件
    for file_name in file_names:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        if os.path.exists(source_path):
            # 如果文件存在，复制到指定文件夹
            shutil.copy(source_path, destination_path)
        else:
            print(f"File '{file_name}' not found in the source folder.")

# 使用示例
image_list_file = 'C:\\Users\\20272\\Desktop\\project\\custom_data\\dataset_no_jgnorelabel\\vallist.txt'  # imagelist.txt文件的路径
source_folder = 'C:\\Users\\20272\\Desktop\\project\\custom_data\\mask'  # 存放图像的源文件夹路径
destination_folder = 'C:\\Users\\20272\\Desktop\\project\\custom_data\\val'  # 存放复制图像的目标文件夹路径

copy_images_from_list(image_list_file, source_folder, destination_folder)
