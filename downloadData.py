#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import sys
import zipfile
import os

try:
	year = int(sys.argv[1])
except:
	print "Du måste ange ett numeriskt värde för vilket års data du vill hämta"
	exit(0)

if not (year - 2) % 4 == 0:
	print "Det var inget val det året"
	exit(0)

# Download the data
downloadUrl = "https://data.val.se/val/val" + year + "/valnatt/valnatt.zip"
urllib.urlretrieve(downloadUrl, "data/download.zip")

# Unpack the zip
zip_ref = zipfile.ZipFile("data/download.zip", "r")
zip_ref.extractall("data/")
zip_ref.close()

# Remove the zip
os.remove("data/download.zip")