travel_vlog=[
	{"country":"German",
	"visits":12,
	"cities":["berlin 1","berlin2","lijon"]
	},
	{"country":"Nepal",
	"visits":1,
	"cities":["ktm 1","bkt","ptn"]
	},
]

def new_country(country1,visit,city):
	dict1={
	"country":country1,
	"visits":visit,
	"cities":city
		}
	travel_vlog.append(dict1)
	

new_country("russia",2,["cech","russ","xyoen"])
print(travel_vlog)