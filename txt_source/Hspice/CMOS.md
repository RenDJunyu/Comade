# 拉扎维学习笔记

## 连接方式

    共源级
        Vdd Vdd 0 DC 1.8
        * CL cpl cpr 1p 
        RD1 Vdd Vout1 1k
        RD2 Vdd Vout2 1k
        MPM1 Vout1 Vin 0 Vout1 p18 W=5u L=180n m=1
        MNM1 Vout2 Vin 0 0 n18 W=5u L=180n m=1
        .dc Vin 0 1.8 0.01
        .probe v(Vout1) v(Vout2)
    二极管连接的负载的共源级
        Vdd Vdd 0 DC 1.8
        Vgs Vin 0 DC 0.75V
        * CL cpl cpr 1p 
        MPM1 Vdd Vdd Vout Vdd p18 W=5u L=180n m=1
        MNM1 Vout Vin 0 0 n18 W=5u L=180n m=1
        .dc Vgs 0 1.8 0.01
        .probe v(Vout)
    电流源控制
        Vdd Vdd 0 DC 1.8
        Ii Iout 0 100m
        * CL cpl cpr 1p 
        MNM1 Vdd Vdd Iout 0 n18 W=5u L=180n m=1
        .dc Ii 0 0.1 1m
        .probe v(Iout)
    采用电流源负载的共源极
        Vdd Vdd 0 DC 1.8
        Vgs Vin 0 DC 0.75V
        VBG Vb 0 DC 0.75V
        * CL cpl cpr 1p 
        MPM1 Vdd Vb Vout Vdd p18 W=5u L=180n m=1
        MNM1 Vout Vin 0 0 n18 W=5u L=180n m=1
        .dc Vgs 0 1.8 0.1 VBG 0 1.8 0.1
        .probe v(Vout)
    带源极负反馈的共源极
        Vdd Vdd 0 DC 1.8
        Vgs Vin 0 DC 0.75V
        RD Vdd Vout 1k
        RS Vrs 0 1k
        MPM1 Vout Vin Vrs Vdd p18 W=5u L=180n m=1
        .dc Vgs 0 1.8 0.1
        .probe v(Vout)
    源跟随器
        Vdd Vdd 0 DC 1.8
        Vgs Vin 0 DC 0.75V
        RS Vout 0 1k
        MNM1 Vdd Vin Vout 0 n18 W=5u L=180n m=1
        .dc Vgs 0 1.8 0.1
        .probe v(Vout)
    共栅极
        Vdd Vdd 0 DC 1.8
        Vs Vin 0 DC 0.75V
        Vb Vbb 0 DC 0.75V
        RD Vout Vdd 1k
        MNM1 Vin Vbb Vout Vin n18 W=5u L=180n m=1
        .dc Vs 0 1.8 0.1
        .probe v(Vout)
    共源共栅级
        