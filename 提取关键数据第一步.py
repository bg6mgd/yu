import queue
q=queue.Queue(3)
f = open('Device.txt','r+',encoding='utf-8')
data=open('test.txt','a')
zz=open('zz.txt','a')
ret = f.readline()

while ret:
    if ret.find("���������Ϣ")!=-1:
        data.write(ret)
    elif ret.find("����")!=-1:
        data.write(ret)
    elif ret.find("����")!=-1:
        if ret.find("�������")!=-1:
            data.write(ret)
    ret = f.readline()



f.close()
data.close()
zz.close()