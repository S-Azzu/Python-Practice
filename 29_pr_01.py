def game():
    return 500
score=game()
with open('chapter.txt')as f:
    chapter=int(f.read())
if chapter<score:
    with open('chapter.txt','w')as f:
        f.write(str(score))