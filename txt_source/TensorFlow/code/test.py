import os
from turtle import color
from black import color_diff
from numpy import number
import timeit
from sklearn.metrics import accuracy_score
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'#***
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras #导入TF子库keras
from tensorflow.keras import layers,optimizers,datasets,losses,Sequential #导入TF子库

# gpus=tf.config.experimental.list_physical_devices('GPU')
# if gpus:
#     try:
#         #设置GPU为增长式占用
#         for gpu in gpus:
#             tf.config.experimental.set_memory_growth(gpu,True)
#     except RuntimeError as e:
#         print(e)

#***以上请勿删除

lrate=0.05
epoch=200
N_SAMPLES = 2000 # 采样点数  
TEST_SIZE = 0.3 # 测试数量比率 
# 利用工具函数直接生成数据集 
X, y = make_moons(n_samples = N_SAMPLES, noise=0.2, random_state=100)  
# 将2000 个点按着7:3 分割为训练集和测试集 
X_train, X_test, y_train, y_test = train_test_split(X, y, 
test_size=TEST_SIZE, random_state=42) 
print(X.shape, y.shape)
# 绘制数据集的分布，X 为2D 坐标，y 为数据点的标签 

class Layer: 
    # 全连接网络层 
    def __init__(self, n_input, n_neurons, activation=None, weights=None, 
bias=None): 
        """ 
        :param int n_input: 输入节点数 
        :param int n_neurons: 输出节点数 
        :param str activation: 激活函数类型 
        :param weights: 权值张量，默认类内部生成 
        :param bias: 偏置，默认类内部生成 
        """  
        # 通过正态分布初始化网络权值，初始化非常重要，不合适的初始化将导致网络不收敛 
        self.weights = weights if weights is not None else np.random.randn(n_input, n_neurons) * np.sqrt(1 / n_neurons) 
        self.bias = bias if bias is not None else np.random.rand(n_neurons) * 0.1 
        self.activation = activation # 激活函数类型，如’sigmoid’ 
        self.last_activation = None # 激活函数的输出值o 
        self.error = None # 用于计算当前层的delta 变量的中间变量 
        self.delta = None  # 记录当前层的delta 变量，用于计算梯度 
    def activate(self, x): 
        # 前向传播函数 
        r = np.dot(x, self.weights) + self.bias  # X@W+b 
        # 通过激活函数，得到全连接层的输出o 
        self.last_activation = self._apply_activation(r) 
        return self.last_activation
    def _apply_activation(self, r): 
        # 计算激活函数的输出 
        if self.activation is None: 
            return r # 无激活函数，直接返回 
        # ReLU 激活函数 
        elif self.activation == 'relu': 
            return np.maximum(r, 0) 
        # tanh 激活函数 
        elif self.activation == 'tanh': 
            return np.tanh(r) 
        # sigmoid 激活函数 
        elif self.activation == 'sigmoid': 
            return 1 / (1 + np.exp(-r)) 
        return r 
    def apply_activation_derivative(self, r): 
        # 计算激活函数的导数 
        # 无激活函数，导数为1 
        if self.activation is None: 
            return np.ones_like(r) 
        # ReLU 函数的导数实现 
        elif self.activation == 'relu': 
            grad = np.array(r, copy=True) 
            grad[r > 0] = 1. 
            grad[r <= 0] = 0. 
            return grad 
        # tanh 函数的导数实现 
        elif self.activation == 'tanh': 
            return 1 - r ** 2 
        # Sigmoid 函数的导数实现 
        elif self.activation == 'sigmoid': 
            return r * (1 - r) 
        return r
class NeuralNetwork: 
    # 神经网络模型大类 
    def __init__(self): 
        self._layers = []  # 网络层对象列表 
 
    def add_layer(self, layer): 
        # 追加网络层 
        self._layers.append(layer)
    def feed_forward(self, X): 
        # 前向传播 
        for layer in self._layers: 
            # 依次通过各个网络层 
            X = layer.activate(X) 
        return X
    def backpropagation(self, X, y, learning_rate): 
        # 反向传播算法实现 
        # 前向计算，得到输出值 
        output = self.feed_forward(X) 
        for i in reversed(range(len(self._layers))):  # 反向循环 
            layer = self._layers[i]  # 得到当前层对象 
            # 如果是输出层 
            if layer == self._layers[-1]:  # 对于输出层 
                layer.error = y - output  # 计算2 分类任务的均方差的导数 
                # 关键步骤：计算最后一层的delta，参考输出层的梯度公式 
                layer.delta = layer.error * layer.apply_activation_derivative(output) 
            else:  # 如果是隐藏层 
                next_layer = self._layers[i + 1]  # 得到下一层对象 
                layer.error = np.dot(next_layer.weights, next_layer.delta) 
                # 关键步骤：计算隐藏层的delta，参考隐藏层的梯度公式 
                layer.delta = layer.error * layer.apply_activation_derivative(layer.last_activation) 
        for i in range(len(self._layers)): 
            layer = self._layers[i] 
            # o_i 为上一网络层的输出  
            o_i = np.atleast_2d(X if i == 0 else self._layers[i - 1].last_activation) 
            # 梯度下降算法，delta 是公式中的负数，故这里用加号 
            layer.weights += layer.delta * o_i.T * learning_rate
    def train(self, X_train, X_test, y_train, y_test, learning_rate, max_epochs): 
        # 网络训练函数 
        # one-hot 编码 
        y_onehot = np.zeros((y_train.shape[0], 2)) 
        y_onehot[np.arange(y_train.shape[0]), y_train] = 1
        mses = [] 
        for i in range(max_epochs):  # 训练1000 个epoch 
            for j in range(len(X_train)):  # 一次训练一个样本 
                self.backpropagation(X_train[j], y_onehot[j], learning_rate) 
            if i % 10 == 0: 
                # 打印出MSE Loss 
                mse = np.mean(np.square(y_onehot - self.feed_forward(X_train))) 
                mses.append(mse) 
                print('Epoch: #%s, MSE: %f' % (i, float(mse))) 

                # 统计并打印准确率
                accuracy=0
                y_test_flat=y_test.flatten()
                for order,n in enumerate(self.feed_forward(X_test)):
                    accuracy+=(n[0]<0.5)==y_test_flat[order]
                accuracy/=len(y_test_flat)
                print('Accuracy: %.2f%%' % (accuracy*100)) 
        return mses 

nn = NeuralNetwork() # 实例化网络类 
nn.add_layer(Layer(2, 25, 'sigmoid'))  # 隐藏层1, 2=>25 
nn.add_layer(Layer(25, 50, 'sigmoid')) # 隐藏层2, 25=>50 
nn.add_layer(Layer(50, 25, 'sigmoid')) # 隐藏层3, 50=>25 
nn.add_layer(Layer(25, 2, 'sigmoid'))  # 输出层, 25=>2
nn.train(X_train, X_test, y_train, y_test,lrate,epoch)
