import queue
q=queue.Queue(3)
f = open('Device.txt','r+',encoding='utf-8')
data=open('test.txt','a')
zz=open('zz.txt','a')
ret = f.readline()

while ret:
    if ret.find("获得轮轴信息")!=-1:
        data.write(ret)
    elif ret.find("车牌")!=-1:
        data.write(ret)
    elif ret.find("轴数")!=-1:
        if ret.find("数据入库")!=-1:
            data.write(ret)
    ret = f.readline()



f.close()
data.close()
zz.close()