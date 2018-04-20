import getVotes
import getParties

import json
from flask import Flask, request, send_from_directory
app = Flask(__name__)

@app.route("/")
def indexRequest():
	return "<h1>Hej!</h1>"

@app.route("/<path:reqPath>")
def jsRequest(reqPath):
	print("Hej")
	response = send_from_directory("pages/", reqPath)
	return response

@app.route("/getVotes/")
def getVotesRequest():
	electionType = request.args.get("val")
	region = request.args.get("region")

	response = app.response_class(
        response= json.dumps(getVotes.getVotes(electionType, region)),
        mimetype="application/json"
    )
	return response

@app.route("/getParties/")
def getPartiesRequest():
	electionType = request.args.get("val")
	region = request.args.get("region")

	response = app.response_class(
        response= json.dumps(getParties.getParties(electionType, region)),
        mimetype="application/json"
    )
	return response

@app.route("/valnatt/")
def valnattRequest():
	response = send_from_directory("pages/", "votes.html")
	return response

if __name__ == "__main__":
	app.run(debug=True)