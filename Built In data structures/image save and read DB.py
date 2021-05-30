#image save and read from db
f=open('IMG1.JPG','rb')
f1=open('myPic.JPG','wb')

for i in f:
    f1.write(i)