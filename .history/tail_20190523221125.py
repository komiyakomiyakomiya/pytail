#!/usr/bin/env python
#_*_ coding: utf-8 _*_:q
import subprocess

filename = 'test.log'
cmd = ('tail -n +1 --follow=name ' + filename)
p = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(p)
while True:
  print  p.stdout.readline()