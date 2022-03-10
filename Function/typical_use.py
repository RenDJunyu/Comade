#-*- coding:utf=8 -*- 这样写除了说明编码,也是为了更加美观
#the fitst workspace to test python
'''
import keyword,datetime,sys,string,os,random,re,time

import numpy
from numpy.linalg import *
from math import *
from scipy.linalg import *
from sympy import *

import wx,turtle #GUI
import pymysql,sqlite3 #database
import pygame #pygame
import __future__,antigravity,this #彩蛋
import urllib.parse as par,urllib.request as req #发出请求...
import urllib3
from bs4 import BeautifulSoup #解析HTML
import requests
import json
from multiprocessing import Process,Queue
import threading
import numpy
from numpy.linalg import *
from flask import Flask,url_for,request,render_template
'''

area=2
if area==1:

    import bluetooth
    target_name = "HC-04"
    target_address = "00:20:08:18:01:B7"
    try:
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
    except:
        print("please open your bluetooth")
    print("Found {} devices.".format(len(nearby_devices)))

    for addr, name in nearby_devices:
        print("  {} - {}".format(addr, name))
        if name==target_name:
            target_address=addr
            print("find device")

    # server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    # port = 1
    # server_sock.bind(("",port))
    # server_sock.listen(1)
    # client_sock,address = server_sock.accept()
    # print ("Accepted connection from ",address)
    # data = client_sock.recv(1024)
    # print ("received [%s]" % data)
    # client_sock.close()
    # server_sock.close()

    port = 1
    sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM )
    sock.connect((target_address, port))
    sock.send("hello!!")
    sock.close()

elif area==2:
    """
        物理计算workspacea
    """
    PI=3.1415926535897932384626
    m_e=9.1e-31
    m_H1=1.6726231e-27
    c=3e8
    k_B=1.38e-23
    p_n=101325
    R_Nak=8.31
    qe=1.602176634e-19
    eV=1.6021766208e-19
    epsilon=8.85e-12
    h=6.63e-34
    hba=1.055e-34

    import math
    print(((h*c)/(850e-9)/eV-1.424)/1.247)
 
elif area==3:
    from time import sleep
    from pynput.mouse import Button,Controller
    import numpy as np
    import cv2 as cv

    from PyQt5.QtWidgets import QApplication
    from win32gui import FindWindow,GetWindowRect
    import sys

    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    mouse=Controller()
    ref_img=["img/sun.png","img/coin_silver.png","img/coin_gold.png"]

    while 1:
        try:
            # sleep(0.5)
            hwnd = FindWindow(None, 'Plants vs. Zombies 1.2.0.1073 RELEASE')
            x1,y1,x2,y2=GetWindowRect(hwnd)
            width,length=x2-x1,y2-y1
            img = screen.grabWindow(hwnd).toImage()
            img.save("img/tosearchin.png")

            MIN_MATCH_COUNT=3 #设置最低匹配数量为10
            for i in range(1,3):
                img1=cv.imread(ref_img[i],0) #读取第一个图像（小图像）
                img2=cv.imread("img/tosearchin.png",0) #读取第二个图像（大图像）
                sift=cv.SIFT_create() #创建sift检测器
                kp1,des1=sift.detectAndCompute(img1,None) 
                kp2,des2=sift.detectAndCompute(img2,None)
                #创建设置FLAAN匹配
                FLANN_INDEX_KDTREE=0
                index_params=dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
                search_params=dict(checks=50)
                flann=cv.FlannBasedMatcher(index_params,search_params)
                mathces=flann.knnMatch(des1,des2,k=2)
                good=[]
                #过滤不合格的匹配结果，大于0.7的都舍弃
                for m,n in mathces:
                    if m.distance<0.8*n.distance:
                        good.append(m)
                #如果匹配结果大于10，则获取关键点的坐标，用于计算变换矩阵
                if len(good)>MIN_MATCH_COUNT:
                    src_pts=np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
                    dst_pts =np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

                #计算变换矩阵和掩膜
                    M,mask=cv.findHomography(src_pts,dst_pts,cv.RANSAC,10.0)
                    matchesMask=mask.ravel().tolist()
                #根据变换矩阵进行计算，找到小图像在大图像中的位置
                    h,w=img1.shape
                    pts=np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2)
                    dst=cv.perspectiveTransform(pts,M)
                    for i in dst:
                        i=i[0]
                        if(i[0]>0 and i[0]<width and i[1]>0 and i[1]<length):
                            mouse.position=(x1+i[0],y1+i[1])
                            mouse.click(Button.left,1)
                            print("click")
                else:
                    print("find nothing!")
                    matchesMask=None
        except:
            continue

elif area==4:
    # import socket
    # # host="10.181.226.181" 
    # host="192.168.137.1"
    # # host="127.0.0.1"
    # port=8088
    # web=socket.socket()
    # web.bind((host,port))
    # web.listen(5)
    # print("recycle")
    # while True:
    #     conn,addr=web.accept()
    #     data=conn.recv(8)
    #     print(data)
    #     # conn.sendall(b'HTTP/1.1 200 OK\r\n\r\nHello world')
    #     conn.close()
    # import socket
    # import time
    # # host="10.181.226.181"
    # host="192.168.137.2"
    # selfhost="192.168.137.1"
    # port=333
    # selfport=8088
    # s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # s.bind((selfhost,selfport))
    # print("recycle")
    # while True:
    #     data=s.recvfrom(208)
    #     print(data)
    #     time.sleep(0.1)
    import socket
    import time
    host="10.181.223.64" 
    # host="192.168.128.2"
    # host="127.0.0.1"
    port=8088
    web=socket.socket()
    web.connect((host,port))
    print("recycle")
    while True:
        # conn,addr=web.accept()
        # data=conn.recv(8)
        web.send(b"123")
        # print(data)
        # conn.sendall(b'HTTP/1.1 200 OK\r\n\r\nHello world')
        # conn.close()
        time.sleep(0.5)
elif area==5:
    from pynput.mouse import Button,Controller
    mouse=Controller()
    mouse.click(Button.left,1)