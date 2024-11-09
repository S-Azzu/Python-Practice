f=open('chapter.txt','r')
a=f.read()
if 'caste!' in a:
    print("yes")
else:
    print("no")
f.close()