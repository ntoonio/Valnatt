import xmltodict
import io

def readFile(fileCode):
	fileName = "data/valnatt_" + fileCode + ".xml"
	with io.open(fileName, "r", encoding="iso-8859-1") as xml_file:
		obj = xmltodict.parse(xml_file.read(), attr_prefix="")

	return obj

def getLan():
	obj = readFile("00R")
	resp = []
	for l in obj["VAL"]["NATION"]["LÄN"]:
		resp.append({"NAMN": l["NAMN"], "KOD": l["KOD"]})
	
	return resp

def getKommuner(lan):
	obj = readFile("00R")
	resp = []
	for l in obj["VAL"]["NATION"]["LÄN"]:
		if l["KOD"] == lan:
			for kr in l["KRETS_RIKSDAG"]:
				if isinstance(kr, str):
					for k in l["KRETS_RIKSDAG"]["KOMMUN"]:
						resp.append({"NAMN": k["NAMN"], "KOD": k["KOD"]})
					break

				elif isinstance(kr["KOMMUN"], list):
					for k in kr["KOMMUN"]:
						resp.append({"NAMN": k["NAMN"], "KOD": k["KOD"]})
					break

	return resp

def getKommunKretsar(code):
	obj = readFile(code + "K")

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

	#regions = getLan()
	#regions = getKommuner("05")
	#regions = getKommunKretsar("0117")
	regions = getKommunDistrikt("011701")
	print(json.dumps(regions, ensure_ascii=False, indent=4))