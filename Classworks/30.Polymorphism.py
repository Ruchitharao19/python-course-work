#method overriding
class hotstar:
    def __init__(self,username):
        print(f"hi {username} welcome to hotstar".center(30,"-"))
    def playvideo(self):
        print("movie with ads")
        print("limited access for movies")
        print(" quality is limited")
        print("one device login ")
        print("no download option")
        print("limit access")
        print("low sound quality")
    def login(self):
        print("movie with ads")
    def interface(self):
        print("interface")
    def profile(self):
        print("profile is same")
class premiumuser(hotstar):
    def __init__(self,username):
        print(f"hi {username} welcome to hotstar .enjoy you premium")
    def playvideo(self):
        print("movie without ads")
        print("unlimited access for movies")
        print("high quality")
        print("multiple device login ")
        print("download option is available")
        print("live access")
        print("improved sound quality")
ruchi=hotstar("ruchi")
ruchi.playvideo()
ruchi.login()
varsha=premiumuser("varsha")
varsha.playvideo()
varsha.login()
print("----------------")

class instagram:
    def feed(self):
        print("feed is same for all")
    def scroll(self):
        print("scroll is same for all")
    def share(self):
        print("share is same for all")
    def like(self):
        print("like is same for all")
    def repost(self):
        print("repost is same for all") 
    def comment(self):
        print("like is same for all")
    def profile(self):
        print("no professional dashboard ")
    def posting(self):
        print("no insights are available")
class creator(instagram):
    def profile(self):
        print("professional dashboard is added in their grid")
    def posting(self):
        print("you can see reach, activities")
ruchi=creator()
ruchi.profile()
ruchi.posting()
varsha=instagram()
varsha.profile()
varsha.posting()
#overloading
class number:
    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        return self.num+other.num
    def __sub__(self,other):
        return self.num-other.num
n1=number(10)
n2=number(20)
print(n1+n2)
print(n1-n2)       
