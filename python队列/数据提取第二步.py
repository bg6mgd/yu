import collections
d = collections.deque()

f = open('test.txt','r+')
zz=open('zz.txt','a')
for i in range(3):
    ret = f.readline()
    print(ret)
    d.append(ret)

    print("----------------------")
    print(d)
    print("**********************")
while True:
    dc=d.copy()
    data1=dc.pop()
    data2=dc.pop()
    data3=dc.pop()


    if (data1.find("车牌")!=-1)and(data2.find("轴数")!=-1)and(data3.find("获得")!=-1):
        zz.write(data1)
        zz.write(data2)
        zz.write(data3)
        d.clear()
        for i in range(3):
            ret=f.readline()
            d.append(ret)
    else:
        d.pop()
        ret=f.readline()
        d.append(ret)










f.close()
zz.close()