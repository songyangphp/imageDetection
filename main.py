#coding:utf-8
from ultralytics import YOLO

# 加载训练模型
model = YOLO('./model/yolov8n.pt')

# 开始训练

if __name__ == '__main__':
    result = model.train(data=r'D:\soft\python\apps\ultralytics\working\json\YOLODataset\dataset.yaml', epochs=300, batch=4)