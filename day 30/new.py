# # file not found error
# try:
#     file=open("file.txt")
# except:
#     with open("file.txt","w") as file:
#         file.write("hello")

# fruits=["Apple","Pear","Orange"]

# def make_pie(index):
#     try:
#         fruit=fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit +"pie")

# make_pie(3)


fb_post=[
{"Like":1,"Share":1},
{"Like":2},
{"Share":1},
{"Like":2},
]
total_likes=0
for post in fb_post:
    try:
        total_likes+=post["Like"]  
    except KeyError:
        ...

print(total_likes)










