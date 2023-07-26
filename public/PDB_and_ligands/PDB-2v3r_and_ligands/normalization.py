import os
import json

def modify_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    # 修改键名和键值
    data["Vina"] = data.pop("Vina score")
    data["num_atoms"] = data.pop("Atoms Num")
    data["num_bonds"] = data.pop("Bonds Num")
    data["num_rings"] = data.pop("Rings Num")
    data["num_benzene_rings"] = data.pop("Benzene Rings Num")

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def batch_modify_json_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            modify_json_file(file_path)

# 将下面这行替换为你存放 JSON 文件的文件夹路径
folder_path = './'

batch_modify_json_files(folder_path)
