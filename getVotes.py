#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import xmltodict

"""
regionType
----------
> "kommunkrets"
> "kommun"
> "län"
> "nation"

electionType
------------
> "K" - Kommun
> "L" - Landstring
> "R" - Riksdag
"""

import io

def getVotes(electionType, region):
	if region["typ"] == "kommunkrets":
		data = readFile(region["län"] + region["kommun"] + electionType)

		for d in data["VAL"]["KOMMUN"]["KRETS_KOMMUN"]:
			if d["KOD"] == region["län"] + region["kommun"] + region["krets"]:
				return d["GILTIGA"]

	elif region["typ"] == "kommun":
		data = readFile(region["län"] + region["kommun"] + electionType)

		return data["VAL"]["KOMMUN"]["GILTIGA"]

	elif region["typ"] == "län":
		data = readFile("00" + electionType)

		for d in data["VAL"]["NATION"]["LÄN"]:
			if d["KOD"] == region["län"] + region["kommun"] + region["krets"]:
				return d["GILTIGA"]

	elif region["typ"] == "nation":
		data = readFile("00R")

		return data["VAL"]["NATION"]["GILTIGA"]

def readFile(fileCode):
	fileName = "data/valnatt_" + fileCode + ".xml"
	with io.open(fileName, "r", encoding="iso-8859-1") as xml_file:
		obj = xmltodict.parse(xml_file.read(), attr_prefix="")

	return obj

if __name__ == "__main__":
	votes = getVotes("R", {"typ": "kommunkrets", "län": "01", "kommun": "17", "krets": "01"})
	print json.dumps(votes, ensure_ascii=False, indent=4)
	