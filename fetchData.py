#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import zipfile
import os

def fetchData(year, log = False):
	if not (year - 2) % 4 == 0:
		print "Det var inget val det året"
		return

	if not os.path.isdir("data/"):
		os.mkdir("data/")

	# Download the data
	if log: print "Downloading"
	downloadUrl = "https://data.val.se/val/val" + str(year) + "/valnatt/valnatt.zip"
	urllib.urlretrieve(downloadUrl, "data/download.zip")

	# Unpack the zip
	if log: print "Unpacking"
	zip_ref = zipfile.ZipFile("data/download.zip", "r")
	zip_ref.extractall("data/")
	zip_ref.close()

	# Remove the zip
	os.remove("data/download.zip")

if __name__ == "__main__":
	import sys

	try:
		year = int(sys.argv[1])
	except:
		print "Du maste ange ett numeriskt varde for vilket ars data du vill hamta"
		exit(0)
	
	fetchData(year, True)