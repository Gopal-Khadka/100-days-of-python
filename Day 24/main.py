# TODO: create a new file
with open('/home/gopal/Downloads/backup/python/day 24/file.txt',mode="a") as my_file:
        
    # for i in range(13):
    #     content=my_file.readline()
    #     print(content,sep=" ")

    my_file.write("Line -1")

with open('/home/gopal/Downloads/backup/python/day 24/new_file.txt',mode="w") as my_file:
    my_file.write("hallo")
