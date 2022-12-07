# nesting dict

#nesting list and dictionary inside dictionary
travel_vlog={
	"France":["Paris","lijon","Another City"],
	"German":"Berlin",
	"Nepal":{"cities_visited":["Ktm","Bkt","Patan"],
				"Total visits":12,
				"Left_visits":65,
				}	
				
				}
print(travel_vlog)
print(type(travel_vlog))
print()

travel_vlog1=[
	{
	"France":["Paris","lijon","Another City"],
	"German":"Berlin",
	"Nepal":{"cities_visited":["Ktm","Bkt","Patan"],
				"Total visits":12,
				"Left_visits":65,
				}	
	}			
				]
				
print(travel_vlog1)
print(type(travel_vlog1))
