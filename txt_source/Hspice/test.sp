.title JUST_FOR_TEST

Vdd Vd 0 DC 5
Vc clk 0 PULSE (0 5 0NS 0.1NS 0.1NS 20NS 40NS)
Vcx clkx 0 PULSE (0 5 20NS 0.1NS 0.1NS 20NS 40NS)
Vi Vin 0 PULSE (0 5 0NS 0.1NS 0.1NS 10NS 20NS)
MNM1 Vin clk Vx 0 n18 W=5u L=1u
MPM1 Vin clkx Vx Vd p18 W=10u L=1u
MNM2 Vout Vx 0 0 n18 W=5u L=1u
MPM2 Vout Vx Vd Vd p18 W=10u L=1u

* .dc Vb -1 10 0.01
* .probe dc ro=par('(v(Vin)-v(Vout))/(i1(MNM)+i1(MPM))')

.tran 20p 200n
.probe tran v(Vin) v(Vout) v(clk) v(Vx)

.temp 27
.option post accurate probe
* .option post accurate probe RUNLVL=6 delmax=20p INTERP
.lib 'models\ms018.lib' tt

.end