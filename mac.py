#!/usr/bin/env python
mac='00:16:3E:0B:C8:FF'
mac_start5=mac[:-3]
mac_last1=mac[-2:]
new_last1=hex(int(mac_last1,16)+1)
if len(new_last1)==3:
  new_last1='0'+new_last1[-1:]
new_mac=mac_start5+':'+new_last1[-2:].upper()
print (mac)
print (new_mac)
