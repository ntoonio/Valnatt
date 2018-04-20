function getParameterByName(name, url) {
	if (!url) url = window.location.href;
	name = name.replace(/[\[\]]/g, "\\$&");
	var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
		results = regex.exec(url);
	if (!results) return null;
	if (!results[2]) return "";
	return decodeURIComponent(results[2].replace(/\+/g, " "));
}

const election = getParameterByName("election")
const region = getParameterByName("region")

var parties = []

$.getJSON("/getVotes?val=" + election + "&region=" + region, function (data) {
	
	var parties = []

	for (var party in data["RÖSTER"]) {
		parties.push(data["RÖSTER"][party]);
	}

	document.getElementById("region").innerText = data["NAMN"]

	const mostVotes = parties.slice().sort(function (a, b) {
		if (parseInt(a["RÖSTER"]) > parseInt(b["RÖSTER"])) {return -1}
		if (parseInt(a["RÖSTER"]) < parseInt(b["RÖSTER"])) {return 1}
		return 0 
	})[0]["RÖSTER"]

	$.getJSON("/getParties?val=" + election + "&region=" + region, function (data) {
		const width = ((100 - parties.length - 2) / parties.length) + "vw"
		
		parties.forEach(function (party) {
			const pillar = document.createElement("div")
			pillar.style.height = party["RÖSTER"] / mostVotes * 100 + "%"
			pillar.style.width = width;
			
			const color = data.find(function (p) {
				return p["FÖRKORTNING"] == party["PARTI"]
			})["FÄRG"]

			pillar.style.backgroundColor = color
			pillar.classList.add("pillar")
			document.getElementById("stats").appendChild(pillar)
		})
	})
})