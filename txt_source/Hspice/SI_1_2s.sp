*
.TITLE  Signal integrity Training deck
.inc 'rise.sp'


* Some parameters that are used and can be changed
* UI/supply nominal level
.param UI=3.5ns Vcc=1.5 Vtt=1.15 Vdata=1

* TX/RX termination
.param TX_rterm=50 TX_cterm=1p
.param RX_rterm=45 RX_cterm=0.5p

* Voh/Vol levels
.param Voh=1.2 Vol=0.25

* Rise/fall time
.param tr=300ps 
.param tf=300ps

* Characteristic impedance
.param Z0=66.1471

* Options to be used
.option probe=1 post=1
.option list

* Set chip voltage and termination voltage
Vcc Vcc 0 Vcc                                           
Vtt Vtt 0 Vtt     

* Dummy connection source                                       
Vconn Vcc Vcc_buff 0

* Input for aggressor and victim
* Modify the data rate for different scenarios and understand the waveform
Xdata0 data_a DATAS datarate=UI 
* Xdata1 data_v DATAS datarate='5*UI'
VV data_v 0 dc 0

Vnw VccNW 0 dc 1

* Aggressor and victim buffers
* XBUFF0 data_a pkg_a Vcc_buff 0 SIMPLE_BUF
* XBUFF1 data_v pkg_v Vcc_buff 0 SIMPLE_BUF 

XBUFF0 pkg_a data_a 0 Vcc_buff VccNW BUFLERMX16
XBUFF1 pkg_v data_v 0 Vcc_buff VccNW BUFLERMX16 

* Package trace
* XPKG_TX pkg_a pkg_v pkg_ao pkg_vo 0 SIMPLE_PKG


T1 pkg_a 0 pkg_rao 0 Z0=50 TD=1n L=0.1
T2 pkg_v 0 pkg_rvo 0 Z0=50 TD=1n L=0.1

* Board trace
* Xboard pkg_v pkg_a pkg_rvo pkg_rao 0 SIMPLE_BRD

* Receivers for aggressor and victim
XRCV0 pkg_rvo 0 SIMPLE_RCV
XRCV1 pkg_rao 0 SIMPLE_RCV

* Transient simulation statements here
.tran 10p 100n                    

* Add your probe statements for the nodes of interest                     
***************************************************
* .probe v(pkg_*) v(data_*)
* .probe i(Vconn)
***************************************************


* Understand this simple transmission line model
* .SUBCKT MCHPKG pin pad
* TPKG1 pad 0 pin 0 Z0=50 TD='200PS*(1.01)'
* Cpin pin 0 .01pF
* .ENDS

.SUBCKT DATAS bit1 datarate=-1
V1 bit1 0 PULSE 0v 'Vdata' '10*datarate' tr tr '5*datarate' '20*datarate'
.ENDS

* Understand this simple buffer model 
* Understand the usage of voltage controlled voltage source
* .SUBCKT SIMPLE_BUF in out Vpwr Vgnd
* Edrive out1 Vgnd VOL='(V(Vpwr)-Vcc+Voh-Vol)*V(in)+Vol'
* Rout out1 out 'TX_rterm'
* Cout out1 Vgnd 'TX_cterm'
* Rin in Vgnd 1G
* .probe v(in) v(out*)
* .ENDS

* .SUBCKT SIMPLE_PKG in_a in_v out_a out_v Vgnd
* L1 in_a	out_a 5n
* L2 in_v	out_v 5n
* K1 L1 L2 0.5
* .ENDS


* Understand W Element and its usage
.SUBCKT SIMPLE_BRD in1 in2 out1	out2 Vgnd
* How to instantiate a W element with N=2 (in1/in2 and out1/out2) for RLGC model below 
* length is 0.1 inch and Vgnd is reference
***************************************************************
Wline1 in1 in2 Vgnd out1 out2 Vgnd
+ RLGCMODEL='simple_model.rlgc' N=2 L=0.1
***************************************************************

* .MODEL simple_model.rlgc W MODELTYPE=RLGC, N=2
* + Lo = 4.460644e-007
* +      9.544025e-008 4.460644e-007
* + Co = 1.019475e-010
* +      -2.181277e-011 1.019475e-010
* + Ro = 0.000000e+000
* +      0.000000e+000 0.000000e+000
* + Go = 0.000000e+000
* +      0.000000e+000 0.000000e+000
* + Rs = 0.000000e+000
* +      0.000000e+000 0.000000e+000
* + Gd = 1.217055e-011
* +      -2.604020e-012 1.217055e-011
* + Lo = 4.460644e-007
* +      9.544025e-008 4.460644e-007
* + Co = 1.019475e-010
* +      -2.181277e-011 1.019475e-010
* + Ro = 0.000000e+000
* +      0.000000e+000 0.000000e+000
* + Go = 0.000000e+000
* +      0.000000e+000 0.000000e+000
* + Rs = 0.000000e+000
* +      0.000000e+000 0.000000e+000 
* + Gd = 0.000000e+000
* +      0.000000e+000 0.000000e+000

.ENDS

.SUBCKT	SIMPLE_RCV in Vgnd
Rin in Vgnd 'Z0'
* Cin in Vgnd 'RX_cterm'
.ENDS

* .print v(pkg_rao)

.print v(pkg_a) v(pkg_v)
.probe v(pkg_a) v(pkg_v)

.END

