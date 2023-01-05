import requests
from datetime import datetime

# --------------------CONSTANTS FOR ACCOUNT------------------------------#
TOKEN = "bfiugviuiuiwugfi578962ncn"
USERNAME = "whateverid"

today = datetime.now() #GIVES TODAY'S DATE

# -------------------JSON PARAMETERS FOR ENDPOINTS------------------------# 
user_params = {
    "token": TOKEN,
    "agreeTermsOfService": "yes",
    "username": USERNAME,
    "notMinor": "yes",
}

graph_params = {
    "id": "graph1",
    "color": "sora",
    "unit": "days",
    "type": "int",
    "name": "habit_graph",
}

pixel_post_param = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20",
}
pixel_put_param = {"quantity": "20"}
# -----------------------HEADER FOR HTTP HEADER--------------------------#
headers = {"X-USER-TOKEN": TOKEN}
# -----------------------ENDPOINTS FOR REQUEST---------------------------#
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_post_endpoint = f"{graph_endpoint}/{graph_params['id']}"
pixel_put_endpoint = f"{pixel_post_endpoint}/{today.strftime('%Y%m%d')}"
pixel_delete_endpoint=pixel_put_endpoint

# create user
create_user=requests.post(pixela_endpoint,params=user_params)
print(create_user.text)
# Note:Create user first to do below actions.

# create graph
graph_response=requests.post(graph_endpoint,json=graph_params,headers=headers)
print(graph_response.text)

# post pixel on the graph
pixel_post = requests.post(pixel_post_endpoint, json=pixel_post_param, headers=headers)
print(pixel_post.text)

# replace pixel on graph
pixel_put=requests.put(pixel_put_endpoint,headers=headers,json=pixel_put_param)
print(pixel_put.text)

# delete data 
pixel_delete= requests.delete(pixel_put_endpoint, headers=headers)
print(pixel_delete.text)
