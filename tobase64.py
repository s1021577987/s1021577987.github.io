#!/usr/bin/python
# -*- coding: utf-8 -*-
import base64

list_base64 = []

with open("vmess", "r") as fr:
	for line in fr:
		if line.find("vmess://") >= 0:
			v = base64.b64encode(line)
			v = v + "\n"
			list_base64.append(v)
			pass


out_f = open("index.html", "w")
out_f.writelines(list_base64)
out_f.close()