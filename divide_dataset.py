import glob
import json
import random
import shutil
import labelme2coco.labelme2coco as labelme2coco

def main():
    # 读取labelme_json所在的地址
    labelme_json = glob.glob(
        r'C:\Users\20272\Desktop\project\custom_data\annotations_labelme_v2_noignorelabel\*.json')
    json_size = len(labelme_json)

    # 划分训练集和验证集
    random.seed(10)         # 随机种子确保在相同随机种子下生成的随机数是可重复的
    train_dataset = random.sample(labelme_json, int(float(json_size * 0.6)))
    labelme_json_remain = list(set(labelme_json) - set(train_dataset))  # 取补集
    val_dataset = random.sample(labelme_json_remain,
                                int(float(json_size * 0.2)))
    test_dataset = list(set(labelme_json_remain) - set(val_dataset))
    print(f'训练集数量：{len(train_dataset)}')
    print(f'验证集数量：{len(val_dataset)}')
    print(f'测试集数量：{len(test_dataset)}')

    # 创建保存数据的文件夹
    train_dir = 'C:\\Users\\20272\\Desktop\\project\\custom_data\\dataset_no_jgnorelabel\\train'
    test_dir = 'C:\\Users\\20272\\Desktop\\project\\custom_data\\dataset_no_jgnorelabel\\test'
    val_dir = 'C:\\Users\\20272\\Desktop\\project\\custom_data\\dataset_no_jgnorelabel\\val'

    # 复制文件到相应的文件夹中
    for json_file in train_dataset:
        shutil.copy(json_file, train_dir)
    
    for json_file in test_dataset:
        shutil.copy(json_file, test_dir)
    
    for json_file in val_dataset:
        shutil.copy(json_file, val_dir)
    print("ok train")


if __name__ == "__main__":
    main()