console.log("Heksan")

const election = "R"
const region = "01170211"

var parties = []

$.getJSON("/getVotes?val=" + election + "&region=" + region, function (data) {
	
	var parties = []

	for (var party in data) {
		parties.push(data[party]);
	}

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