# Day 17

# How to create class?
class sample:
    pass


# Here i created an empty class which I will be working with Later

# initializing a class using constructor
class user:
    def __init__(self, uid, username, location):
        self.id = uid
        self.name = username
        self.location = location
        print("user object is created")


Nayan = user(7, "Nayan Awasthi", "Bangalore")  # here I created an object using user class and initialized it with data
print(Nayan.name, Nayan.location)


class insta_usr:
    def __init__(self, uid, username):
        self.id = uid
        self.name = username
        self.followers = 0
        self.following = 0
        print("insta user object is created")

    def follow(self, usr):
        """
        Method to follow others in Social media
        :param usr:
        :return:
        """
        usr.followers += 1
        self.following += 1


nyn1 = insta_usr(12, "Kaka")
nyn2 = insta_usr(11, "laka")
# Before using Follow Method
print(nyn1.following)
print(nyn1.followers)
print("_")
nyn1.follow(nyn2)
# After using Follow Method
print(nyn1.following)
print(nyn1.followers)
print("_")
# After your follow method the followers number increased for other instagram user
print(nyn2.following)
print(nyn2.followers)
