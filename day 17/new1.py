# class User:
#     pass

# user1=User()

# def hello():
#     pass

# hello()
# # pascal case: use capital letters in class word eg:PascalCase
# # camelcase: first letter small but others capital eg: camelCase
# # snake case:all lower case and underscore eg: snake_case


""""Defining class"""


class User():
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.follower = 0
        self.following = 0

        """Thease above are attributes(properties of objects)"""
        # now time for method or functions
    def follow(self,user):
        """user who you are following have one more followers"""
        user.follower+=1
        """your following count also goes up"""
        self.following+=1

    # """Everytime the class gets used this gets triggered."""
    # print("new user created.")


"""Creating objects using class"""
user1 = User(500, "Gopal")
user2=User(512,"Harry")
user1.follow(user2)

print(user1.following)
print(user2.follower)


# user1.id = "512"
# # assigning attributes(variable) to objects

# """name is a attribute but user_name is a parameter"""
# print(user1.name)
# print(user1.follower)


# user2 = User()
# user2.id = "512"
# # assigning attributes(variable) to objects
# user2.username = "Gopal"
# print(user2.username)

"""THis above method is inefficient for creatng lot of objects"""
"""It is time to use constructor or initializing object"""
