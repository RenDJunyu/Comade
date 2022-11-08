# 仿真方位角定位

# numpy也有三角函数，故不调用math
from turtle import color
from unittest import result
import numpy as np
import matplotlib.pyplot as plt
import random as rd

# Fixing random state for reproducibility
np.random.seed(19680801)

# 球坐标和垂直坐标互换
def ball2ver2ball(coor,mode):
    if mode == 0:#mode0 ball2ver
        x = coor[0]*np.sin(coor[1])*np.cos(coor[2])
        y = coor[0]*np.sin(coor[1])*np.sin(coor[2])
        z = coor[0]*np.cos(coor[1])
        return x,y,z
    elif mode == 1:#mode1 ver2ball
        r = (coor[0]**2+coor[1]**2+coor[2]**2)**0.5
        theta = np.arccos(coor[2]/r)
        phy = np.arccos(coor[0]/(r*np.sin(theta)))
        return r,theta,phy


# 可能判断方位角需要自己实现，另谈

# 先生成采样到的数据，包括信号强度和信号的方位角
# 先不用类的方法描述
# 在空间中随机生成一个连续移动，速度连续变化且合理的运动目标，并持续发出射频信号
def sim_data_gen():
    # 无人机生成的范围为，距离≥5.5km（无人机典型发射信号功率20dBm）,侦测范围为0~360°、俯仰角-5°~55°
    radius = 6e3
    pitch = (-5,55)
    typical_p = 20
    # 为方便计算，先用球坐标生成无人机，用垂直坐标进行移动，然后再转换
    # 频率先不予考虑
    init_r = rd.randint(0,radius)
    init_theta = rd.randint(pitch[0],pitch[1])/180*np.pi
    init_phy = rd.randrange(0,360)/180*np.pi
    #转换得到垂直坐标
    x,y,z = ball2ver2ball((init_r,init_theta,init_phy),0)
    # 初始速度上，文档给出最大20m/s的飞行速度，大疆精灵4的最大上升/下降速度为6/4m/s
    max_up_v,max_down_v = 6,-4
    max_v = 20
    v_z = rd.randint(-max_down_v*10,max_up_v*10)/10
    temp = int((max_v**2-v_z**2)**0.5*10)
    v_x = rd.randint(-temp,temp)/10
    temp = int((max_v**2-v_z**2-v_x**2)**0.5*10)
    v_y = rd.randint(-temp,temp)/10
    # 先不考虑变速
    gearshift=False
    # 采样速度，系统给出的1k次/s，即数据间隔时间为1ms
    # 采样时间，在无人机不做变速的情况下，从初始位置，飞出范围外即停止采样
    # sample_fre = 1e3
    sample_fre = 1
    # 信号频率 2.4GHz附近
    typical_fre = 2.4e3 #单位Mhz
    interval_time = 1/sample_fre
    res = []
    if gearshift == False:
        while 1:
            r,theta,phy = ball2ver2ball((x,y,z),1)
            # 飞出范围不再耿总
            if r>radius or theta<pitch[0]/180*np.pi or theta>pitch[1]/180*np.pi:
                return res
            # 电磁波自由空间衰减公式,MHz,Km
            Ls = 32.45+ 20*np.log10(r/1e3) + 20*np.log10(typical_fre)
            Ls += np.random.randn()
            # res.append([r,theta,phy,typical_p-Ls])
            res.append([r,theta,phy,typical_p-Ls])
            # 采样间隔，UAV发生移动
            x += v_x*interval_time
            y += v_y*interval_time
            z += v_z*interval_time
            
# 原始射频信号，加入白噪声，考虑信道数据
# 套入RSSI
    
# 根据信号强度和方位角进行判断

# 3D绘图
def figure_plot(data):

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    xyz=np.array([ball2ver2ball((i[0],i[1],i[2]),0) for i in data])
    print(xyz.shape)
    ax.scatter(xyz[:,0],xyz[:,1],xyz[:,2], marker='^')

    # ax.set_xlabel('X Label')
    # ax.set_ylabel('Y Label')
    ax.set_xlim(-6000,6000)
    ax.set_ylim(-6000,6000)
    ax.set_zlim(-6000,6000)

    t = np.linspace(0, np.pi * 2, 100)
    # s = np.linspace(-5/180*np.pi, 90/180*np.pi, 100)
    s = np.linspace(55/180*np.pi, 95/180*np.pi, 100)

    t, s = np.meshgrid(t, s)
    x = 6e3*np.cos(t) * np.sin(s)
    y = 6e3*np.sin(t) * np.sin(s)
    z = 6e3*np.cos(s)
    # z[>0]=0  # 截取球体的下半部分
    ax.plot_wireframe(x, y, z,  rstride=5, cstride=5 , color="g")
    
    plt.show()

if __name__ == "__main__":
    print("check")
    res = sim_data_gen()
    figure_plot(res)
    print(res[0:10])


