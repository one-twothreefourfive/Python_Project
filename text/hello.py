#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("hello world");
print("hello world,tan zheng,1991 07 03");
print("hello world","tan zheng","1991 07 03");

x='中文'.encode('utf-8')
y=b'ABC'.decode('ascii')
b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print("%d"%(len("ABC")))
print("%s"%(chr(66)))
print("%s"%('\u4e2d\u6587'))
z = b'ABC'
print("%s"%(x))
xx=x.decode('utf-8')
print("%s"%(xx))

name = input('please enter your name: ')
print('hello,', name)

s1=72
s2=85
r1=85*100/72
print("%0.1f"%(r1))