from weibo import APIClient
import webbrowser
import json


def event_func():
    APP_KEY='2218208544'
    APP_SECRET='956ae245a2f62a11a9eca1d91fbda092'
    CALLBACK_URL='http://cdgir.cumt.edu.cn/ShowCode.aspx'
    client=APIClient(app_key=APP_KEY,app_secret=APP_SECRET,\
                     redirect_uri=CALLBACK_URL)
    url=client.get_authorize_url()
    print url
    webbrowser.open(url)

    code=raw_input("input the code:").strip()
    print code
    r=client.request_access_token(code);
    access_token=r.access_token
    expires_in=r.expires_in
    client.set_access_token(access_token,expires_in)
    poi_result=client.place.nearby.pois.get(lat='39.98435',long='116.30999')

    text=""
    print poi_result.total_number
    for val in poi_result.pois:
        #for k, v in val.items():
            #print ("%s : %s" % (k,v))这个是val这个dic的循环遍历
        text+="%s\t%s\t%s\t%s\t%s\r\n" % (val.poiid,val.title,val.lon,val.lat,val.address)#可参考api的json返回示例

    #print text.encode('utf-8')
    #print text.encode('utf-8')
    open('poi.txt','a').write(text.encode('utf-8'))
    #为什么不用每隔10秒钟取一次数据？因为你给的lat和long固定了，所以每次请求的数据都是确定的，都一样，这个查询
    #相当于点的周围位置查询

def main():
    event_func()

if __name__=='__main__':
    main()
