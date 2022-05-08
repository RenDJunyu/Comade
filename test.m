clc
clear
[NUM]=xlsread('isee_grades',1,'A2:K22');

lb=[zeros(140,1);-Inf;-Inf;-Inf;-Inf;-Inf;-Inf;-Inf;zeros(10,1)];
ub=repmat(Inf,157,1);
b=zeros(70,1);

A=[1,zeros(1,69),1,zeros(1,69),zeros(1,7),-1,zeros(1,9);
    0,1,zeros(1,68),0,1,zeros(1,68),zeros(1,7),-1,zeros(1,9);
    0,0,1,zeros(1,67),0,0,1,zeros(1,67),zeros(1,7),-1,zeros(1,9);
    0,0,0,1,zeros(1,66),0,0,0,1,zeros(1,66),zeros(1,7),-1,zeros(1,9);
    0,0,0,0,1,zeros(1,65),0,0,0,0,1,zeros(1,65),zeros(1,7),-1,zeros(1,9);
    0,0,0,0,0,1,zeros(1,64),0,0,0,0,0,1,zeros(1,64),zeros(1,7),-1,zeros(1,9);
    0,0,0,0,0,0,1,zeros(1,63),0,0,0,0,0,0,1,zeros(1,63),zeros(1,7),-1,zeros(1,9);
    zeros(1,7),1,zeros(1,62),zeros(1,7),1,zeros(1,62),zeros(1,7),0,-1,zeros(1,8);
    zeros(1,8),1,zeros(1,61),zeros(1,8),1,zeros(1,61),zeros(1,7),0,-1,zeros(1,8);
    zeros(1,9),1,zeros(1,60),zeros(1,9),1,zeros(1,60),zeros(1,7),0,-1,zeros(1,8);
    zeros(1,10),1,zeros(1,59),zeros(1,10),1,zeros(1,59),zeros(1,7),0,-1,zeros(1,8);
    zeros(1,11),1,zeros(1,58),zeros(1,11),1,zeros(1,58),zeros(1,7),0,-1,zeros(1,8);
    zeros(1,12),1,zeros(1,57),zeros(1,12),1,zeros(1,57),zeros(1,7),0,-1,zeros(1,8);
    zeros(1,13),1,zeros(1,56),zeros(1,13),1,zeros(1,56),zeros(1,8),-1,zeros(1,8);
    zeros(1,14),1,zeros(1,55),zeros(1,14),1,zeros(1,55),zeros(1,9),-1,zeros(1,7);
    zeros(1,15),1,zeros(1,54),zeros(1,15),1,zeros(1,54),zeros(1,9),-1,zeros(1,7);
    zeros(1,16),1,zeros(1,53),zeros(1,16),1,zeros(1,53),zeros(1,9),-1,zeros(1,7);
    zeros(1,17),1,zeros(1,52),zeros(1,17),1,zeros(1,52),zeros(1,9),-1,zeros(1,7);
    zeros(1,18),1,zeros(1,51),zeros(1,18),1,zeros(1,51),zeros(1,9),-1,zeros(1,7);
    zeros(1,19),1,zeros(1,50),zeros(1,19),1,zeros(1,50),zeros(1,9),-1,zeros(1,7);
    zeros(1,20),1,zeros(1,49),zeros(1,20),1,zeros(1,49),zeros(1,9),-1,zeros(1,7);
    zeros(1,21),1,zeros(1,48),zeros(1,21),1,zeros(1,48),zeros(1,10),-1,zeros(1,6);
    zeros(1,22),1,zeros(1,47),zeros(1,22),1,zeros(1,47),zeros(1,10),-1,zeros(1,6);
    zeros(1,23),1,zeros(1,46),zeros(1,23),1,zeros(1,46),zeros(1,10),-1,zeros(1,6);
    zeros(1,24),1,zeros(1,45),zeros(1,24),1,zeros(1,45),zeros(1,10),-1,zeros(1,6);
    zeros(1,25),1,zeros(1,44),zeros(1,25),1,zeros(1,44),zeros(1,10),-1,zeros(1,6);
    zeros(1,26),1,zeros(1,43),zeros(1,26),1,zeros(1,43),zeros(1,10),-1,zeros(1,6);
    zeros(1,27),1,zeros(1,42),zeros(1,27),1,zeros(1,42),zeros(1,10),-1,zeros(1,6);
        zeros(1,28),1,zeros(1,41),zeros(1,28),1,zeros(1,41),zeros(1,11),-1,zeros(1,5);
    zeros(1,29),1,zeros(1,40),zeros(1,29),1,zeros(1,40),zeros(1,11),-1,zeros(1,5);
    zeros(1,30),1,zeros(1,39),zeros(1,30),1,zeros(1,39),zeros(1,11),-1,zeros(1,5);
    zeros(1,31),1,zeros(1,38),zeros(1,31),1,zeros(1,38),zeros(1,11),-1,zeros(1,5);
    zeros(1,32),1,zeros(1,37),zeros(1,32),1,zeros(1,37),zeros(1,11),-1,zeros(1,5);
    zeros(1,33),1,zeros(1,36),zeros(1,33),1,zeros(1,36),zeros(1,11),-1,zeros(1,5);
    zeros(1,34),1,zeros(1,35),zeros(1,34),1,zeros(1,35),zeros(1,11),-1,zeros(1,5);
    zeros(1,35),1,zeros(1,34),zeros(1,35),1,zeros(1,34),zeros(1,12),-1,zeros(1,4);
    zeros(1,36),1,zeros(1,33),zeros(1,36),1,zeros(1,33),zeros(1,12),-1,zeros(1,4);
    zeros(1,37),1,zeros(1,32),zeros(1,37),1,zeros(1,32),zeros(1,12),-1,zeros(1,4);
    zeros(1,38),1,zeros(1,31),zeros(1,38),1,zeros(1,31),zeros(1,12),-1,zeros(1,4);
    zeros(1,39),1,zeros(1,30),zeros(1,39),1,zeros(1,30),zeros(1,12),-1,zeros(1,4);
    zeros(1,40),1,zeros(1,29),zeros(1,40),1,zeros(1,29),zeros(1,12),-1,zeros(1,4);
    zeros(1,41),1,zeros(1,28),zeros(1,41),1,zeros(1,28),zeros(1,12),-1,zeros(1,4);
        zeros(1,42),1,zeros(1,27),zeros(1,42),1,zeros(1,27),zeros(1,13),-1,zeros(1,3);
    zeros(1,43),1,zeros(1,26),zeros(1,43),1,zeros(1,26),zeros(1,13),-1,zeros(1,3);
    zeros(1,44),1,zeros(1,25),zeros(1,44),1,zeros(1,25),zeros(1,13),-1,zeros(1,3);
    zeros(1,45),1,zeros(1,24),zeros(1,45),1,zeros(1,24),zeros(1,13),-1,zeros(1,3);
    zeros(1,46),1,zeros(1,23),zeros(1,46),1,zeros(1,23),zeros(1,13),-1,zeros(1,3);
    zeros(1,47),1,zeros(1,22),zeros(1,47),1,zeros(1,22),zeros(1,13),-1,zeros(1,3);
    zeros(1,48),1,zeros(1,21),zeros(1,48),1,zeros(1,21),zeros(1,13),-1,zeros(1,3);
    zeros(1,49),1,zeros(1,20),zeros(1,49),1,zeros(1,20),zeros(1,14),-1,zeros(1,2);
    zeros(1,50),1,zeros(1,19),zeros(1,50),1,zeros(1,19),zeros(1,14),-1,zeros(1,2);
    zeros(1,51),1,zeros(1,18),zeros(1,51),1,zeros(1,18),zeros(1,14),-1,zeros(1,2);
    zeros(1,52),1,zeros(1,17),zeros(1,52),1,zeros(1,17),zeros(1,14),-1,zeros(1,2);
    zeros(1,53),1,zeros(1,16),zeros(1,53),1,zeros(1,16),zeros(1,14),-1,zeros(1,2);
    zeros(1,54),1,zeros(1,15),zeros(1,54),1,zeros(1,15),zeros(1,14),-1,zeros(1,2);
    zeros(1,55),1,zeros(1,14),zeros(1,55),1,zeros(1,14),zeros(1,14),-1,zeros(1,2);
        zeros(1,56),1,zeros(1,13),zeros(1,56),1,zeros(1,13),zeros(1,15),-1,zeros(1,1);
    zeros(1,57),1,zeros(1,12),zeros(1,57),1,zeros(1,12),zeros(1,15),-1,zeros(1,1);
    zeros(1,58),1,zeros(1,11),zeros(1,58),1,zeros(1,11),zeros(1,15),-1,zeros(1,1);
    zeros(1,59),1,zeros(1,10),zeros(1,59),1,zeros(1,10),zeros(1,15),-1,zeros(1,1);
    zeros(1,60),1,zeros(1,9),zeros(1,60),1,zeros(1,9),zeros(1,15),-1,zeros(1,1);
    zeros(1,61),1,zeros(1,8),zeros(1,61),1,zeros(1,8),zeros(1,15),-1,zeros(1,1);
    zeros(1,62),1,zeros(1,7),zeros(1,62),1,zeros(1,7),zeros(1,15),-1,zeros(1,1);
    zeros(1,63),1,zeros(1,6),zeros(1,63),1,zeros(1,6),zeros(1,16),-1;
    zeros(1,64),1,zeros(1,5),zeros(1,64),1,zeros(1,5),zeros(1,16),-1;
    zeros(1,65),1,zeros(1,4),zeros(1,65),1,zeros(1,4),zeros(1,16),-1;
    zeros(1,66),1,zeros(1,3),zeros(1,66),1,zeros(1,3),zeros(1,16),-1;
    zeros(1,67),1,zeros(1,2),zeros(1,67),1,zeros(1,2),zeros(1,16),-1;
    zeros(1,68),1,zeros(1,1),zeros(1,68),1,zeros(1,1),zeros(1,16),-1;
    zeros(1,69),1,zeros(1,69),1,zeros(1,16),-1];

x0=zeros(157,1);

x=fmincon(@(x0)func(x0,NUM),x0,A,b,[],[],lb,ub)



    