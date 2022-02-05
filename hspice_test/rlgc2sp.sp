#Current Calculation Test

.include "rcmodel.sp.inc"
Xdie vssSG64 vssSG63 vssSG62 vssSG61 vssSG60 
 + vssSG53 vssSG52 vssSG51 vssSG50 vssSG49 
 + vssSG48 vssSG41 vssSG40 vssSG39 vssSG38 
 + vssSG37 vssSG36 vssSG29 vssSG28 vssSG27 
 + vssSG26 vssSG25 vssSG24 vssSG17 vssSG16 
 + vssSG15 vssSG14 vssSG13 vssSG12 vssSG5 
 + vssSG4 vssSG3 vssSG2 vssSG1 vssSG0 
 + vssBG34 vssBG33 vssBG32 vssBG31 vssBG30 
 + vssBG29 vssBG28 vssBG27 vssBG26 vssBG25 
 + vssBG24 vssBG23 vssBG22 vssBG21 vssBG20 
 + vssBG19 vssBG18 vssBG17 vssBG16 vssBG15 
 + vssBG14 vssBG13 vssBG12 vssBG11 vssBG10 
 + vssBG9 vssBG8 vssBG7 vssBG6 vssBG5 
 + vssBG4 vssBG3 vssBG2 vssBG1 vssBG0 
 + vddSG65 vddSG64 vddSG63 vddSG62 vddSG61 
 + vddSG60 vddSG53 vddSG52 vddSG51 vddSG50 
 + vddSG49 vddSG48 vddSG41 vddSG40 vddSG39 
 + vddSG38 vddSG37 vddSG36 vddSG29 vddSG28 
 + vddSG27 vddSG26 vddSG25 vddSG24 vddSG17 
 + vddSG16 vddSG15 vddSG14 vddSG13 vddSG12 
 + vddSG5 vddSG4 vddSG3 vddSG2 vddSG1 
 + vddSG0 vddBG34 vddBG33 vddBG32 vddBG31 
 + vddBG30 vddBG29 vddBG28 vddBG27 vddBG26 
 + vddBG25 vddBG24 vddBG23 vddBG22 vddBG21 
 + vddBG20 vddBG19 vddBG18 vddBG17 vddBG16 
 + vddBG15 vddBG14 vddBG13 vddBG12 vddBG11 
 + vddBG10 vddBG9 vddBG8 vddBG7 vddBG6 
 + vddBG5 vddBG4 vddBG3 vddBG2 vddBG1 
 + vddBG0 vssSG65 PowerModel


R0 vddBG0  0 0.1
Vss0 vssBG0 0 0
R1 vddBG1  0 0.1
Vss1 vssBG1 0 0
R2 vddBG2  0 0.1
Vss2 vssBG2 0 0
R3 vddBG3  0 0.1
Vss3 vssBG3 0 0
Vt vddBG4 0 PU (1 0.9 5NS 0.2NS 0.2NS 5NS 10.4NS)
Vss4 vssBG4 0 0
R5 vddBG5  0 0.1
Vss5 vssBG5 0 0
R6 vddBG6  0 0.1
Vss6 vssBG6 0 0
R7 vddBG7  0 0.1
Vss7 vssBG7 0 0
R8 vddBG8  0 0.1
Vss8 vssBG8 0 0
R9 vddBG9  0 0.1
Vss9 vssBG9 0 0
R10 vddBG10  0 0.1
Vss10 vssBG10 0 0
R11 vddBG11  0 0.1
Vss11 vssBG11 0 0
R12 vddBG12  0 0.1
Vss12 vssBG12 0 0
R13 vddBG13  0 0.1
Vss13 vssBG13 0 0
R14 vddBG14  0 0.1
Vss14 vssBG14 0 0
R15 vddBG15  0 0.1
Vss15 vssBG15 0 0
R16 vddBG16  0 0.1
Vss16 vssBG16 0 0
R17 vddBG17  0 0.1
Vss17 vssBG17 0 0
R18 vddBG18  0 0.1
Vss18 vssBG18 0 0
R19 vddBG19  0 0.1
Vss19 vssBG19 0 0
R20 vddBG20  0 0.1
Vss20 vssBG20 0 0
R21 vddBG21  0 0.1
Vss21 vssBG21 0 0
R22 vddBG22  0 0.1
Vss22 vssBG22 0 0
R23 vddBG23  0 0.1
Vss23 vssBG23 0 0
R24 vddBG24  0 0.1
Vss24 vssBG24 0 0
R25 vddBG25  0 0.1
Vss25 vssBG25 0 0
R26 vddBG26  0 0.1
Vss26 vssBG26 0 0
R27 vddBG27  0 0.1
Vss27 vssBG27 0 0
R28 vddBG28  0 0.1
Vss28 vssBG28 0 0
R29 vddBG29  0 0.1
Vss29 vssBG29 0 0
R30 vddBG30 0 0.1
Vss30 vssBG30 0 0
R31 vddBG31  0 0.1
Vss31 vssBG31 0 0
R32 vddBG32  0 0.1
Vss32 vssBG32 0 0
R33 vddBG33  0 0.1
Vss33 vssBG33 0 0
R34 vddBG34  0 0.1
Vss34 vssBG34 0 0


.tran 20ps 15ns
.probe TRAN I(R0)
.option post accurate probe
.end