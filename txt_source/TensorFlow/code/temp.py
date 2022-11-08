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

(x,y) ,(x_val, y_val) = datasets.mnist.load_data()   
x = 2*tf.convert_to_tensor(x,dtype = tf.float32)/255.-1  #转换浮点张量，并缩放到-1~1
y = tf.one_hot(y, depth = 10)   #onehot编码,标签打平，避免分类造成的无关约束
lr = 0.01

w1  =tf.Variable(tf.random.truncated_normal([784,256], stddev =0.1))    #产生限定分布区域为[-0.1,0.1]的正太分布
b1 = tf.Variable(tf.zeros([256]))

w2 = tf.Variable(tf.random.truncated_normal([256,128], stddev=0.1))
b2 = tf.Variable(tf.zeros([128]))

w3 = tf.Variable(tf.random.truncated_normal([128,10], stddev=0.1))
b3 = tf.Variable(tf.zeros([10]))

with tf.GradientTape() as tape:
    x = tf.reshape(x,[-1,28*28]) #-1为自动补全
    h1 = x@w1 + b1
    h1 = tf.nn.relu(h1)     #线性整流，<0时 ->0,     大于0时不变（二极管）
    # print(h1.shape)

    h2 = h1@w2 + b2
    h2 = tf.nn.relu(h2)

    out = h2@w3 + b3
    loss  =tf.square(y - out)
    loss  = tf.reduce_mean(loss)

grads = tape.gradient(loss,[w1,b1,w2,b2,w3,b3])

w1.assign_sub(lr * grads[0])
b1.assign_sub(lr * grads[1])
w2.assign_sub(lr * grads[2])
b2.assign_sub(lr * grads[3])
w3.assign_sub(lr * grads[4])
b3.assign_sub(lr * grads[5])
