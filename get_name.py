import os

def list_files_to_txt(folder_path, output_file):
    # 获取文件夹中的所有文件名
    files = os.listdir(folder_path)
    
    # 打开输出文件
    with open(output_file, 'w') as f:
        # 遍历文件名列表
        for file_name in files:
            # 将文件名写入txt文件中
            f.write(file_name + '\n')

# 使用示例
folder_path = r'C:\Users\20272\Desktop\project\custom_data\dataset_no_jgnorelabel\val'  # 替换成实际的文件夹路径
output_file = r'C:\Users\20272\Desktop\project\custom_data\dataset_no_jgnorelabel\vallist.txt'    # 替换成实际的输出文件路径

list_files_to_txt(folder_path, output_file)
