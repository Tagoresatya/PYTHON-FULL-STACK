'''
media = ['beach.png','waves.mp4','mountain.jpg','party.jpg','dance.mp4',
         'selfie.jpg','birthday.png','concert.jpg','singing.mp4','sunset.jpg']

png = ['beach.png','birthday.png']
jpg = ['mountain.jpg','party.jpg','selfie.jpg','concert.jpg','sunset.jpg']
mp4 = ['waves.mp4','dance.mp4','singing.mp4']

sent_items = input('Selet the files to share: ')

'''


media = ['beach.png','waves.mp4','mountain.jpg','party.jpg','dance.mp4',
         'selfie.jpg','birthday.png','concert.jpg','singing.mp4','sunset.jpg']

photos=[]
videos=[]

for i in media:
    if i.endswith('.mp4'):
        videos.append(i)
    else:
        photos.append(i)

print('\n----------photos---------')
for i in photos:
    print(i)

print('\n--------videos----------')
for i in videos:
    print(i)


select = set(input("Enter the files to share (using) comma): ").split(','))
for i in select:
    if i in media:
        print(f'{i}-sent')
    else:
        print(f'{i}-file not found')
        
