#可以将文件夹中的多个文件夹里的文件按后缀分别提取出来

import os
import shutil


def split_file(src, dst1, dst2):
    '''
    function: 将文件中不同后缀的文件分开到不同文件夹
    example: 区分jpg和png图像
    src:str(filefolder)
    dst:str(filefolder)
    '''
    # 区分jpg和json
    jpg = []
    json = []
    for f in os.listdir(src):
        if f.endswith('.JPG'):
            jpg.append(f)
        elif f.endswith('.json'):
            json.append(f)

    # 创建目标文件夹
    if not os.path.isdir(dst1):
        os.mkdir(dst1)
    if not os.path.isdir(dst2):
        os.mkdir(dst2)

    # 拷贝文件到目标文件夹
    for j in jpg:
        _jpg = os.path.join(src, j)
        shutil.copy(_jpg, dst1)
    for p in json:
        _png = os.path.join(src, p)
        shutil.copy(_png, dst2)


if __name__ == '__main__':
    base_filename = r'C:\Users\23180\Desktop\convert'
    src = os.path.join(base_filename, 'Cable Type')
    dst1 = os.path.join(base_filename, 'images')
    dst2 = os.path.join(base_filename, 'labels')
    for d in os.listdir(src):
        filename = os.path.join(src, d)  # 带路径的文件名
        split_file(filename, dst1, dst2)