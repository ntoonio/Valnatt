import xmltodict
import io

def readFile(fileCode):
	fileName = "data/valnatt_" + fileCode + ".xml"
	with io.open(fileName, "r", encoding="iso-8859-1") as xml_file:
		obj = xmltodict.parse(xml_file.read(), attr_prefix="")

	return obj

def getRiksdagskrets():
	obj = readFile("00R")
	resp = []
	for l in obj["VAL"]["NATION"]["LÄN"]:
		for k in l["KRETS_RIKSDAG"]:
			if isinstance(k, str):
				resp.append({"NAMN": l["KRETS_RIKSDAG"]["NAMN"], "KOD": l["KRETS_RIKSDAG"]["KOD"][-2:]})
				break
			elif isinstance(k, dict):
				resp.append({"NAMN": k["NAMN"], "KOD": k["KOD"][-2:]})

	return resp

def getKommuner(region):
	obj = readFile("00R")
	resp = []
	for l in obj["VAL"]["NATION"]["LÄN"]:
		for kr in l["KRETS_RIKSDAG"]:
			if isinstance(kr, str):
				if l["KRETS_RIKSDAG"]["KOD"][-2:] == region:
					for k in l["KRETS_RIKSDAG"]["KOMMUN"]:
						resp.append({"NAMN": k["NAMN"], "KOD": k["KOD"]})
						break

			elif isinstance(kr["KOMMUN"], list):
				if kr["KOD"][-2:] == region:
					for k in kr["KOMMUN"]:
						resp.append({"NAMN": k["NAMN"], "KOD": k["KOD"]})

	return resp

def getKommunKretsar(region):
	if len(region) == 2:
		region = "OO"

	obj = readFile(region + "K")

	resp = []
	
	for k in obj["VAL"]["KOMMUN"]["KRETS_KOMMUN"]:
		if isinstance(k, str):
			k = obj["VAL"]["KOMMUN"]["KRETS_KOMMUN"]
			resp.append({"NAMN": k["NAMN"], "KOD": k["KOD"]})
			break
		elif isinstance(k, dict):
			resp.append({"NAMN": k["NAMN"], "KOD": k["KOD"]})

	return resp

def getKommunDistrikt(code):
	obj = readFile(code[:4] + "K")

	resp = []
	
	def _getDistrikt(dist):
		resp = []
		for d in dist:
			if isinstance(k, str):
				d = obj["VAL"]["KOMMUN"]["KRETS_KOMMUN"]["VALDISTRIKT"]
				resp.append({"NAMN": d["NAMN"], "KOD": d["KOD"]})
				break
			elif isinstance(k, dict):
				resp.append({"NAMN": d["NAMN"], "KOD": d["KOD"]})

		return resp

	for k in obj["VAL"]["KOMMUN"]["KRETS_KOMMUN"]:
		if isinstance(k, str):
			dist = obj["VAL"]["KOMMUN"]["KRETS_KOMMUN"]["VALDISTRIKT"]
			resp = _getDistrikt(dist)
			break
		elif isinstance(k, dict):
			if k["KOD"] == code:
				dist = k["VALDISTRIKT"]
				resp = _getDistrikt(dist)

	return resp

if __name__ == "__main__":
	import json

	#regions = getRiksdagskrets()
	regions = getKommuner("02")
	#regions = getKommunKretsar("0117")
	#regions = getKommunDistrikt("011701")
	print(json.dumps(regions, ensure_ascii=False, indent=4))