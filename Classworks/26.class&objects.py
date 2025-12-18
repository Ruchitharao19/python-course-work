class Instagram:
    settings=['Insites', 'Status', 'Privacy']
    @classmethod
    def settingsupdate(cls):
        print(cls.settings)
    @staticmethod
    def welcome():
        print("Welcome to the Instagram. Have Fun!!!")
    def userdetails(self, username, password, bio=''):
        self.username=username
        self.password=password
        self.bio=bio
        print (f"Hello {self.username}")
randheer=Instagram()
randheer.userdetails("Randheer", "r@123")
print(randheer.username)
print(randheer.password)
print(randheer.bio)
print(randheer.settings)
print(Instagram.settings)
randheer.settingsupdate()
Instagram.settingsupdate()
randheer.welcome()
Instagram.welcome()
