# -*- coding: utf-8 -*- 

import getVotes
import getParties
import getRegions

import json
from flask import Flask, request, send_from_directory
app = Flask(__name__)

@app.route("/")
def indexRequest():
	return "<h1>Hej!</h1>"

@app.route("/<path:reqPath>")
def jsRequest(reqPath):
	if reqPath.endswith("/"):
		reqPath += "index.html"
	response = send_from_directory("pages/", reqPath)
	return response

@app.route("/getVotes/")
def getVotesRequest():
	electionType = request.args.get("val")
	region = request.args.get("region")

	response = app.response_class(
		response= json.dumps(getVotes.getVotes(electionType, region), ensure_ascii=False),
		mimetype="application/json"
	)
	return response

@app.route("/getParties/")
def getPartiesRequest():
	electionType = request.args.get("election")
	region = request.args.get("region")
	
	response = app.response_class(
		response= json.dumps(getParties.getParties(electionType, region), ensure_ascii=False),
		mimetype="application/json"
	)
	return response

@app.route("/getRegions/")
def getRegionsRequest():
	region = request.args.get("region")
	rType = request.args.get("type")
	
	if rType == "riksdagskrets":
		regions = getRegions.getRiksdagskrets()
	elif rType == "kommun":
		regions = getRegions.getKommuner(region)
	elif rType == "kommunKrets":
		regions = getRegions.getKommunKretsar(region)
	elif rType == "kommunDistrikt":
		regions = getRegions.getKommunDistrikt(region)
	else:
		regions = {"error": "Not an allowed region type"}

	response = app.response_class(
		response= json.dumps(regions, ensure_ascii=False),
		mimetype="application/json"
	)
	return response

if __name__ == "__main__":
	app.run(debug=True)