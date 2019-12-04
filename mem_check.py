#!/usr/bin/python
with open('/proc/meminfo') as f:
  for line in f:
    if line.startswith('MemTotal'):
      total=line.split()[1]
      continue
    if line.startswith('MemFree'):
      free=line.split()[1]
      break
print("总量=%.2f" % (int(total)/1024.0)+'M')
print("空闲=%.2f" % (int(free)/1024.0)+'M')
print("空闲率=%.2f" % (int(free)/int(total)))
