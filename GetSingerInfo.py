#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import urllib2
from xml.dom.minidom import parse, parseString
#import MySQLdb 

def GetContent():
    content = urllib2.urlopen("http://baike.soso.com/Wap.htm?orig=1205&id=264&lid=124277").read()
    fd = file("qianming.xml", "w")
    fd.write(content);
    fd.close()
    print content


def GetSigerId():
    shost = "172.27.31.7";
    suser = "QueryCring";
    spass = "QueryCring";
    sdbname = "Client_Music_Res_DB";
    db_conn = MySQLdb.connect(host=shost, user=suser, passwd=spass, db=sdbname)
    cursor = db_conn.cursor()
    sql = "select singer_id,singer_name from WX_QM_Singer_Info limit 100"
    count = cursor.execute(sql)
    lines = []
    for line in cursor.fetchall():
        tmp = line[0]+','+line[1]+'\n'
        lines.append(tmp)
    fd = file("singer_id,txt", "w")
    fd.writelines(lines)
    fd.close()


if __name__ == "__main__":
    GetSigerId()
    #GetContent()
