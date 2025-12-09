n=int(input ("Enter the no of message: "))
data={}
for i in range (n) :
    name, msg=input().split(':')
    if name in data:
        data[name].append(msg)
    else:
        data[name]=[msg]
print(data)
choices={
    1: 'Count total number of messages',
    2: 'Identify unique users in the chat',
    3: 'Count total words in the chat',
    20: 'Exit'
}
while True:
    for i in choices:
        print (f'{i}.{choices[i]}')
    ch=int(input("Enter the choice: "))
    if ch==1:
        cnt=0
        for i in data:
            cnt+=len(data[i])
        print(f"-----------Total number of messages: {cnt}---------")
    elif ch==2:
        print(f"------------unique users in the chat--------------")
        for i in data:
            print (i)
    elif ch==3:
        '''
words=msg.split()
        count=len(words)
        print(f"-----------Total words in the chat: {count}--------")'''
        count=0
        for word in msg.split():
            count+=1
        print(f"-----------Total words in the chat: {count}--------")
    elif ch==20:
        print("End of the program")
        break
    else:
        print("Exit")
        
