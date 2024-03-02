class StarCookie:
    milk = 0.1
    
    def __init__(self,color, weight):
        self.color = color
        self.weight = weight

star_cookie1 = StarCookie("Brown",20)
star_cookie2 = StarCookie("Chocolate", 22)
# star_cookie1.milk = 0.2
StarCookie.milk = 0.2

print(star_cookie1.__dict__)
print(star_cookie2.__dict__)
print(StarCookie.__dict__)

# print(star_cookie1.weight)
# print(star_cookie1.color)
# print(star_cookie1.milk)

# print(star_cookie2.weight)
# print(star_cookie2.color)
# print(star_cookie2.milk)



# class Youtube:
#     def __init__(self, username, subscribers=0):
#         self.username = username
#         self.subscribers = subscribers

# user1 = Youtube("Shadow")
# print(user1.username)
# print(user1.subscribers)

# user2 = Youtube("Dark")
# user2.subscriber = 234
# print(user2.username)
# print(user2.subscriber)