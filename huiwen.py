import time
def huiwen(num):
    index = 10000
    maxn = 999999
    sum = 0
    li = []
    for data in xrange(index,maxn):
        strind=str(data)
        strrver = strind[::-1]
        strvar=list(strind)
        for i in strvar:
            sum+=int(i)
        if strind==strrver and sum==num:
            li.append(data)
        sum=0
    return li
if __name__=='__main__':
    lis = []
    for n in xrange(5,60):
        lis.extend(huiwen(5))
    starttime = time.time()
    for i in lis:
        print i
    endtime = time.time()
    print 'totaltime:%f'%(endtime-starttime)
        
        
        
        
        
        
        
    