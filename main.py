import weibo
import json
import webbrowser
import time

#前面的APP_KEY和APP_SECRET可以从文件或者别的途径获取
APP_KEY='2218208544'
APP_SECRET='956ae245a2f62a11a9eca1d91fbda092'
CALLBACK_URL='http://cdgir.cumt.edu.cn/ShowCode.aspx'
Cache=[] #全局poiid

def event_func():
    client=weibo.APIClient(APP_KEY,APP_SECRET,CALLBACK_URL)
    url=client.get_authorize_url()
    webbrowser.open(url)
    code=raw_input("input the code:").strip()
    r=client.request_access_token(code);
    client.set_access_token(r.access_token,r.expires_in)
    count=50 #请求数
    page=1 #请求的页码
    requestNum=0
    lat_long=['39.90960','116.39']#这个可以从文件中获取坐标点
    latitude=lat_long[0]
    longitude=lat_long[1]
    poi_result=client.place.nearby.pois.get(lat='39.98435',long='116.30999',count=50,page=page)
    requestNum=1
    total_number=poi_result.total_number
    
    if (total_number>0) and (int(total_number)%count!=0):
        page=int(total_number)/count+1
    else:
        page=int(total_number)/count

    text=""
    for val in poi_result.pois:
        if val.poiid in Cache:
            pass
        else:
            Cache.append(val.poiid)
            text+="%s,%s,%s,%s,%s\n" % (val.poiid,val.title,val.lon,val.lat,val.address)#可参考api的json返回示例
    if page==1:        
        return
    else:
        for pn in range(2,page+1):
            poi_result=client.place.nearby.pois.get(lat='39.98435',long='116.30999',count=50,page=pn)
            requestNum+=1
            for val in poi_result.pois:
                if val.poiid in Cache:
                    pass
                else:
                    Cache.append(val.poiid)
                    text+="%s, %s, %s %s, %s\n" % (val.poiid,val.title,val.lon,val.lat,val.address)#可参考api的json返回示例
        
    open('poi.txt','a').write(text.encode('utf-8'))
    print 'There are %d pages' % page
    print 'There are %d requests' % requestNum

def main():
    #for i in range(5):
        #event_func()
        #time.sleep(10)
    event_func()
    open('poid.txt','a').write(('\n').join(Cache))
    print 'done!'
    #上述东西我都测试过，不会出现重复现象，问题一并解决

if __name__=='__main__':
    main()
    
