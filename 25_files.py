#realine data 
f=open('chapter.txt','r')
data=f.readline()
print(data)
f.close()

f=open("chapter.txt","r")
data=f.read()
print(data)
f.close()