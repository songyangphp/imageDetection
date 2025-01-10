### 1.创建环境
    conda create -n yolov8 python=3.9


### 2.激活环境
    conda activate yolo8


### 3.安装ultralytics模块
    pip install ultralytics


### 4.在anaconda中切换到当前目录下
    D:\soft\python\apps\ultralytics


### 5.测试环境
    yolo predict model=yolov8n.pt source="https://ultralytics.com/images/bus.jpg"
#### - 测试成功后会自动生成runs目录


### 6.安装labelme模块-标注工具
    pip install labelme


### 7.打开标注工具
    labelme


### 8.数据标注
#### 8.1 labelme窗口 -> 文件 -> 自动保存
#### 8.2 创建多边形 -> 输入名字 -> 下一幅
#### 8.3 会自动生成.json标注的文件
#### 8.4 将标注文件 转为 yolo格式 安装labelme2yolo模块
    pip install labelme2yolo

#### 8.5 执行main文件中的 move_json_file 方法 将json标注文件移动到 labelme_json_dir
#### 8.6 执行以下命令 将json标注文件 转换为 yolo格式
    labelme2yolo --json_dir D:\soft\python\apps\ultralytics\working\json
#### 8.7 执行成功后 会在json目录下生成YOLODataset目录


### 9.开始训练（yolo8环境下运行此py脚本）
    py D:\soft\python\apps\ultralytics\main.py

### 10.训练完成后会生成runs目录，该目录下会生成权重文件
    D:\soft\python\apps\ultralytics\runs\detect\train7\weights

### 11.验证，会在runs/predict/目录下生成带标记的照片
    yolo task=detect mode=predict model=D:\soft\python\apps\ultralytics\runs\detect\train7\weights\best.pt source=D:\soft\python\apps\ultralytics\working\json\YOLODataset\images\val
    