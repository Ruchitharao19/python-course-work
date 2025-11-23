#list
lang=['python','java','c','c++','mysql','ds','flask','javascript']
for i in lang:
    print(i)
for i in enumerate(lang):
    print(i,i[0],i[1])
#tuple
lang=('python','java','c','c++','mysql','ds','flask','javascript')
for i in lang:
    print(i)
for i in enumerate(lang):
    print(i,i[0],i[1])
#set
lang={'python','java','c','c++','mysql','ds','flask','javascript'}
for i in lang:
    print(i)
#dict
lang={1:'python',2:'java',3:'c',4:'c++',5:'mysql',6:'ds',7:'flask',8:'javascript'}
for i in lang:
    print(f'key-{i} value-{lang[i]}')
          
for i in enumerate(lang):
    print(f'index-{i[0]} key-{i[1]} valu-{lang[i[1]]}')
#string
lang="python programming"
for i in lang:
    print(f'{i}')
for i in enumerate(lang):
    print(f'index-{i[0]}val-{i[1]}')

#for var in range(start,end+1,step):
for i in range(1,11,1):
    print(i)
    
    
