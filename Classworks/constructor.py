class Instagram:
    def __init__(self,username,pwd):
        self.username=username
        self.password=pwd
        self.bio=''
        self.followers={}
        self.following={}
        print("Welcome to the Instagram. Have Fun!")
        print(f"Username:{self.username}")
        print(f"Username:{self.password}")
ruchitha=Instagram("ruchitha","123")



