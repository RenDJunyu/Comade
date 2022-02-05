import os
from numpy import number
import timeit
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'#***
import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow import keras #导入TF子库keras
from tensorflow.keras import layers,optimizers,datasets,losses #导入TF子库

# gpus=tf.config.experimental.list_physical_devices('GPU')
# if gpus:
#     try:
#         #设置GPU为增长式占用
#         for gpu in gpus:
#             tf.config.experimental.set_memory_growth(gpu,True)
#     except RuntimeError as e:
#         print(e)

#***以上请勿删除
# 在线下载汽车效能数据集 
dataset_path = keras.utils.get_file("auto-mpg.data", 
"http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data") 
# 利用pandas 读取数据集，字段有效能（公里数每加仑），气缸数，排量，马力，重量
# 加速度，型号年份，产地 
column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight', 
                'Acceleration', 'Model Year', 'Origin'] 
raw_dataset = pd.read_csv(dataset_path, names=column_names, 
                    na_values = "?", comment='\t', 
                    sep=" ", skipinitialspace=True) 
dataset = raw_dataset.copy() 
# 查看部分数据 
# dataset.head()
dataset.isna().sum() # 统计空白数据 
dataset = dataset.dropna() # 删除空白数据项 
dataset.isna().sum() # 再次统计空白数据
# 处理类别型数据，其中origin 列代表了类别1,2,3,分布代表产地：美国、欧洲、日本 
# 先弹出(删除并返回)origin 这一列 
origin = dataset.pop('Origin') 
# 根据origin 列来写入新的3 个列 
dataset['USA'] = (origin == 1)*1.0 
dataset['Europe'] = (origin == 2)*1.0 
dataset['Japan'] = (origin == 3)*1.0 
# dataset.tail() # 查看新表格的后几项
#切分为训练集和测试集 
train_dataset = dataset.sample(frac=0.8,random_state=0) 
test_dataset = dataset.drop(train_dataset.index) 
# 移动MPG 油耗效能这一列为真实标签Y 
train_labels = train_dataset.pop('MPG') 
test_labels = test_dataset.pop('MPG')
# 查看训练集的输入X 的统计数据 
train_stats = train_dataset.describe() 
# train_stats.pop("MPG") # 仅保留输入X 
train_stats = train_stats.transpose() # 转置 
# 标准化数据 
def norm(x): # 减去每个字段的均值，并除以标准差 
    return (x - train_stats['mean']) / train_stats['std'] 
normed_train_data = norm(train_dataset) # 标准化训练集 
normed_test_data = norm(test_dataset) # 标准化测试集
print(normed_train_data.shape,train_labels.shape) 
print(normed_test_data.shape, test_labels.shape) 
train_db = tf.data.Dataset.from_tensor_slices((normed_train_data.values, 
train_labels.values)) # 构建Dataset 对象 
train_db = train_db.shuffle(100).batch(32) # 随机打散，批量化
class Network(keras.Model): 
    # 回归网络模型 
    def __init__(self): 
        super(Network, self).__init__() 
        # 创建3 个全连接层 
        self.fc1 = layers.Dense(64, activation='relu') 
        self.fc2 = layers.Dense(64, activation='relu') 
        self.fc3 = layers.Dense(1) 
 
    def call(self, inputs, training=None, mask=None): 
        # 依次通过3 个全连接层 
        x = self.fc1(inputs) 
        x = self.fc2(x) 
        x = self.fc3(x) 
        return x
model = Network() # 创建网络类实例 
# 通过build 函数完成内部张量的创建，其中4 为任意设置的batch 数量，9 为输入特征长度 
model.build(input_shape=(4, 9))  
model.summary() # 打印网络信息 
optimizer = tf.keras.optimizers.RMSprop(0.0002) # 创建优化器，指定学习率

for epoch in range(200): # 200 个Epoch 
    for step, (x,y) in enumerate(train_db): # 遍历一次训练集 
        # 梯度记录器，训练时需要使用它 
        with tf.GradientTape() as tape: 
            out = model(x) # 通过网络获得输出 
            loss = tf.reduce_mean(losses.MSE(y, out)) # 计算MSE 
            mae_loss = tf.reduce_mean(losses.MAE(y, out)) # 计算MAE 
 
        if step % 10 == 0: # 间隔性地打印训练误差 
            print(epoch, step, float(mae_loss)) 
        # 计算梯度，并更新 
        grads = tape.gradient(loss, model.trainable_variables) 
        optimizer.apply_gradients(zip(grads, model.trainable_variables))
