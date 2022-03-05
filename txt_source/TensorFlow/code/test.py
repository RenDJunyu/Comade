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

gpus=tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        #设置GPU为增长式占用
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu,True)
    except RuntimeError as e:
        print(e)

#***以上请勿删除


if __name__ == '__main__':
    main()