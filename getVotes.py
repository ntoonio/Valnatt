#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import xmltodict

"""
regionType
----------
> "kommundistrikt"
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

def getVotes(electionType, region):
	if len(region) > 6:
		data = readFile(region[:4] + electionType)

		def _getDistrikt(dist, region):
			for d in dist:
				if isinstance(d, str):
					return {"NAMN": dist["NAMN"], "RÖSTER": dist["GILTIGA"]}
				elif isinstance(k, dict):
					if d["KOD"] == region:
						return {"NAMN": d["NAMN"], "RÖSTER": d["GILTIGA"]}

		for k in data["VAL"]["KOMMUN"]["KRETS_KOMMUN"]:
			if isinstance(k, str):
				dist = data["VAL"]["KOMMUN"]["KRETS_KOMMUN"]["VALDISTRIKT"]
				return _getDistrikt(dist, region)
			elif isinstance(k, dict):
				return _getDistrikt(k["VALDISTRIKT"], region)

	elif len(region) == 6:
		data = readFile(region[:4] + electionType)

		for d in data["VAL"]["KOMMUN"]["KRETS_KOMMUN"]:
			if d["KOD"] == region:
				return {"NAMN": d["NAMN"], "RÖSTER": d["GILTIGA"]}

	elif len(region) == 4:
		data = readFile(region[:4] + electionType)

		return {"NAMN": data["VAL"]["KOMMUN"]["NAMN"], "RÖSTER": data["VAL"]["KOMMUN"]["GILTIGA"]}

	elif len(region) == 2 and region != "00":
		data = readFile("00" + electionType)
		for l in data["VAL"]["NATION"]["LÄN"]:
			for k in l["KRETS_RIKSDAG"]:
				if isinstance(k, str):
					if l["KRETS_RIKSDAG"]["KOD"][-2:] == region:
						return {"NAMN": l["KRETS_RIKSDAG"]["NAMN"], "RÖSTER": l["KRETS_RIKSDAG"]["GILTIGA"]}
					break
				elif isinstance(k, dict):
					if k["KOD"][-2:] == region:
						return {"NAMN": k["NAMN"], "RÖSTER": k["GILTIGA"]}


	elif electionType == "R":
		data = readFile("00R")

		return {"NAMN": data["VAL"]["NATION"]["NAMN"], "RÖSTER": data["VAL"]["NATION"]["GILTIGA"]}

def readFile(fileCode):
	fileName = "data/valnatt_" + fileCode + ".xml"
	with io.open(fileName, "r", encoding="iso-8859-1") as xml_file:
		obj = xmltodict.parse(xml_file.read(), attr_prefix="")

	return obj

if __name__ == "__main__":
	import json

	votes = getVotes("R", "01170211")
	print(json.dumps(votes, ensure_ascii=False, indent=4))