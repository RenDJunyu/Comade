.title JUST_FOR_TEST

Vdd Vd 0 DC 5
Vb Vin 0 1
MNM Vin Vd Vout 0 n18 W=5u L=1u
MPM Vin 0 Vout Vd p18 W=15u L=1u
R1 Vout 0 1k
.dc Vb -1 10 0.01
.probe dc ro=par('(v(Vin)-v(Vout))/(i1(MNM)+i1(MPM))')

* .tran 20p 20.8n
* .probe tran v(Vout)

.temp 27
.option post accurate probe
* .option post accurate probe RUNLVL=6 delmax=20p INTERP
.lib 'models\ms018.lib' tt

.end