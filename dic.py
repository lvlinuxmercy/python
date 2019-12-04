#!/usr/bin/python
name = input("please input name: ")
age = input("please input age: ")
gender = input("please input gender M/F: ")
info = {}
info['name'] = name
info['age'] = age
info['gender'] = gender
print(info)
print(info.items())
for k,v in info.items():
    print("%s: %s" % (k,v))
