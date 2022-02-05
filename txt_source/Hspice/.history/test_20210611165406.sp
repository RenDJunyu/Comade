.title JUST_FOR_TEST

Vin in 0 DC 5
CL cpl cpr 1p 
RL cpr 0 1k
MNM1 in in cpl cpl n18 W=1u L=200n
MNM2 cpl in 0 0 n18 W=1u L=200n

.tran 1n 10m
.probe TRAN V(cpr)

.temp 27
.option post accurate probe
.lib '.\models\ms018.lib' tt

.end

