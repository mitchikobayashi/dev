wdays=['月','火','水','木','金']
print(wdays[1])

wdays=['月','火','水','木','金']
wdays[1]='炎'
print(wdays)

wdays=['月','火','水','木','金']
for day in wdays:
    print(day, '曜日')

wdays=['月','火','水','木','金']
for day in wdays[1:4]:
    print(day, '曜日')

wdays=['月','火','水','木','金']
day=wdays[1:4]
print(day, '曜日')

for cnt in range(10):
    print('ハロー')

for cnt in range(10):
    print(cnt, '回目のハロー！')

for cnt in range(1,11):
    print(cnt,'回目のハロー')

for cnt1 in range(1,10):
    for cnt2 in range(1,10):
        print(cnt1*cnt2)

for cnt1 in range(1,10):
    for cnt2 in range(1,10):
        print(cnt1,'X',cnt2, '=',cnt1*cnt2)

shikin=50000
while shikin>=0:
    print(shikin)
    shikin=shikin-5080

team=['A','B','C','D','E']
for t1 in team:
    for t2 in team:
        print(t1,'vs',t2)

team=['A','B','C','D','E']
for t1 in team:
    for t2 in team:
        if t1 != t2:
            print(t1, 'vs', t2)

team=['A','B','C','D','E']
opps=['A','B','C','D','E']
for t1 in team:
    opps.remove (t1)
    for t2 in opps:
        print(t1, 'vs', t2)

direction=['東','西','南','北']
for d in direction:
    print(d)

wdays=['月','火','水','木','金']
for day in wdays[0:3]:
    print(day, '曜日')


for cnt1 in range(1,4):
    for cnt2 in range(1,5):
        print(cnt1,'X',cnt2,'=',cnt1*cnt2)