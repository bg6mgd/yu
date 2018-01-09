f = open('Device.txt','r+',encoding='utf-8')
data=open('test.txt','a')
zz=open('zz.txt','a')
retdata = f.readline()

ret=retdata[23:]

str=["a","b","c"]
i=0
while ret:

    if ret.find("获得轮轴信息")!=-1:
        i=+1
        str[1]=ret

        data.write(ret)
    elif ret.find("车牌")!=-1:
        print(ret)
        str[2]=ret
        data.write(ret)
    elif ret.find("轴数")!=-1:
        if ret.find("数据入库")!=-1:
            str[0]=ret
            print(ret)
            data.write(ret)
    elif (str[0].find("数据入库")!=-1)and(str[1].find("获得轮轴信息")!=-1)and(str[2].find("入库成功")!=-1):
            for dd in str:
                zz.write(dd)
            str.clear()

    retdata = f.readline()
    if len(retdata)>24:
        ret = retdata[23:]
    else:
        ret=retdata


f.close()
data.close()
zz.close()
