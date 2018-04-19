import io
import xmltodict

def getParties(election, region):
	obj = readFile(region[:4] + election)
	resp = []

	for p in obj["VAL"]["PARTI"]:
		resp.append(p)
	
	return resp

def readFile(fileCode):
	fileName = "data/valnatt_" + fileCode + ".xml"
	with io.open(fileName, "r", encoding="iso-8859-1") as xml_file:
		obj = xmltodict.parse(xml_file.read(), attr_prefix="")

	return obj

if __name__ == "__main__":
	import json

	parties = getParties("K", "0117")
	print(json.dumps(parties, ensure_ascii=False, indent=4))