from datetime import datetime
import requests

# response=requests.get(url="http://api.open-notify.org/iss-now.json")
# code=response.status_code
# response.raise_for_status()
# data=response.json()
# print(data["iss_position"])
position={
    "lat": 37.7749,
    "lng": -122.4194,
    "formatted":0,
}
responses=requests.get(url="http://api.sunrise-sunset.org/json",params=position)
responses.raise_for_status()
data=responses.json()
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]
exact_hr_sunrise=sunrise
exact_hr_sunset=sunset
print(exact_hr_sunrise)
print(exact_hr_sunset)

now=datetime.now().hour
print(now)