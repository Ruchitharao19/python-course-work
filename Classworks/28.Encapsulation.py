#encapsulation

class Instagram:
    def __init__(self,username,pwd):
        print("welcome")
        self.username=username
        self.__password=pwd
        self._post=[]
    def getpassword(self):
        return self.__password
    def setpassword(self,newpassword):
        self.__password=newpassword
        print("password updated")
    @property
    def viewPost(self):
        return self._post
    @viewPost.setter
    def viewPost(self,post):
        self._post.append(post)
ruchitha=Instagram("ruchitha","123")
print(f"before:{ruchitha.username}")
ruchitha.username="ruchi"
print(f"after:{ruchitha.username}")

print(f"before:{ruchitha.getpassword()}")
ruchitha.setpassword("ruchi")
print(f"after:{ruchitha.getpassword()}")

print(ruchitha.viewPost)
ruchitha.viewPost = "hello"
ruchitha.viewPost = "first reel"
print(ruchitha.viewPost)
