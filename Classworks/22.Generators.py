def reels(data):
    for i in data:
        yield i
data=['1..100','100..200','200..300','300..400']
scroll=reels(data)
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))

#or
def reels(data):
    for i in data:
        yield i
data=['1..100','100..200','200..300','300..400']
scroll=reels(data)
while True:
    ch=input(f"{S}croll or {B}ack")
    if ch =='s':
        print(next(scroll))
    else:
        print("Exit")
        break
