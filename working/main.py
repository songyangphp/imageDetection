#coding:utf-8

import os
import requests
import shutil


def download_img():
    """
    oss地址下载图片
    :return:
    """
    img_url_list = []
    with open(r'./imgurl.txt', 'r') as imgurl_file:
        for i in imgurl_file:
            paper = i.split(',')
            if len(paper) > 0:
                img_url_list.append(paper[0])

    for img_url in img_url_list:
        if 'https' not in img_url:
            continue

        response = requests.get(img_url)

        if response.status_code == 200:
            file_name = img_url.split('_')[-1]
            file_path = r'./imgs/' + file_name

            with open(file_path, 'wb') as fp:
                fp.write(response.content)
                print('-' + file_path + '保存成功')


def move_json_file():
    """
    移动.json标注文件到labelme_json_dir目录下
    :return:
    """
    path = r'./imgs'  # 图片路径 默认保存到此路径下
    json_path = r'./json'  # 存放json标注文件的目录
    for file_name in os.listdir(path):
        if file_name.split('.')[-1] == 'json':  # 识别目录下的json文件
            shutil.move(r'./imgs/' + file_name, json_path)  # 移动
            print('-' + file_name + '移动成功')


def png_to_jpg():
    path = r'./imgs'


if __name__ == '__main__':
    move_json_file()
    # download_img()
