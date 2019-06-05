#coding=utf-8
import urllib
import httplib
import gzip
import sys
import base64
from xml.dom.minidom import parse, parseString

def getReq(ver, cid, gt, gl):
    req = '<?xml version="1.0" encoding="UTF-8"?>\
<root>\
<uid></uid>\
<imei>0</imei>\
<sid>123123123123</sid>\
<v>%s</v>\
<qq>0</qq>\
<cid>%s</cid>\
<gt>%s</gt>\
<gl>%s</gl>\
<music>5ZGo</music>\
<sin>0</sin>\
<ein>5</ein>\
<mt>bW9sbw==</mt>\
<channel></channel>\
</root>' % (ver, cid, gt, gl)
    return req

def getReqSinEin(ver, cid, gt, gl, sin, ein):
    req = '<?xml version="1.0" encoding="UTF-8"?>\
<root>\
<uid></uid>\
<imei>0</imei>\
<sid>123123123123</sid>\
<v>%s</v>\
<qq>0</qq>\
<cid>%s</cid>\
<gt>%s</gt>\
<gl>%s</gl>\
<music>eg==</music>\
<sin>%d</sin>\
<ein>%d</ein>\
<mt>bW9sbw==</mt>\
<channel></channel>\
</root>' % (ver, cid, gt, gl, sin, ein)
    return req

def getResponse(host, port, req):
    conn = httplib.HTTPConnection(host + ":" + port)

    headers = {"Accept": "text/plain"}

    print 100 * "-"
    print "request: " + host + ":" + port
    print 100 * "-"
    print req
    print 100 * "-"

    conn.request("POST", "/", req, headers)

    resp = conn.getresponse()

    print "response: ", resp.status, resp.reason 
    print 100 * "-"

    data = resp.read()

    conn.close()

    file = open('.tmp.gz','w')
    file.write(data[5:])
    file.close()

    f = gzip.open('.tmp.gz','r')
    xmltext = f.read()
    f.close()
    
    return xmltext


def decodeBase64(xmltext):
    domxml = parseString(xmltext)
    root_node = domxml.documentElement

    utxt_node = root_node.getElementsByTagName('utxt')
    for utxt in utxt_node:
        utxt.firstChild.data = base64.b64decode(utxt.firstChild.data).decode('utf8','ignore')

    info_nodes = root_node.getElementsByTagName('info1')
    for info in info_nodes:
        info.firstChild.data = base64.b64decode(info.firstChild.data).decode('utf8','ignore')
        
    info_nodes = root_node.getElementsByTagName('info2')
    for info in info_nodes:
        info.firstChild.data = base64.b64decode(info.firstChild.data).decode('utf8','ignore')

    info_nodes = root_node.getElementsByTagName('info3')
    for info in info_nodes:
        info.firstChild.data = base64.b64decode(info.firstChild.data).decode('utf8','ignore')

    desc_nodes = root_node.getElementsByTagName('albumdesc')
    for desc in desc_nodes:
        desc.firstChild.data = base64.b64decode(desc.firstChild.data).decode('utf8','ignore')

    print root_node.toxml().encode('gbk','ignore')


if __name__ == '__main__':

    # host = 'test3.wapmusic.qq.com'
    host = '10.135.0.18'
    # port = '80'
    port = '18151'

    #MOLO version
    ver = 146

    req = getReq(ver, 1000117, 0, 0)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)

#    req = getReq(ver, 1000102, 0, "SINGER-1")
#    xmltext = getResponse(host, port, req)
#    decodeBase64(xmltext)

    req = getReq(ver, 1000102, 9, 5)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)

    '''
    #test 1000100_GetSession
    req = getReq(ver, 1000100, 0, 0)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)        

    #test 1000101_GetHomepage
    req = getReq(ver, 1000101, 0, 0)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)
    
    #test 1000102_点击推广图片_不想去上班
    req = getReq(ver, 1000102, 1, 95126)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)
    
    #test 1000102_华语新歌榜
    req = getReq(ver, 1000102, 9, 5)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)

    #test 1000102_华语排行榜
    req = getReq(ver, 1000102, 9, 1)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)

    #test 1000102_QQ音乐总榜
    req = getReq(ver, 1000102, 9, 0)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)

    #test 1000102_日韩排行榜
    req = getReq(ver, 1000102, 9, 2)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)

    #test 1000102_欧美排行榜
    req = getReq(ver, 1000102, 9, 3)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)
    
    #test 1000102_新歌
    req = getReq(ver, 1000102, 14, 6)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)
    
    #test 1000117_取歌手榜单列表
    req = getReq(ver, 1000117, 0, 0)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)
    
    #test 1000131_取歌曲榜单列表
    req = getReq(ver, 1000131, 0, 0)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)

    #test 1000102_华语男歌手
    req = getReq(ver, 1000102, 0, 'SINGER-1')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    
        
    #test 1000102_华语女歌手
    req = getReq(ver, 1000102, 0, 'SINGER-2')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    
    
    #test 1000102_华语组合
    req = getReq(ver, 1000102, 0, 'SINGER-3')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)        
    
    #test 1000102_日韩男歌手
    req = getReq(ver, 1000102, 0, 'SINGER-4')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    
    
    #test 1000102_日韩女歌手
    req = getReq(ver, 1000102, 0, 'SINGER-5')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    
    
    #test 1000102_日韩组合
    req = getReq(ver, 1000102, 0, 'SINGER-6')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)        
        
    #test 1000102_欧美男歌手
    req = getReq(ver, 1000102, 0, 'SINGER-7')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    

    #test 1000102_欧美女歌手
    req = getReq(ver, 1000102, 0, 'SINGER-8')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    
    
    #test 1000102_欧美组合
    req = getReq(ver, 1000102, 0, 'SINGER-9')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    
                
    #test 1000102_其他歌手
    req = getReq(ver, 1000102, 0, 'SINGER-10')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    
    
    #test 1000102_欧美男歌手 中的 热门歌手
    #^号，表示取热门歌手
    req = getReq(ver, 1000102, 0, 'SINGER-7^') 
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    

    #test 1000102_在_全部歌手_查找以字母c开头的歌手'
    #规则：以‘歌手榜单’+‘首字母’的形式，确定要搜索的范围
    req = getReq(ver, 1000102, 0, 'SINGER-12c')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    
    
    #test 1000102_在_华语组合_查找以字母c开头的歌手
    req = getReq(ver, 1000102, 0, 'SINGER-3c')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    
        
    #test 1000102_在_欧美男歌手_查找以字母a-z以外开头的歌手
    req = getReq(ver, 1000102, 0, 'SINGER-3#')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)
            
    #test 1000110_按照歌曲名搜索
    req = getReq(ver, 1000110, 100, 5)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)
    
    #test 1000110_按照歌手名搜索
    req = getReq(ver, 1000110, 100, 6)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)        

    #test 1000110_按照歌曲名+歌手名搜索
    req = getReq(ver, 1000110, 100, 7)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    

    #test 1000110_按照专辑名搜索
    req = getReq(ver, 1000110, 100, 8)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    

    #test 1000122_联想输入
    req = getReq(ver, 1000122, 0, 0)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    
    
    #test 1000102_取指定专辑的歌曲列表_《西安事变》
    req = getReq(ver, 1000102, 1, 95125)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    
        
    #test 1000102_取专辑列表
    req = getReq(ver, 1000102, 0, 'ALBUM-8')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    

    #test 1000115_随机取歌
    req = getReq(ver, 1000115, 0, 0)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    

    #test 1000118_取热词（人工配置）
    req = getReq(ver, 1000118, 0, 0)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    

    #test 1000110_按照歌曲名搜索
    req = getReqSinEin(ver, 1000110, 100, 5, 10, 19)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)            
    
    #test 1000102_所有歌手
    req = getReqSinEin(ver, 1000102, 0, 'SINGER-12', 0, 14)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)        
    
    #test 1000102_所有歌手 里面的 热门歌手
    req = getReqSinEin(ver, 1000102, 0, 'SINGER-12^', 0, 14)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    

    #test 1000102_取专辑的列表
    req = getReq(ver, 1000131, 5, 0)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)

    #test 1000102_取专辑详情_全部地区
    req = getReq(ver, 1000102, 5, 0)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)

    #test 1000102_取专辑详情_华语地区
    req = getReq(ver, 1000102, 5, 1)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)

    #test 1000102_取专辑详情_欧美地区
    req = getReq(ver, 1000102, 5, 2)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)

    #test 1000102_取专辑详情_日韩地区
    req = getReq(ver, 1000102, 5, 3)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)

    #test 1000102_取专辑详情_小语种和其他地区
    req = getReq(ver, 1000102, 5, 4)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)
    
    #test 1000102_在欧美专辑中查找以'd'开头的专辑
    req = getReq(ver, 1000102, 5, '2d')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)

    #test 1000102_取华语专辑中的“热门专辑”
    #注意：热门专辑不支持组合查找，即“查找以字母d开头的热门专辑”
    req = getReq(ver, 1000102, 5, '1^')
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)
    
    #test 1000102_取专辑详情
    #专辑语言：0 国语,1 粤语,2 台语,3 日语,4 韩语,5 英语,6 法语,7 其他,8 拉丁
    req = getReq(ver, 1000102, 6, 91325)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)
    
    #test 1000102_取指定专辑的歌曲列表
    req = getReq(ver, 1000102, 1, 91325)
    xmltext = getResponse(host, port, req)
    decodeBase64(xmltext)    
    '''
    
