    %���м����Ⳣ��ʵ��
    %����������е�
    
    size =100; %�����ģ
    sites = exprnd (size/10 ,size, 2); %���ɵĳ���˳���ٸı䣬����Ϊ����1:size

    %����ÿ������֮��ľ���

    distance_map=inf(size*(size-1)/2,4);
    WR_loc=1;
    for i=1:size
        for j=i+1:size
            distance_map(WR_loc,:)=[i,j,((sites(i,1)-sites(j,1))^2+(sites(i,2)-sites(j,2))^2)^0.5,0];
            WR_loc=WR_loc+1;
        end
    end
    %��ÿ����������������֮��ľ����������
    [orderes,index]=sort(distance_map(:,3));
    linknum=zeros(size,1);
    linksum=0;
    %ѭ��ѡ����С�ľ��룬��������
    %����·���м�(���������е��м�)�ĳ��У�����ȥ
    
    WR_loc=1;
    while linksum<size-1
        map_loc=index(WR_loc);
        WR_loc=WR_loc+1;
        point1=distance_map(map_loc,1);
        point2=distance_map(map_loc,2);
        if(linknum(point1)==2 || linknum(point2)==2 )
            continue
        end
        linknum(point1)=linknum(point1)+1;
        linknum(point2)=linknum(point2)+1;
        linksum=linksum+1;
        distance_map(map_loc,4)=1;
    end

    %todo �����Ч�����γɱջ�
    %����ʱ���б��

    %��·�����ţ�����㿪ʼ���Ӷ��������
    tmp=find(linknum==1);
    startp=tmp(1);
    endp=tmp(2);
    used_route=find(distance_map(:,4)==1);
    LR_is=sum(distance_map(used_route,2)==startp);
    end1=0;
    end2=startp;
    out_line=zeros(size,1);
    out_line(1)=startp;
    WR_loc=2;
    while end2~=endp
        two_line=[find(distance_map(used_route,1)==end2);find(distance_map(used_route,2)==end2)];
        two_line=used_route(two_line);
        if(end1==0)
            anotherend=find(distance_map(two_line,1:2)~=end2);
        else  
            anotherend=[find(distance_map(two_line,1:2)~=end1 & distance_map(two_line,1:2)~=end2)];
        end
        end1=end2;
        end2=distance_map(two_line,anotherend);
        out_line(WR_loc)=end2;
        WR_loc=WR_loc+1;
    end    

    %����·��ͼ
    plot(sites(out_line,1),sites(out_line,2));
