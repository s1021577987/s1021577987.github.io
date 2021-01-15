#!/usr/bin/python
# -*- coding: utf-8 -*-
import base64

in_f = open("vmess.html", "r")
read_data = in_f.read()
in_f.close()

out_f = open("index.html", "w")
out_f.write(base64.b64encode(read_data))
out_f.close()