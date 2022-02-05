    %旅行家问题尝试实现
    %生成随机城市点
    
    size =100; %问题规模
    sites = exprnd (size/10 ,size, 2); %生成的城市顺序不再改变，以作为代号1:size

    %计算每个城市之间的距离

    distance_map=inf(size*(size-1)/2,4);
    WR_loc=1;
    for i=1:size
        for j=i+1:size
            distance_map(WR_loc,:)=[i,j,((sites(i,1)-sites(j,1))^2+(sites(i,2)-sites(j,2))^2)^0.5,0];
            WR_loc=WR_loc+1;
        end
    end
    %对每个城市与其他城市之间的距离进行排序
    [orderes,index]=sort(distance_map(:,3));
    linknum=zeros(size,1);
    linksum=0;
    %循环选择最小的距离，进行连接
    %处于路线中间(即三个城市的中间)的城市，被划去
    
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

    %todo 如何有效避免形成闭环
    %连接时进行标记

    %将路线重排，从起点开始，从而方便绘制
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

    %绘制路线图
    plot(sites(out_line,1),sites(out_line,2));
