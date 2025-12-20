#single inheritance
class whatsapp_v1:
    def messaging(self):
        print("you can message")
    def sendpics(self):
        print("you can send pics")
class whatsapp_v2(whatsapp_v1):
    def uploadstatus(self):
        print("you can upload the status")
    def videos(self):
        print("you can upload the videos")
        
imran = whatsapp_v1()
print("imran-v1")
imran.messaging()
imran.sendpics()
suma = whatsapp_v2()
print("suma-v2")
suma.uploadstatus()
suma.videos()
suma.sendpics()
suma.messaging()
#Multilevel
class whatsapp_v1:
    def messaging(self):
        print("you can message")
    def sendpics(self):
        print("you can send pics")
class whatsapp_v2(whatsapp_v1):
    def uploadstatus(self):
        print("you can upload the status")
    def videos(self):
        print("you can upload the videos")
class whatsapp_v3(whatsapp_v2):
    def calls(self):
        print("you can call")
    def groups(self):
        print("you can have groups")
        
imran = whatsapp_v1()
print("imran-v1")
imran.messaging()
imran.sendpics()
suma = whatsapp_v2()
print("suma-v2")
suma.uploadstatus()
suma.videos()
suma.sendpics()
suma.messaging()
ran=whatsapp_v3()
print("ran-v3")
ran.uploadstatus()
ran.videos()
ran.sendpics()
ran.messaging()
ran.calls()
ran.groups()

#multiple
class whatsapp_v1:
    def messaging(self):
        print("you can message")
    def sendpics(self):
        print("you can send pics")
class whatsapp_v2(whatsapp_v1):
    def uploadstatus(self):
        print("you can upload the status")
    def videos(self):
        print("you can upload the videos")
class whatsapp_v3(whatsapp_v2):
    def calls(self):
        print("you can call")
    def groups(self):
        print("you can have groups")
class community:
    def clubgroup(self):
        print("you can create a community with clubbing the group ")
class meta:
    def ai(self):
        print("you can chat")

class whatsapp_v4(whatsapp_v3,community,meta):
    def channel(self):
        print("you can create channel to engage")
imran = whatsapp_v1()
print("imran-v1")
imran.messaging()
imran.sendpics()
suma = whatsapp_v2()
print("suma-v2")
suma.uploadstatus()
suma.videos()
suma.sendpics()
suma.messaging()
ran=whatsapp_v3()
print("ran-v3")
ran.uploadstatus()
ran.videos()
ran.sendpics()
ran.messaging()
ran.calls()
ran.groups()
ruchi=whatsapp_v4()
print("ruchi-v4")
ruchi.messaging()
ruchi.sendpics()
ruchi.uploadstatus()
ruchi.videos()
ruchi.calls()
ruchi.groups()
ruchi.clubgroup()
ruchi.ai()
#hierarchical
class whatsapp_v1:
    def messaging(self):
        print("you can message")
    def sendpics(self):
        print("you can send pics")
class whatsapp_v2(whatsapp_v1):
    def uploadstatus(self):
        print("you can upload the status")
    def videos(self):
        print("you can upload the videos")
class whatsapp_v3(whatsapp_v2):
    def calls(self):
        print("you can call")
    def groups(self):
        print("you can have groups")
class community:
    def clubgroup(self):
        print("you can create a community with clubbing the group ")
class meta:
    def ai(self):
        print("you can chat")
class meta1(meta):
    def generateimages(self):
        print("you can generate images")
class meta2(meta):
    def human_emotions(self):
        print("you can share your feelings")
class meta3(meta1,meta2):
    def technical(self):
        print("you can tech questions")
class whatsapp_v4(whatsapp_v3,community,meta3):
    def channel(self):
        print("you can create channel to engage")
imran = whatsapp_v1()
print("imran-v1")
imran.messaging()
imran.sendpics()
suma = whatsapp_v2()
print("suma-v2")
suma.uploadstatus()
suma.videos()
suma.sendpics()
suma.messaging()
ran=whatsapp_v3()
print("ran-v3")
ran.uploadstatus()
ran.videos()
ran.sendpics()
ran.messaging()
ran.calls()
ran.groups()
ruchi=whatsapp_v4()
print("ruchi-v4")
ruchi.messaging()
ruchi.sendpics()
ruchi.uploadstatus()
ruchi.videos()
ruchi.calls()
ruchi.groups()
ruchi.clubgroup()
ruchi.ai()
varsha=whatsapp_v4()
print("ruchi-v4")
varsha.messaging()
varsha.sendpics()
varsha.uploadstatus()
varsha.videos()
varsha.calls()
varsha.groups()
varsha.clubgroup()
varsha.ai()

varsha.generateimages()
varsha.human_emotions()
varsha.technical()

# when the parent class and child class has same methods. To access same methods
#super method
class whatsapp_v1:
    def sendpics(self):
        print("you can send pics")
class whatsapp_v2(whatsapp_v1):
    def sendpics(self):
        super().sendpics()
        print("you can like pics")
ruchitha=whatsapp_v2()
ruchitha.sendpics()

class whatsapp_v1:
    def sendpics(self):
        print("you can send pics")
class whatsapp_v2():
    def sendpics(self):
        print("you can like pics")
class whatsapp_v3(whatsapp_v1,whatsapp_v2):
    def sendpics(self):
        whatsapp_v1.sendpics(self)
        whatsapp_v2.sendpics(self)
        print("you can add music")      
ruchitha=whatsapp_v3()
ruchitha.sendpics()
        
