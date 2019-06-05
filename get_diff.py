import os
import sys

charge_set = set() 
for line in open("./uniq_charge", "r"):
    fields = line.strip("\r\n").split(" ")
    routeid = fields[0]
    serial = fields[1]
    sub_id = routeid.split(".")
    sub_id[3] = "0"
    routeid = ".".join(list(sub_id))
    key = "%s:%s"%(routeid,serial)
    charge_set.add(key)

raw_set = set()
for line in open("./uniq_raw", "r"):
    fields = line.strip("\r\n").split(" ")
    routeid = fields[0]
    serial = fields[1]
    key = "%s:%s"%(routeid,serial)
    raw_set.add(key)

print (raw_set) - (charge_set)
    


