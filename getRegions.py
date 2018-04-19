import xmltodict
import io

def readFile(fileCode):
	fileName = "data/valnatt_" + fileCode + ".xml"
	with io.open(fileName, "r", encoding="iso-8859-1") as xml_file:
		obj = xmltodict.parse(xml_file.read(), attr_prefix="")

	return obj

def getRegions(path):
	if path == "":
		obj = readFile("00R")
		resp = []
		for l in obj["VAL"]["NATION"]["LÄN"]:
			resp.append({"NAMN": l["NAMN"], "KOD": l["KOD"]})

		return resp
	elif len(path) == 2:
		obj = readFile("00R")
		resp = []
		for l in obj["VAL"]["NATION"]["LÄN"]:
			if l["KOD"] == path:
				with open("hej.json", "w") as f:
					json.dump(l, f, ensure_ascii=False)
				print(json.dumps(l["KRETS_RIKSDAG"], indent=4))
				for k in l["KOMMUN"]:
					print(k)

		return resp

if __name__ == "__main__":
	import json

	regions = getRegions("01")
	print(json.dumps(regions, ensure_ascii=False, indent=4))