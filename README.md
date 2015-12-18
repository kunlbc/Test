1.CallBackURL换成了http://cdgir.cumt.edu.cn/ShowCode.aspx <br/>
2.数据写到txt里面不太好读，建议写进数据库<br/>
3.第二个链接没有问题<br/>
4.test.py和test2.py这两个文件是新写的<br/>
5.每隔一段时间进行抓取，应该主要是为了获得他的签到数据<br/>
6.考虑过为什么会出现重复的数据?这是因为你设置中心点不同时，因为有一个距离的原因，所以地点难免会有重叠，这才是重复数据的根本原因，在同一个请求中，不会出现数据重叠的情况，main.py中的代码已经验证了这个特点<br/>
<div style="border-top:1px solid #fa7d3c"></div>
