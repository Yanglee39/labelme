import json
from json import dumps
import base64
import os

def image_to_base64(image_path):
    # 读取二进制图片,获得图片的原始字节码
    with open(image_path, 'rb') as jpg_file:
        byte_content = jpg_file.read()

    # 把原始的字节码编码成为base64字节码
    base64_bytes = base64.b64encode(byte_content)

    # 把base64字节码解码成为utf-8格式的字符串
    base64_string = base64_bytes.decode('utf-8')

    return base64_string


# 图片所在文件夹
root_dir = 'C:\\Users\\20272\\Desktop\\project\\custom_data\\images'
# 标注所在文件夹
anntotatinos_dir = 'C:\\Users\\20272\\Desktop\\project\\custom_data\\annotations_custom'
# labelme.json保存地址
save_directory = "C:\\Users\\20272\\Desktop\\project\\custom_data\\annotations_labelme_v2_noignorelabel"

# imagelist所在文件夹
imagelist_root = "C:\\Users\\20272\\Desktop\\project\\custom_data"
imagelist_txt = os.path.join(imagelist_root, "imagelist.txt")       # 地址拼接

# annotationslist所在文件夹
annotationlist_txt = os.path.join(imagelist_root, "annotationlist.txt")       # 地址拼接

with open(imagelist_txt, 'r') as file:
    # 读取文本文件的内容,得到的是一个一个字符串‘’，里面包含了整个文件的内容
    images = file.read()
    # 调用字符串分割函数split()方法一个包含多个部分的列表
    images = images.split('\n')

with open(annotationlist_txt, 'r') as file:
    # 读取文本文件的内容,得到的是一个一个字符串‘’，里面包含了整个文件的内容
    annotations = file.read()
    # 调用字符串分割函数split()方法一个包含多个部分的列表
    annotations = annotations.split('\n')    

# 利用字符串拼接的方式将图像文件地址和图像文件名组合在一起
for image in images:
    
    image_filename = os.path.join(root_dir, image)
    
    annotation_headname = image.split('.')[0]
    annotation_tailname = '.json'

    annotation_totalname = annotation_headname + annotation_tailname         
    annotation_filename = os.path.join(anntotatinos_dir, annotation_totalname)# 得到完整的annotation的文件地址
    
    # 创建一个新的labelme的json格式
    labelme_data = {
        "version": "3.16.2",         # 本地3.16.2    4.5.7
        "flags": {},
        "shapes": [],
        "lineColor": [0, 255, 0, 128],
        "fillColor": [255, 0, 0, 128],
        "imagePath": "",
        "imageData": None
    }

    # 填充labelme_data中的imagepath字段
    labelme_data["imagePath"] = image_filename

    # 填充labelme_data中的imageData字段
    labelme_data["imageData"] = image_to_base64(image_filename)

    # 读取annotation文件填充其他字段
    with open(annotation_filename, 'r') as f:
        annotation_data = json.load(f)
    
    # 访问每个json文件中的bundles字段
    bundles = annotation_data["bundles"]

    # 访问bundles中的group字段
    groups = bundles[0]["groups"]

    # 遍历groups中的每个group，每个group都是一个改图片中的标注信息
    for group in groups:
        shape = {
            "label": None,
            "points": [],
            "shape_type": "polygon",
        }
        if group["type"] != 'ignore':
            # 获取group中的type字段,获得标注标签的名称，填充shape["label"]字段
            shape["label"] = group["type"]

            # 获取每个group中的objects中的points键中的值，获得标注标签点的坐标，填充shape["points"]字段
            objects = group["objects"]
        
            point_info = {
                "x": None,
                "y": None
            }
    
            for p in objects[0]["points"]:
                point_info["x"] = p["x"]
                point_info["y"] = p["y"]

                shape["points"].append([point_info["x"], point_info["y"]])

            labelme_data["shapes"].append(shape)

    # 保存创建好的json文件
    output_json_file = os.path.join(save_directory, annotation_totalname) 
    with open(output_json_file, 'w') as f:
        json.dump(labelme_data, f)
    
    print(f"转换完成并保存为{output_json_file}")
