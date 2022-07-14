.title JUST_FOR_TEST

Vdd Vd 0 DC 5
VinA Ain 0 PULSE (0 5 0NS 0.1NS 0.1NS 50NS 100NS)
VinB Bin 0 PULSE (0 5 0NS 0.1NS 0.1NS 75NS 150NS)
Vb Vb1 0 DC 0
* MPM1 Vd Ain Vout Vd p18 W=3u L=180n
* MPM2 Vd Bin Vout Vd p18 W=3u L=180n
MPM1 Vd Vb1 Vout Vd p18 W=1000n L=180n
MNM1 0  Ain Vout1 0 n18 W=1u L=180n
MNM2 Vout1 Bin Vout 0 n18 W=1u L=180n
C1 Vout 0 1p
* .dc Vb -1 10 0.01

.tran 20p 500n
.probe tran v(Ain) v(Bin) v(Vout) POWER

.temp 27
.option post accurate probe
* .option post accurate probe RUNLVL=6 delmax=20p INTERP
.lib 'models\ms018.lib' tt

.end