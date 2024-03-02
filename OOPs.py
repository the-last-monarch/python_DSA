# class StarCookie:
#     milk = 0.1
    
#     def __init__(self,color, weight):
#         self.color = color
#         self.weight = weight

# star_cookie1 = StarCookie("Brown",20)
# star_cookie2 = StarCookie("Chocolate", 22)
# # star_cookie1.milk = 0.2
# StarCookie.milk = 0.2

# print(star_cookie1.__dict__)
# print(star_cookie2.__dict__)
# print(StarCookie.__dict__)

# print(star_cookie1.weight)
# print(star_cookie1.color)
# print(star_cookie1.milk)

# print(star_cookie2.weight)
# print(star_cookie2.color)
# print(star_cookie2.milk)



class Youtube:
    def __init__(self, username, subscribers=0, subscription=0):
        self.username = username
        self.subscribers = subscribers
        self.subscription = subscription
    
    def subscribe(self, user):
        user.subscribers += 1
        self.subscription += 1

user1 = Youtube("Shadow")
user2 = Youtube("Dark")
user1.subscribe(user2)

print(user1.username)
print(f"user1 subscribers are {user1.subscribers}")
print(f"user1 subscription are {user1.subscription}")

print(user2.username)
print(f"user2 subscribers are {user2.subscribers}")
print(f"user2 subscription are {user2.subscription}")