import os

# 定义要遍历的文件夹路径
folder_path = 'C:\\Users\\CGJWW93\\Desktop\\labelme\\custom_data\\labelme_mask_image_copy'

# 遍历文件夹中的所有文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # 检查文件的后缀是否为.png
        if file.endswith('.png'):
            # 构建新的文件名，将后缀改为.jpg
            new_file_name = os.path.splitext(file)[0] + '.jpg'
            
            # 构建完整的文件路径
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(root, new_file_name)
            
            # 重命名文件
            os.rename(old_file_path, new_file_path)
            
            print(f'Renamed: {file} -> {new_file_name}')
